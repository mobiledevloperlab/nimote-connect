# Installation and connection

**English** · [简体中文](../zh/install.md) · [Español](../es/install.md) · [日本語](../ja/install.md) · [한국어](../ko/install.md)

[Product overview](../../README.md) · [Download installers](https://github.com/mobiledevloperlab/nimote-connect/releases)

Choose an archive for your system and architecture. Before extracting it, compare its SHA-256 digest with the matching checksum file.

## Install and pair

1. Extract the archive on the development computer. Run `./install.sh` on macOS or Linux, or `.\install.ps1` in PowerShell on Windows, as your regular user. This installs Connect and Host.
2. For desktop bundles, run `~/.local/bin/nimoteconn gui --connect` after installation and choose a connection method. CLI bundles prompt for a device code by default. To install for existing SSH and pair later, use `./install.sh --defer-login` or `.\install.ps1 -DeferLogin`. Upgrade as the original user to retain an existing binding. To require an existing binding, use `./install.sh --skip-login` or `.\install.ps1 -SkipLogin`.
3. Enable OpenSSH on the development computer. On macOS, open **System Settings → General → Sharing → Remote Login**. On Linux and Windows, start OpenSSH Server.

## Connect from NimoteCode

- **Existing SSH or personal Tailscale.** Enter the computer's SSH address or Tailscale address and its SSH port in NimoteCode.
- **Nimote internet access.** OpenSSH must listen on local TCP port 22. Pair the computer from the Connect page or run `nimoteconn login` and approve the code in NimoteCode. Then enable remote access in NimoteConn or with the CLI. When the computer shows **Registered with Nimote**, select it on your phone and open a Host session to verify the connection.

Verify the SSH host fingerprint on your first connection.

## Check and manage access

On macOS and Linux, run `~/.local/bin/nimoteconn doctor` for local diagnostics and `~/.local/bin/nimoteconn remote-access status` for internet access status. On Windows, run `& "$env:LOCALAPPDATA\NimoteConnect\nimoteconn.exe" remote-access status` in PowerShell. Use `remote-access enable` or `remote-access disable` on the same CLI to change the setting.
