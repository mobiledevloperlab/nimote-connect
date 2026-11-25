# 설치 및 연결

[English](../en/install.md) · [简体中文](../zh/install.md) · [Español](../es/install.md) · [日本語](../ja/install.md) · **한국어**

[제품 소개](README.md) · [설치 패키지 다운로드](https://github.com/mobiledevloperlab/nimote-connect/releases)

운영체제와 아키텍처에 맞는 패키지를 선택하세요. 압축을 풀기 전에 패키지의 SHA-256 값과 해당 체크섬 파일을 비교하세요.

## 설치 및 기기 등록

1. 개발 컴퓨터에서 패키지의 압축을 풉니다. 평소 쓰는 계정으로 macOS 또는 Linux에서는 `./install.sh`를, Windows에서는 PowerShell에서 `.\install.ps1`을 실행합니다. Connect와 Host가 설치됩니다.
2. 처음 설치할 때는 안내에 따라 호환 클라이언트에서 기기 코드를 승인합니다. 업그레이드에는 기존 계정을 사용하세요. 이미 등록한 컴퓨터에서는 `./install.sh --skip-login` 또는 `.\install.ps1 -SkipLogin`을 사용할 수 있습니다.
3. 개발 컴퓨터에서 OpenSSH를 활성화합니다. macOS에서는 **시스템 설정 → 일반 → 공유 → 원격 로그인**을 엽니다. Linux와 Windows에서는 OpenSSH Server를 시작합니다.

## NimoteCode에서 연결하기

- **기존 SSH 또는 개인 Tailscale.** 컴퓨터의 SSH 주소 또는 Tailscale 주소와 SSH 포트를 NimoteCode에 입력합니다.
- **Nimote 인터넷 접속.** OpenSSH가 로컬 TCP 포트 22에서 대기 중이어야 합니다. NimoteConn의 **Connect** 패널이나 CLI에서 원격 접속을 활성화합니다. 컴퓨터가 온라인으로 표시되면 호환되는 NimoteCode 클라이언트에서 선택합니다.

처음 연결할 때는 SSH 호스트 키의 지문을 확인하세요.

## 접속 상태 확인 및 관리

macOS 또는 Linux에서 `nimoteconnect doctor`로 로컬 진단을 하고, `nimoteconnect remote-access status`로 인터넷 접속 상태를 확인할 수 있습니다. Windows에서는 PowerShell에서 `& "$env:LOCALAPPDATA\NimoteConnect\nimote-connect.exe" remote-access status`를 실행하세요. 같은 CLI에서 `remote-access enable` 또는 `remote-access disable`로 설정을 변경할 수 있습니다.
