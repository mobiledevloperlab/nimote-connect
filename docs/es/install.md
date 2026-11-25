# Instalación y conexión

[English](../en/install.md) · [简体中文](../zh/install.md) · **Español** · [日本語](../ja/install.md) · [한국어](../ko/install.md)

[Descripción del producto](README.md) · [Descargar instaladores](https://github.com/mobiledevloperlab/nimote-connect/releases)

Elige el paquete de tu sistema y arquitectura. Antes de extraerlo, compara su SHA-256 con el archivo de verificación correspondiente.

## Instalar y vincular

1. Extrae el paquete en el equipo de desarrollo. Con tu cuenta habitual, ejecuta `./install.sh` en macOS o Linux, o `.\install.ps1` en PowerShell en Windows. Se instalarán Connect y Host.
2. Con el paquete de escritorio, ejecuta `~/.local/bin/nimoteconn gui --connect` tras instalar y elige un método de conexión. Los paquetes CLI solicitan un código de dispositivo durante la primera instalación. Si quieres usar tu conexión SSH y vincular el equipo más tarde, ejecuta `./install.sh --defer-login` o `.\install.ps1 -DeferLogin`. Actualiza con la cuenta original para conservar la vinculación. Para exigir una vinculación existente, usa `./install.sh --skip-login` o `.\install.ps1 -SkipLogin`.
3. Activa OpenSSH en el equipo. En macOS, abre **Ajustes del Sistema → General → Compartir → Sesión remota**. En Linux y Windows, inicia OpenSSH Server.

## Conectarte desde NimoteCode

- **SSH existente o Tailscale personal.** Introduce la dirección SSH o Tailscale del equipo y el puerto SSH en NimoteCode.
- **Acceso por internet de Nimote.** OpenSSH debe escuchar en el puerto TCP 22 local. Vincula el equipo desde el panel **Conexión** de NimoteConn o ejecuta `nimoteconn login` y aprueba el código en NimoteCode. Activa el acceso remoto desde NimoteConn o la CLI. Cuando el equipo aparezca como registrado en Nimote, selecciónalo en el teléfono y abre una sesión de Host para verificar la conexión.

Comprueba la huella del servidor SSH al conectarte por primera vez.

## Consultar y gestionar el acceso

En macOS y Linux, usa `~/.local/bin/nimoteconn doctor` para consultar el diagnóstico local y `~/.local/bin/nimoteconn remote-access status` para ver el estado del acceso por internet. En Windows, ejecuta `& "$env:LOCALAPPDATA\NimoteConnect\nimoteconn.exe" remote-access status` en PowerShell. Usa `remote-access enable` o `remote-access disable` en la misma CLI para cambiar el ajuste.
