# Nimote Connect

[English](../../README.md) · [简体中文](../zh/README.md) · [Español](../es/README.md) · [日本語](../ja/README.md) · **한국어**

**휴대전화에서 개발 컴퓨터에 연결해 터미널과 AI 코딩 작업을 이어가세요.**

Nimote Connect는 NimoteCode와 함께 사용하는 상용 서비스입니다. 개발 컴퓨터에 Connect와 Host를 설치하면 호환 클라이언트에서 작업 공간을 열고, 변경 사항과 승인 요청을 검토하고, 진행하던 작업을 이어갈 수 있습니다. 프로젝트 파일과 작업 트리는 개발 컴퓨터에 저장되며, 에이전트도 같은 컴퓨터에서 실행됩니다.

[다운로드 및 릴리스 노트](https://github.com/mobiledevloperlab/nimote-connect/releases) · [설치 및 연결](install.md)

## 주요 기능

| 사용 상황 | Nimote Connect로 할 수 있는 일 |
| --- | --- |
| 휴대전화에서 작업 재개 | 원격 터미널을 열고 세션 기록, Git 변경 사항, 검사 결과 및 대기 중인 승인 요청을 확인할 수 있습니다. 컴퓨터에 설치 및 구성한 Codex, Claude Code(ACP 경유), OpenCode를 Host에서 사용할 수 있습니다. |
| 인터넷을 통해 연결 | 기기 코드로 컴퓨터를 등록합니다. 인터넷 접속은 기본적으로 꺼져 있습니다. 켜면 가능한 경우 기기 간에 직접 연결하며, 직접 연결할 수 없을 때는 DERP 릴레이를 이용할 수 있습니다. OpenSSH에서 계정을 인증하고 호스트 키 지문을 확인할 수 있습니다. |
| 기존 SSH 환경 사용 | 현재 SSH 연결을 계속 사용할 수 있습니다. 개인 Tailscale 네트워크를 사용한다면 컴퓨터의 Tailscale 주소와 SSH 포트를 NimoteCode에 입력하세요. |
| GitHub 이슈를 검토 가능한 변경으로 전환 | 컴퓨터에 인증된 GitHub CLI(`gh`)로 이슈를 로컬 에이전트에게 할당합니다. 독립된 Git worktree에서 작업하고 지정한 검사를 실행할 수 있습니다. 검사에 실패해도 작업 공간을 유지해 이어갈 수 있습니다. 검사를 통과하면 초안 PR을 수동으로 만들거나 해당 작업에 자동 생성을 설정할 수 있습니다. |
| NimoteHost Community에서 업그레이드 | macOS 또는 Linux에서 기존 설치에 사용한 계정으로 설치 프로그램을 실행하면 표준 SSH 연결, Host 데이터 및 기록을 유지할 수 있습니다. 진행 중인 작업이 있으면 설치 프로그램이 업그레이드를 보류합니다. |

## 다운로드

운영체제와 아키텍처에 맞는 패키지를 고르고, 해당 `.sha256` 파일을 사용해 검증하세요. 제공되는 패키지, 호환 클라이언트 및 검증 범위는 각 버전의 릴리스 노트에서 확인할 수 있습니다. [GitHub Releases](https://github.com/mobiledevloperlab/nimote-connect/releases)

| 운영체제 | 아키텍처 | 패키지 |
| --- | --- | --- |
| macOS | Apple Silicon `arm64`, Intel `amd64` | NimoteConn 데스크톱 앱이 포함된 `.tar.gz` |
| Linux | `amd64`, `arm64` | CLI `.tar.gz`. systemd 사용자 세션 필요 |
| Windows | `amd64`(x64), `arm64` | CLI `.zip`. PowerShell로 설치하며 로그인한 계정의 백그라운드 작업으로 실행 |

macOS에서 로컬 설치, 업그레이드, 롤백을 검증했으며 Intel 빌드는 Rosetta에서 검증했습니다. Linux와 Windows의 CLI 패키지는 교차 컴파일했습니다. 각 운영체제의 네이티브 환경 검증과 공식 클라이언트에서의 전체 연결 과정 검증은 아직 남아 있습니다.

## 비공개 소스 배포

**Nimote Connect의 독점 구현 소스는 비공개입니다.** 이 저장소는 공개 문서를 제공하며 승인된 설치 패키지를 GitHub Releases에서 배포합니다. GitHub가 자동으로 생성하는 `Source code (zip)`와 `Source code (tar.gz)`는 이 저장소의 스냅샷입니다. 설치 패키지는 릴리스 첨부 파일에서 다운로드하세요.

상용 패키지는 NimoteHost Community의 공개 코어를 사용하며 해당 구성 요소의 제3자 라이선스 고지를 포함합니다. [NimoteHost Community](https://github.com/mobiledevloperlab/nimotehost) · [릴리스 관리 가이드(중국어 간체)](../release/README.md)
