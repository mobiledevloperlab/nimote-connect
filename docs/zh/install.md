# 安装与连接

[English](../en/install.md) · **简体中文** · [Español](../es/install.md) · [日本語](../ja/install.md) · [한국어](../ko/install.md)

[产品介绍](README.md) · [下载安装包](https://github.com/mobiledevloperlab/nimote-connect/releases)

请按操作系统和架构选择安装包，并在安装前比对归档的 SHA-256 与同名校验文件。

## 安装与绑定

1. **在要连接的电脑上安装。** 解压并进入安装包目录。macOS 和 Linux 用日常登录账户运行 `./install.sh`，Windows 在 PowerShell 中运行 `.\install.ps1`。安装包同时安装 Connect 和 Host。
2. **首次绑定电脑。** 按安装器提示，在与该版本匹配的客户端中批准设备码。升级时请使用原安装账户。已有绑定时，macOS 和 Linux 可用 `./install.sh --skip-login`，Windows 可用 `.\install.ps1 -SkipLogin`。
3. **启用 OpenSSH。** macOS 可从「系统设置 → 通用 → 共享 → 远程登录」开启。Linux 或 Windows 需启用 OpenSSH Server。

## 从 NimoteCode 连接

- **现有 SSH 或个人 Tailscale。** 在 NimoteCode 填写电脑的 SSH 地址或 Tailscale 地址，以及实际的 SSH 端口。
- **Nimote 公网连接。** OpenSSH 需监听本机 TCP 22。在 NimoteConn 的「Connect → 公网连接」或通过下方命令启用公网连接。等设备显示「已上线」，再从兼容的 NimoteCode 客户端选择这台电脑。

首次 SSH 连接时请核对主机指纹。

## 查看和管理公网连接

macOS 和 Linux 可用 `nimoteconnect doctor` 查看本地服务及 SSH 探测结果，用 `nimoteconnect remote-access status` 查看公网状态。Windows 可用 `& "$env:LOCALAPPDATA\NimoteConnect\nimote-connect.exe" remote-access status`。命令行通过 `remote-access enable` 或 `remote-access disable` 开关公网访问。
