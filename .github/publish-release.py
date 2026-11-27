"""Validate tracked packages and publish matching GitHub Release assets."""

import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys


ARCHIVE_NAME = re.compile(
    r"nimote-connect-(?:commercial-)?(?P<version>[0-9]+\.[0-9]+\.[0-9]+"
    r"(?:-[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*)?)-"
    r"(?P<os>darwin|linux|windows)-(?:amd64|arm64)\.(?P<ext>tar\.gz|zip)"
)
PUBLIC_VERSION = re.compile(
    r"(?P<version>(?:0|[1-9][0-9]*)(?:\.(?:0|[1-9][0-9]*)){2})"
    r"(?:-(?P<channel>beta|rc)\.(?P<number>[1-9][0-9]*))?"
)
INTERNAL_VERSION = re.compile(r"[0-9]+\.[0-9]+\.[0-9]+-(?:local|ci|dev)(?:\.|$)")


def sha256(path):
    with path.open("rb") as source:
        return hashlib.file_digest(source, "sha256").hexdigest()


def collect_assets(directory):
    releases = {}
    for sidecar in sorted(directory.glob("*.sha256")):
        if not sidecar.with_suffix("").is_file():
            raise ValueError(f"{sidecar}: missing archive")

    for path in sorted(directory.iterdir()):
        if not path.name.endswith((".tar.gz", ".zip")):
            continue
        match = ARCHIVE_NAME.fullmatch(path.name)
        if not match or (match["os"] == "windows") != (match["ext"] == "zip"):
            raise ValueError(f"{path}: invalid archive name")

        version = match["version"]
        if INTERNAL_VERSION.match(version):
            continue
        if not PUBLIC_VERSION.fullmatch(version):
            raise ValueError(f"{path}: use a stable, beta.N, or rc.N version")

        sidecar = path.with_name(path.name + ".sha256")
        if path.is_symlink() or sidecar.is_symlink() or not sidecar.is_file():
            raise ValueError(f"{path}: expected a regular archive and matching .sha256")
        digest = sha256(path)
        if sidecar.read_text(encoding="utf-8").split() != [digest, path.name]:
            raise ValueError(f"{sidecar}: SHA-256 or filename mismatch")

        assets = releases.setdefault("v" + version, {})
        assets[path] = "sha256:" + digest
        assets[sidecar] = "sha256:" + sha256(sidecar)
    return releases


def github_pages(endpoint):
    output = subprocess.check_output(
        ["gh", "api", "--paginate", "--slurp", endpoint], text=True
    )
    return [item for page in json.loads(output) for item in page]


def publish(releases, repo, target):
    endpoint = f"repos/{repo}/releases"
    existing = {release["tag_name"]: release for release in github_pages(endpoint)}
    for tag, assets in releases.items():
        release = existing.get(tag)
        if release is None:
            version = PUBLIC_VERSION.fullmatch(tag[1:])
            title = f"Nimote Connect {version['version']}"
            channel = version["channel"]
            if channel:
                label = {"beta": "Beta", "rc": "RC"}[channel]
                title += f" {label} {version['number']}"
            args = ["gh", "release", "create", tag, "--target", target, "--title", title]
            notes = Path("release") / f"{tag}.md"
            if notes.is_file():
                args.extend(["--notes-file", str(notes)])
            else:
                args.extend(["--notes", "Download the archive and its SHA-256 file for your platform."])
            if channel:
                args.extend(["--prerelease", "--latest=false"])
            subprocess.run([*args, *map(str, assets)], check=True)
            continue

        uploaded = {
            item["name"]: item.get("digest")
            for item in github_pages(f"{endpoint}/{release['id']}/assets")
            if item["state"] == "uploaded"
        }
        changed = [str(path) for path, digest in assets.items() if uploaded.get(path.name) != digest]
        if changed:
            if release.get("immutable"):
                raise ValueError(f"{tag}: assets differ from an immutable release")
            subprocess.run(["gh", "release", "upload", tag, "--clobber", *changed], check=True)
        if release["draft"]:
            subprocess.run(["gh", "release", "edit", tag, "--draft=false"], check=True)


if __name__ == "__main__":
    try:
        assets = collect_assets(Path("release"))
        if assets:
            commit = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
            publish(assets, os.environ["GH_REPO"], commit)
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        sys.exit(str(error))
