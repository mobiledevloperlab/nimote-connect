# インストールと接続

[English](../en/install.md) · [简体中文](../zh/install.md) · [Español](../es/install.md) · **日本語** · [한국어](../ko/install.md)

[製品概要](README.md) · [インストーラーのダウンロード](https://github.com/mobiledevloperlab/nimote-connect/releases)

OS とアーキテクチャに合うパッケージを選び、展開する前に SHA-256 を対応するチェックサムファイルと照合してください。

## インストールとデバイス登録

1. 開発用コンピューターでアーカイブを展開します。普段使うアカウントで、macOS または Linux では `./install.sh`、Windows では PowerShell で `.\install.ps1` を実行し、Connect と Host をインストールします。
2. 初回は、指示に従って対応クライアントでデバイスコードを承認します。更新時は元のアカウントを使ってください。登録済みの場合は `./install.sh --skip-login` または `.\install.ps1 -SkipLogin` を使えます。
3. 開発用コンピューターで OpenSSH を有効にします。macOS では **システム設定 → 一般 → 共有 → リモートログイン** を開きます。Linux と Windows では OpenSSH Server を起動します。

## NimoteCode から接続する

- **既存の SSH または個人用 Tailscale。** コンピューターの SSH アドレスまたは Tailscale アドレスと、SSH ポートを NimoteCode に入力します。
- **Nimote のインターネット経由のアクセス。** OpenSSH がローカル TCP ポート 22 で待ち受けている必要があります。NimoteConn の **Connect** パネルまたは CLI でリモートアクセスを有効にします。コンピューターがオンラインになったら、対応する NimoteCode クライアントで選択します。

初回接続では SSH ホスト鍵のフィンガープリントを確認してください。

## 状態の確認とアクセスの管理

macOS と Linux では、`nimoteconnect doctor` でローカル診断、`nimoteconnect remote-access status` でインターネット経由のアクセス状態を確認できます。Windows では、PowerShell から `& "$env:LOCALAPPDATA\NimoteConnect\nimote-connect.exe" remote-access status` を実行します。同じ CLI の `remote-access enable` または `remote-access disable` で設定を切り替えられます。
