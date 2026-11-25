# 설치 및 연결

[English](../en/install.md) · [简体中文](../zh/install.md) · [Español](../es/install.md) · [日本語](../ja/install.md) · **한국어**

[제품 소개](README.md) · [설치 패키지 다운로드](https://github.com/mobiledevloperlab/nimote-connect/releases)

운영체제와 아키텍처에 맞는 패키지를 선택하세요. 압축을 풀기 전에 패키지의 SHA-256 값과 해당 체크섬 파일을 비교하세요.

## 설치 및 기기 등록

1. 개발 컴퓨터에서 패키지의 압축을 풉니다. 평소 쓰는 계정으로 macOS 또는 Linux에서는 `./install.sh`를, Windows에서는 PowerShell에서 `.\install.ps1`을 실행합니다. Connect와 Host가 설치됩니다.
2. 데스크톱 패키지를 설치한 후 `~/.local/bin/nimoteconn gui --connect`를 실행해 연결 방식을 선택하세요. CLI 패키지는 처음 설치할 때 기본적으로 기기 코드를 표시합니다. 기존 SSH를 먼저 사용하려면 `./install.sh --defer-login` 또는 `.\install.ps1 -DeferLogin`으로 기기 연결을 미룰 수 있습니다. 기존 기기 연결을 유지하려면 처음 설치한 계정으로 업그레이드하세요. 기존 기기 연결이 있는 경우에만 설치하려면 `./install.sh --skip-login` 또는 `.\install.ps1 -SkipLogin`을 사용하세요.
3. 개발 컴퓨터에서 OpenSSH를 활성화합니다. macOS에서는 **시스템 설정 → 일반 → 공유 → 원격 로그인**을 엽니다. Linux와 Windows에서는 OpenSSH Server를 시작합니다.

## NimoteCode에서 연결하기

- **기존 SSH 또는 개인 Tailscale.** 컴퓨터의 SSH 주소 또는 Tailscale 주소와 SSH 포트를 NimoteCode에 입력합니다.
- **Nimote 인터넷 접속.** OpenSSH가 로컬 TCP 포트 22에서 대기 중이어야 합니다. NimoteConn의 연결 페이지에서 기기를 연결하거나 `nimoteconn login`을 실행한 뒤 NimoteCode에서 코드를 승인하세요. 데스크톱 앱이나 CLI에서 인터넷 접속을 활성화합니다. Nimote에 등록되면 휴대폰에서 해당 컴퓨터를 선택하고 Host 세션을 열어 연결을 확인하세요.

처음 연결할 때는 SSH 호스트 키의 지문을 확인하세요.

## 접속 상태 확인 및 관리

macOS 또는 Linux에서 `~/.local/bin/nimoteconn doctor`로 로컬 진단을 하고, `~/.local/bin/nimoteconn remote-access status`로 인터넷 접속 상태를 확인할 수 있습니다. Windows에서는 PowerShell에서 `& "$env:LOCALAPPDATA\NimoteConnect\nimoteconn.exe" remote-access status`를 실행하세요. 같은 CLI에서 `remote-access enable` 또는 `remote-access disable`로 설정을 변경할 수 있습니다.
