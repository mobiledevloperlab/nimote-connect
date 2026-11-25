# Nimote Connect

**English** · [简体中文](docs/zh/README.md) · [Español](docs/es/README.md) · [日本語](docs/ja/README.md) · [한국어](docs/ko/README.md)

**Connect to your development computer from your phone and pick up your terminal and AI coding sessions.**

Nimote Connect is the commercial companion service for NimoteCode. It installs Connect and Host on your development computer. Use a compatible NimoteCode client to open your workspace, review changes, handle approvals, and resume work. Your project files, worktrees, and agents stay on your computer.

[Downloads and release notes](https://github.com/mobiledevloperlab/nimote-connect/releases) · [Installation and connection](docs/en/install.md)

## What you can do

| Use case | How Nimote Connect helps |
| --- | --- |
| Resume from your phone | Open a remote terminal, view session history, Git diffs and check results, and review pending approvals. Host works with Codex, Claude Code via ACP, and OpenCode when installed and configured on the computer. |
| Connect over the internet | Pair the computer with a device code. Internet access is off by default. When enabled, it uses a direct peer-to-peer connection when possible and can fall back to a DERP relay. OpenSSH still authenticates the account and lets you verify the host fingerprint. |
| Keep your existing SSH setup | Reuse your SSH connection. With a personal Tailscale network, enter the computer's Tailscale address and SSH port in NimoteCode. |
| Take a GitHub issue to review | Use the computer's authorized GitHub CLI (`gh`) to dispatch an issue to a local agent. Work happens in a separate Git worktree with checks you specify. Resume after a failed check using the retained workspace. After checks pass, create a draft PR manually or enable automatic draft creation for that task. |
| Upgrade from NimoteHost Community | On macOS or Linux, run the installer as the original account to retain the standard SSH entry point, Host data, and history. The installer pauses the upgrade while tasks are active. |

## Downloads

Pick the archive for your system and architecture and verify it with the matching `.sha256` file. Check each release note for available builds, compatible clients, and validation coverage. [GitHub Releases](https://github.com/mobiledevloperlab/nimote-connect/releases)

| Platform | Architectures | Package |
| --- | --- | --- |
| macOS | Apple silicon `arm64`, Intel `amd64` | `.tar.gz`, see the release notes for CLI or desktop availability |
| Linux | `amd64`, `arm64` | CLI `.tar.gz`, requires a systemd user session |
| Windows | `amd64` (x64), `arm64` | CLI `.zip` with a PowerShell installer and per-user background tasks |

Install, upgrade, and rollback were tested locally on macOS, with the Intel build tested under Rosetta. Linux and Windows CLI builds were cross-compiled. Native platform validation and the full connection flow with the official client are still pending.

## Closed-source distribution

**Nimote Connect's proprietary implementation is closed source.** This repository contains public product documentation, release automation, and installer packages. GitHub's automatically generated `Source code (zip)` and `Source code (tar.gz)` are snapshots of this repository. Download the platform installer from the release assets.

The commercial package uses the public NimoteHost Community core and ships third-party notices for the applicable components. [NimoteHost Community](https://github.com/mobiledevloperlab/nimotehost) · [Release maintenance guide (简体中文)](docs/release/README.md)
