# Installation and connection

**English** · [简体中文](../zh/install.md) · [Español](../es/install.md) · [日本語](../ja/install.md) · [한국어](../ko/install.md)

[Product overview](../../README.md) · [Download installers](https://github.com/mobiledevloperlab/nimote-connect/releases)

Choose an archive for your system and architecture. Before extracting it, compare its SHA-256 digest with the matching checksum file.

## Install and pair

1. Extract the archive on the development computer. Run `./install.sh` on macOS or Linux, or `.\install.ps1` in PowerShell on Windows, as your regular user. This installs Connect and Host.
2. On first install, approve the device code in a compatible client as prompted. For upgrades, use the original account. With an existing pairing, you can use `./install.sh --skip-login` or `.\install.ps1 -SkipLogin`.
3. Enable OpenSSH on the development computer. On macOS, open **System Settings → General → Sharing → Remote Login**. On Linux and Windows, start OpenSSH Server.

## Connect from NimoteCode

- **Existing SSH or personal Tailscale.** Enter the computer's SSH address or Tailscale address and its SSH port in NimoteCode.
- **Nimote internet access.** OpenSSH must listen on local TCP port 22. Turn on **Connect → Remote access** in NimoteConn or use the CLI. When the computer is **Online**, select it in a compatible NimoteCode client.

Verify the SSH host fingerprint on your first connection.

## Check and manage access

On macOS and Linux, run `nimoteconnect doctor` for local diagnostics and `nimoteconnect remote-access status` for internet access status. On Windows, run `& "$env:LOCALAPPDATA\NimoteConnect\nimote-connect.exe" remote-access status` in PowerShell. Use `remote-access enable` or `remote-access disable` on the same CLI to change the setting.
