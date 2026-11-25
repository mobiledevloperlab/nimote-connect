# Nimote Connect

[English](../../README.md) · **简体中文** · [Español](../es/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md)

**从手机连回自己的开发电脑，继续终端、代码和 AI 开发任务。**

Nimote Connect 是安装在开发电脑上的商业版连接与开发服务，配合 NimoteCode 使用。你可以在 Mac、Linux 或 Windows 上运行 Host，从兼容的客户端连接这台电脑，查看会话、操作终端、检查改动，或继续已有的开发任务。项目文件和工作区保存在开发电脑上，Agent 也在这台电脑上运行。

[下载与版本说明](https://github.com/mobiledevloperlab/nimote-connect/releases) · [安装与连接](install.md)

## 你可以用它做什么

| 使用场景 | Nimote Connect 提供的能力 |
| --- | --- |
| 离开电脑后继续开发 | 从 NimoteCode 进入远程工作区，使用终端，查看会话历史、Git 差异和验证结果，处理待审批操作。Host 可对接电脑上已安装并配置的 Codex、Claude Code（通过 ACP）和 OpenCode。 |
| 从外网连接自己的电脑 | 用设备码绑定电脑，按需开启公网连接。网络条件允许时点对点直连，直连不可用时可通过 DERP 中继。公网连接默认关闭，也可随时在桌面端或命令行关闭。 |
| 沿用已有网络 | 继续使用现有 SSH 入口。在已有个人 Tailscale 网络中，也可以在 NimoteCode 填写电脑的 Tailscale 地址和 SSH 端口，通过同一个 Host 访问工作区。 |
| 把 GitHub Issue 变成可审查的改动 | 在授权仓库中把 Issue 派发给本机 Agent，在独立 Git worktree 中开发和运行指定检查。检查失败时可保留现场并续跑。检查通过后可手动创建草稿 PR，或为任务显式启用自动创建草稿 PR。 |
| 从 NimoteHost Community 升级 | 在 macOS 或 Linux 上使用原安装账户运行商业包安装器，沿用标准 SSH 入口、Host 数据和历史。安装器检测到进行中的任务会暂停升级，待任务结束后可以重试。 |

公网连接通过电脑上的 OpenSSH 完成登录，保留 SSH 账号认证与主机指纹校验。GitHub Issue 编排沿用电脑上已授权的 GitHub CLI（`gh`），并记录开发、验证和评审阶段，便于在中途失败后定位并继续处理。

## 下载

请在 [GitHub Releases](https://github.com/mobiledevloperlab/nimote-connect/releases) 选择对应操作系统和架构的安装包，并下载同名 `.sha256` 文件。安装前比较归档的 SHA-256 与校验文件。可下载的版本、适用客户端和已验证范围以每条发布说明为准。

| 平台 | 架构 | 安装包 |
| --- | --- | --- |
| macOS | Apple 芯片 `arm64`、Intel `amd64` | `.tar.gz`，CLI 或桌面应用的供应情况见发布说明 |
| Linux | `amd64`、`arm64` | 命令行 `.tar.gz`，需要 systemd 用户会话 |
| Windows | `amd64`（x64）、`arm64` | 命令行 `.zip`，通过 PowerShell 安装，后台任务在当前用户登录时运行 |

这些是项目当前的打包范围。macOS 安装、升级和回滚已通过本地制品验收，其中 Intel 版通过 Rosetta 验证。Linux 和 Windows 当前有命令行交叉构建产物，原生平台验收以及正式客户端的完整连接流程仍待验证。

## 闭源发行

**Nimote Connect 的专有实现为闭源软件。** 本仓库用于产品介绍、公开文档和已批准的安装包分发，Git 历史只存放公开资料。GitHub Releases 自动列出的 `Source code (zip)` 和 `Source code (tar.gz)` 是本公开仓库对应标签的快照。请从同一版本的附件区下载平台安装包。

商业包使用 [NimoteHost Community](https://github.com/mobiledevloperlab/nimotehost) 的公开核心。随包分发的第三方许可证和声明适用于各自的组件。[发布说明维护指南](../release/README.md)
