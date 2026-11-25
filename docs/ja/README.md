# Nimote Connect

[English](../../README.md) · [简体中文](../zh/README.md) · [Español](../es/README.md) · **日本語** · [한국어](../ko/README.md)

**スマートフォンから開発用コンピューターに接続し、ターミナルや AI コーディングの作業を再開できます。**

Nimote Connect は、NimoteCode と連携する商用サービスです。開発用コンピューターに Connect と Host をインストールすると、対応するクライアントからワークスペースを開き、変更の確認、操作の承認、作業の再開ができます。プロジェクトファイルと作業ツリーは開発用コンピューターに保存され、エージェントもそこで動作します。

[ダウンロードとリリースノート](https://github.com/mobiledevloperlab/nimote-connect/releases) · [インストールと接続](install.md)

## 主な機能

| 利用シーン | Nimote Connect でできること |
| --- | --- |
| 外出先で作業を再開する | リモートターミナルを開き、セッション履歴、Git の差分、チェックの結果、承認待ちの操作を確認できます。開発用コンピューターにインストールして設定した Codex、Claude Code（ACP 経由）、OpenCode を Host から利用できます。 |
| インターネット経由で接続する | デバイスコードでコンピューターを登録します。インターネット経由のアクセスは初期状態でオフです。有効にすると、可能な場合は端末間で直接接続し、直接接続できない場合は DERP リレーを利用できます。OpenSSH によるアカウント認証とホスト鍵の確認も行えます。 |
| 既存の SSH 環境を使う | 現在の SSH 接続をそのまま利用できます。個人用 Tailscale ネットワークを利用している場合は、コンピューターの Tailscale アドレスと SSH ポートを NimoteCode に入力します。 |
| GitHub Issue の変更をレビューに回す | コンピューター上で認証済みの GitHub CLI（`gh`）を使い、Issue をローカルのエージェントに割り当てます。独立した Git worktree で作業し、指定したチェックを実行できます。チェックに失敗しても作業環境を保持して再開できます。チェック通過後は、手動でドラフト PR を作成するか、タスクごとに自動作成を有効にできます。 |
| NimoteHost Community から移行する | macOS または Linux で元のインストールに使ったアカウントから実行すると、標準の SSH 接続先、Host のデータ、履歴を引き継げます。実行中のタスクがある場合、インストーラーはアップグレードを保留します。 |

## ダウンロード

お使いの OS とアーキテクチャに合うパッケージを選び、対応する `.sha256` ファイルで確認してください。配布ファイル、対応クライアント、検証済みの範囲は、各バージョンのリリースノートに記載されます。 [GitHub Releases](https://github.com/mobiledevloperlab/nimote-connect/releases)

| OS | アーキテクチャ | パッケージ |
| --- | --- | --- |
| macOS | Apple シリコン `arm64`、Intel `amd64` | CLI 版とデスクトップ版の `.tar.gz` |
| Linux | `amd64`、`arm64` | CLI 版 `.tar.gz`。systemd のユーザーセッションが必要 |
| Windows | `amd64`（x64）、`arm64` | CLI 版 `.zip`。PowerShell でインストールし、ログイン中のユーザーのバックグラウンドタスクとして実行 |

macOS ではインストール、更新、ロールバックをローカルで確認済みです。Intel 版は Rosetta で確認しました。Linux と Windows の CLI 版はクロスビルド済みです。各 OS のネイティブ環境での検証と、正式クライアントでの一連の接続検証は今後の予定です。

## クローズドソースでの配布

**Nimote Connect の独自実装はクローズドソースです。** このリポジトリでは公開ドキュメントを提供し、承認済みのインストーラーを GitHub Releases で配布します。GitHub が自動生成する `Source code (zip)` と `Source code (tar.gz)` は、このリポジトリのスナップショットです。インストーラーはリリースの添付ファイルから取得してください。

商用パッケージは NimoteHost Community の公開コアを使用し、該当コンポーネントの第三者ライセンス情報を同梱します。 [NimoteHost Community](https://github.com/mobiledevloperlab/nimotehost) · [リリース管理ガイド（簡体字中国語）](../release/README.md)
