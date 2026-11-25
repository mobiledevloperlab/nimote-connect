# インストールと接続

[English](../en/install.md) · [简体中文](../zh/install.md) · [Español](../es/install.md) · **日本語** · [한국어](../ko/install.md)

[製品概要](README.md) · [インストーラーのダウンロード](https://github.com/mobiledevloperlab/nimote-connect/releases)

OS とアーキテクチャに合うパッケージを選び、展開する前に SHA-256 を対応するチェックサムファイルと照合してください。

## インストールとデバイス登録

1. 開発用コンピューターでアーカイブを展開します。普段使うアカウントで、macOS または Linux では `./install.sh`、Windows では PowerShell で `.\install.ps1` を実行し、Connect と Host をインストールします。
2. デスクトップ版では、インストール後に `~/.local/bin/nimoteconn gui --connect` を実行して接続方法を選びます。CLI 版では、初回インストール時にデバイスコードが表示されます。既存の SSH を先に使う場合は、`./install.sh --defer-login` または `.\install.ps1 -DeferLogin` で登録を後回しにできます。既存の登録を維持するには、元のアカウントで更新してください。 登録済みであることを確認して更新するには、`./install.sh --skip-login` または `.\install.ps1 -SkipLogin` を使います。
3. 開発用コンピューターで OpenSSH を有効にします。macOS では **システム設定 → 一般 → 共有 → リモートログイン** を開きます。Linux と Windows では OpenSSH Server を起動します。

## NimoteCode から接続する

- **既存の SSH または個人用 Tailscale。** コンピューターの SSH アドレスまたは Tailscale アドレスと、SSH ポートを NimoteCode に入力します。
- **Nimote のインターネット経由のアクセス。** OpenSSH がローカル TCP ポート 22 で待ち受けている必要があります。NimoteConn の「接続」でコンピューターを登録するか、`nimoteconn login` を実行し、NimoteCode でコードを承認します。その後、デスクトップアプリまたは CLI でリモートアクセスを有効にします。Nimote に登録済みと表示されたら、スマートフォンでコンピューターを選び、Host セッションを開いて接続を確認します。

初回接続では SSH ホスト鍵のフィンガープリントを確認してください。

## 状態の確認とアクセスの管理

macOS と Linux では、`~/.local/bin/nimoteconn doctor` でローカル診断、`~/.local/bin/nimoteconn remote-access status` でインターネット経由のアクセス状態を確認できます。Windows では、PowerShell から `& "$env:LOCALAPPDATA\NimoteConnect\nimoteconn.exe" remote-access status` を実行します。同じ CLI の `remote-access enable` または `remote-access disable` で設定を切り替えられます。
