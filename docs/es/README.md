# Nimote Connect

[English](../../README.md) · [简体中文](../zh/README.md) · **Español** · [日本語](../ja/README.md) · [한국어](../ko/README.md)

**Conéctate desde el móvil a tu equipo de desarrollo y continúa con el terminal y tus sesiones de programación con IA.**

Nimote Connect es el servicio comercial que complementa a NimoteCode. Instala Connect y Host en tu equipo para abrir el espacio de trabajo desde un cliente compatible, revisar cambios, gestionar aprobaciones y retomar tareas. Los archivos del proyecto, los árboles de trabajo y los agentes permanecen en tu equipo.

[Descargas y notas de versión](https://github.com/mobiledevloperlab/nimote-connect/releases) · [Instalación y conexión](install.md)

## Qué puedes hacer

| Caso de uso | Cómo te ayuda Nimote Connect |
| --- | --- |
| Retomar el trabajo desde el móvil | Abre un terminal remoto y consulta el historial, las diferencias de Git, los resultados de las comprobaciones y las aprobaciones pendientes. Host admite Codex, Claude Code mediante ACP y OpenCode si están instalados y configurados en el equipo. |
| Conectarte por internet | Vincula el equipo con un código de dispositivo. El acceso por internet está desactivado de forma predeterminada. Al activarlo, usa una conexión directa entre pares cuando es posible y puede recurrir a un relé DERP. OpenSSH autentica la cuenta y permite verificar la huella del servidor. |
| Aprovechar tu configuración SSH | Usa tu conexión SSH habitual. Si tienes una red personal de Tailscale, introduce la dirección Tailscale del equipo y el puerto SSH en NimoteCode. |
| Preparar una revisión a partir de una incidencia de GitHub | Usa GitHub CLI (`gh`), con autorización en el equipo, para asignar la incidencia a un agente local. El agente trabaja en un árbol de trabajo de Git independiente y ejecuta las comprobaciones que indiques. Si fallan, puedes retomar el trabajo en el mismo espacio. Tras superar las comprobaciones, puedes crear un borrador de PR manualmente o habilitar su creación automática para esa tarea. |
| Actualizar desde NimoteHost Community | En macOS o Linux, ejecuta el instalador con la cuenta original para conservar el acceso SSH habitual, los datos de Host y el historial. El instalador aplaza la actualización mientras haya tareas activas. |

## Descargas

Selecciona el paquete de tu sistema y arquitectura y verifícalo con el archivo `.sha256` correspondiente. Las notas de cada versión indican los paquetes disponibles, los clientes compatibles y las validaciones realizadas. [GitHub Releases](https://github.com/mobiledevloperlab/nimote-connect/releases)

| Plataforma | Arquitecturas | Paquete |
| --- | --- | --- |
| macOS | Apple silicon `arm64`, Intel `amd64` | `.tar.gz` en ediciones CLI y escritorio |
| Linux | `amd64`, `arm64` | `.tar.gz` de línea de comandos, requiere una sesión de usuario de systemd |
| Windows | `amd64` (x64), `arm64` | `.zip` de línea de comandos con instalador PowerShell y tareas en segundo plano por usuario |

La instalación, la actualización y la vuelta a la versión anterior se probaron localmente en macOS. El paquete Intel se probó mediante Rosetta. Los paquetes de Linux y Windows se compilaron de forma cruzada. Quedan pendientes las pruebas nativas y la validación del flujo completo de conexión con el cliente oficial.

## Distribución de código cerrado

**La implementación propietaria de Nimote Connect es de código cerrado.** Este repositorio contiene documentación pública y distribuye instaladores aprobados mediante GitHub Releases. Los archivos automáticos `Source code (zip)` y `Source code (tar.gz)` son copias del contenido del repositorio. Descarga el instalador para tu plataforma entre los archivos adjuntos de la versión.

El paquete comercial usa el núcleo público de NimoteHost Community e incluye los avisos de terceros correspondientes. [NimoteHost Community](https://github.com/mobiledevloperlab/nimotehost) · [Guía de publicación (简体中文)](../release/README.md)
