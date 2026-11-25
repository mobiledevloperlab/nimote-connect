# Instalación y conexión

[English](../en/install.md) · [简体中文](../zh/install.md) · **Español** · [日本語](../ja/install.md) · [한국어](../ko/install.md)

[Descripción del producto](README.md) · [Descargar instaladores](https://github.com/mobiledevloperlab/nimote-connect/releases)

Elige el paquete de tu sistema y arquitectura. Antes de extraerlo, compara su SHA-256 con el archivo de verificación correspondiente.

## Instalar y vincular

1. Extrae el paquete en el equipo de desarrollo. Con tu cuenta habitual, ejecuta `./install.sh` en macOS o Linux, o `.\install.ps1` en PowerShell en Windows. Se instalarán Connect y Host.
2. En la primera instalación, aprueba el código de dispositivo en un cliente compatible cuando el instalador lo solicite. Para actualizar, usa la cuenta original. Si el equipo ya está vinculado, puedes ejecutar `./install.sh --skip-login` o `.\install.ps1 -SkipLogin`.
3. Activa OpenSSH en el equipo. En macOS, abre **Ajustes del Sistema → General → Compartir → Sesión remota**. En Linux y Windows, inicia OpenSSH Server.

## Conectarte desde NimoteCode

- **SSH existente o Tailscale personal.** Introduce la dirección SSH o Tailscale del equipo y el puerto SSH en NimoteCode.
- **Acceso por internet de Nimote.** OpenSSH debe escuchar en el puerto TCP 22 local. Activa el acceso remoto en el panel **Connect** de NimoteConn o mediante la CLI. Cuando el equipo aparezca en línea, selecciónalo en un cliente NimoteCode compatible.

Comprueba la huella del servidor SSH al conectarte por primera vez.

## Consultar y gestionar el acceso

En macOS y Linux, usa `nimoteconnect doctor` para consultar el diagnóstico local y `nimoteconnect remote-access status` para ver el estado del acceso por internet. En Windows, ejecuta `& "$env:LOCALAPPDATA\NimoteConnect\nimote-connect.exe" remote-access status` en PowerShell. Usa `remote-access enable` o `remote-access disable` en la misma CLI para cambiar el ajuste.
