## 1. Introducción

En la mayoría de los casos, los servidores y máquinas que necesitamos gestionar no comparten el mismo espacio físico. Pueden estar ubicados en:

- Diferentes departamentos de una empresa.
- Centros de Proceso de Datos (CPD) generales.
- Infraestructura en la nube.

Para acceder a ellos de forma remota existen servicios, métodos y herramientas que se agrupan en dos grandes categorías: **acceso por terminal de texto** y **acceso por escritorio gráfico**.

---

## 2. Terminales en modo texto

Una de las formas de administrar un sistema de forma remota es usar un servidor que permita el acceso como terminal de texto. El usuario se conecta al equipo a través de la red con nombre de usuario y contraseña, como si estuviera delante de él. Los principales protocolos son:

| Protocolo | Puerto | Cifrado | Estado |
|-----------|--------|---------|--------|
| **Telnet** | 23 | No — la información viaja en claro | Obsoleto |
| **Rlogin** | 513 | No — usa mecanismo Rhosts | Obsoleto |
| **SSH** | 22 | Sí — cifrado fuerte | Estándar actual |

!!! warning "Atención"
    Telnet y Rlogin envían contraseñas en texto plano por la red. No deben usarse en entornos de producción. **SSH es el único estándar seguro** para acceso remoto por terminal.

---

## 3. SSH (Secure Shell)

**SSH (Secure Shell)** es un protocolo de red que permite acceder a otro equipo a través de una red para ejecutar comandos, controlarlo de manera remota e intercambiar archivos de forma segura. Ofrece autenticación fuerte y comunicaciones cifradas.

### 3.1 Instalación

**Servidor SSH** (en la máquina a la que nos conectaremos):

```bash
sudo apt install openssh-server
sudo systemctl enable --now ssh
sudo systemctl status ssh
```

**Cliente SSH** (normalmente ya instalado en Linux):

```bash
sudo apt install openssh-client
```

### 3.2 Conexión básica

```bash
ssh usuario@ip_o_hostname
```

Ejemplos:

```bash
# Conectar con usuario "alumno" a la IP 192.168.1.10
ssh alumno@192.168.1.10

# Conectar especificando puerto distinto al 22
ssh -p 2222 alumno@192.168.1.10

# Ejecutar un comando remoto directamente sin abrir sesión interactiva
ssh alumno@192.168.1.10 'df -h'
```

En la primera conexión, SSH muestra la huella digital (*fingerprint*) del servidor y pide confirmación para añadirlo a `~/.ssh/known_hosts`.

### 3.3 Autenticación basada en claves

La autenticación por clave pública es más segura que la contraseña y permite la automatización de tareas. Funciona con un par de claves:

- **Clave privada**: permanece en el cliente (`~/.ssh/id_rsa` o `~/.ssh/id_ed25519`).
- **Clave pública**: se copia al servidor (`~/.ssh/authorized_keys`).

#### Paso 1 — Generar el par de claves en el cliente

```bash
ssh-keygen -t ed25519 -C "comentario_identificativo"
```

| Opción | Descripción |
|--------|-------------|
| `-t ed25519` | Algoritmo de cifrado (más moderno y seguro que RSA) |
| `-t rsa -b 4096` | Alternativa RSA de 4096 bits |
| `-C` | Comentario para identificar la clave |

El comando crea dos ficheros en `~/.ssh/`:

```
~/.ssh/id_ed25519       ← clave privada (NUNCA compartir)
~/.ssh/id_ed25519.pub   ← clave pública (se copia al servidor)
```

#### Paso 2 — Copiar la clave pública al servidor

```bash
ssh-copy-id usuario@ip_servidor
```

Esto añade la clave pública al fichero `~/.ssh/authorized_keys` del servidor. A partir de ahora la conexión no pedirá contraseña.

#### Verificación

```bash
ssh usuario@ip_servidor   # debe conectar sin pedir contraseña
```

### 3.4 Configuración del servidor SSH

El fichero de configuración principal del servidor es `/etc/ssh/sshd_config`. Tras modificarlo, hay que reiniciar el servicio:

```bash
sudo nano /etc/ssh/sshd_config
sudo systemctl restart ssh
```

Parámetros más importantes:

| Parámetro | Valor por defecto | Descripción |
|-----------|-------------------|-------------|
| `Port` | `22` | Puerto de escucha |
| `PermitRootLogin` | `prohibit-password` | Acceso directo de root (`no` para máxima seguridad) |
| `PasswordAuthentication` | `yes` | Permite autenticación por contraseña |
| `MaxAuthTries` | `6` | Intentos máximos de autenticación por conexión |
| `AllowUsers` | (no definido) | Lista blanca de usuarios que pueden conectarse |
| `ClientAliveInterval` | `0` | Segundos entre keepalives al cliente |

Ejemplo de configuración reforzada:

```
Port 22
PermitRootLogin no
PasswordAuthentication no
MaxAuthTries 3
AllowUsers alumno admin
ClientAliveInterval 300
```

!!! warning "Atención"
    Antes de deshabilitar `PasswordAuthentication`, asegúrate de que la autenticación por clave funciona correctamente. De lo contrario perderás el acceso al servidor.

---

## 4. Transferencia segura de ficheros

### 4.1 SCP (Secure Copy)

`scp` copia ficheros entre equipos usando el protocolo SSH. Su sintaxis es similar a `cp`.

```bash
# Copiar fichero local al servidor remoto
scp fichero.txt usuario@192.168.1.10:/ruta/destino/

# Copiar directorio completo al servidor
scp -r directorio/ usuario@192.168.1.10:/ruta/destino/

# Descargar fichero del servidor al equipo local
scp usuario@192.168.1.10:/ruta/fichero.txt ./

# Especificar puerto
scp -P 2222 fichero.txt usuario@192.168.1.10:/tmp/
```

### 4.2 SFTP (SSH File Transfer Protocol)

`sftp` abre una sesión interactiva de transferencia de ficheros sobre SSH, similar a un cliente FTP pero cifrado.

!!! note "Cheat Sheet"
    [:material-file-pdf-box: SFTP Commands Cheat Sheet](../assets/sftp-cheatsheet.pdf) — resumen de todos los comandos SFTP en una página.

```bash
sftp usuario@192.168.1.10
```

Una vez dentro, los comandos se dividen en tres categorías:

#### Listado de ficheros

| Comando | Descripción |
|---------|-------------|
| `ls [opciones] [ruta]` | Lista ficheros en el servidor remoto |
| `lls [opciones] [ruta]` | Lista ficheros en el equipo local |

Opciones de `ls`: `-1` (una columna), `-a` (todos), `-h` (tamaño legible), `-l` (formato largo), `-S` (ordenar por tamaño), `-t` (ordenar por fecha), `-r` (orden inverso).

#### Manipulación de directorios

| Comando | Descripción |
|---------|-------------|
| `pwd` | Muestra el directorio actual en el servidor |
| `lpwd` | Muestra el directorio actual en el equipo local |
| `cd ruta` | Cambia directorio en el servidor |
| `lcd ruta` | Cambia directorio en el equipo local |
| `mkdir ruta` | Crea directorio en el servidor |
| `rmdir ruta` | Elimina directorio vacío en el servidor |

!!! note "Nota"
    Las rutas absolutas siempre empiezan por `/` (ej. `/home/usuario/data`). Las rutas relativas parten del directorio actual.

#### Manipulación de ficheros

| Comando | Descripción |
|---------|-------------|
| `get fichero-remoto [dir-local]` | Descarga un fichero del servidor |
| `put fichero-local [dir-remoto]` | Sube un fichero al servidor |
| `rm fichero-remoto` | Elimina un fichero en el servidor |

Se pueden usar comodines (`*`) para transferir múltiples ficheros:

```
sftp> get *.pdf
sftp> put data.xml /users/mike/data/
sftp> rm /users/mike/data/*
```

---

## 5. Escritorio remoto

Se habla de **escritorio remoto** cuando un usuario se conecta a un equipo desde otro utilizando la red y accede a su entorno gráfico. Se utiliza habitualmente para administración remota de sistemas con entorno de escritorio.

Para cualquier solución de escritorio remoto existen dos partes:

- **Servidor**: se instala en el equipo a controlar remotamente.
- **Cliente**: se instala en el equipo desde el que se quiere acceder.

Los protocolos más habituales en Linux son:

| Protocolo | Descripción |
|-----------|-------------|
| **RDP** (Remote Desktop Protocol) | Protocolo de Microsoft. En Linux se implementa con **xRDP**. Permite conectar desde un cliente Windows con la herramienta nativa "Conexión a Escritorio Remoto". |
| **VNC** (Virtual Network Computer) | Multiplataforma. Comparte el escritorio del servidor. El cliente puede ver y controlar la sesión gráfica del usuario remoto. |

### 5.1 xRDP — Escritorio remoto con RDP en Linux

**xRDP** es un servidor RDP de código abierto para Linux que permite recibir conexiones desde clientes RDP (Windows, Linux, macOS).

#### Instalación en Ubuntu Server / Desktop

```bash
sudo apt update
sudo apt install xrdp
sudo systemctl enable --now xrdp
sudo systemctl status xrdp
```

#### Permitir el puerto en el firewall

```bash
sudo ufw allow 3389/tcp
sudo ufw reload
```

#### Conexión desde un cliente

**Desde Windows**: Inicio → "Conexión a Escritorio Remoto" → introducir la IP del servidor Linux.

**Desde Linux** (con cliente `rdesktop` o `freerdp`):

```bash
# Con rdesktop
sudo apt install rdesktop
rdesktop 192.168.1.10

# Con FreeRDP
sudo apt install freerdp2-x11
xfreerdp /u:usuario /p:contraseña /v:192.168.1.10
```

### 5.2 VNC — Virtual Network Computing

VNC comparte el escritorio gráfico del servidor. Hay múltiples implementaciones; una de las más usadas en Ubuntu es **TigerVNC**.

#### Instalación del servidor VNC

```bash
sudo apt update
sudo apt install tigervnc-standalone-server
```

#### Configurar contraseña VNC

```bash
vncpasswd
```

#### Iniciar el servidor VNC

```bash
vncserver :1 -geometry 1280x720 -depth 24
```

Esto arranca una sesión VNC en el display `:1` (puerto **5901**).

#### Detener el servidor VNC

```bash
vncserver -kill :1
```

#### Conexión desde un cliente

**Desde Linux** (con `tigervnc-viewer` o `vinagre`):

```bash
sudo apt install tigervnc-viewer
vncviewer 192.168.1.10:1
```

**Desde Windows**: descargar TigerVNC Viewer o RealVNC Viewer e introducir `192.168.1.10:5901`.

### 5.3 Comparativa RDP vs VNC

| Característica | xRDP | VNC |
|----------------|------|-----|
| Protocolo base | RDP (Microsoft) | RFB |
| Puerto por defecto | 3389 | 5900+display |
| Cifrado nativo | Sí (TLS) | Básico (depende del cliente) |
| Compresión | Alta | Media |
| Cliente nativo en Windows | Sí | No (requiere instalar) |
| Multiplataforma | Sí (con xRDP) | Sí |
| Rendimiento | Alto | Medio |

---

## 6. Actividades

!!! example "Tarea"

    **Práctica 1. SSH — Red Hat Academy**

    ![Red Hat Academy](../assets/img/rha-logo.png){ width=300 }

    Para esta práctica trabajarás con el material del **Capítulo 10 — Configuración y seguridad de SSH** de *Red Hat Academy: Administración de Sistemas en Red Hat I (RH124) 9.0*.

    Accede al portal de [Red Hat Academy](https://www.redhat.com/es/services/training/red-hat-academy) e inicia el entorno de laboratorio. Completa las siguientes secciones del capítulo:

    | Sección | Tipo | Duración |
    |---------|------|----------|
    | Introducción | Lectura | 3 min |
    | Acceso a la línea de comandos remota con SSH | Lectura + Ejercicio guiado | 30 min |
    | Configurar autenticación basada en claves de SSH | Lectura + Ejercicio guiado | 30 min |
    | Personalización de la configuración del servicio SSH | Lectura + Ejercicio guiado | 30 min |
    | Configuración y seguridad de SSH | Laboratorio | 15 min |
    | Conclusión | Lectura | 2 min |

    **Duración total estimada: 110 minutos.**

    !!! note "Nota"
        No olvides iniciar el entorno de laboratorio antes de comenzar los ejercicios guiados.

!!! example "Tarea"

    **Práctica 2. Transferencia segura de archivos — Red Hat Academy**

    ![Red Hat Academy](../assets/img/rha-logo.png){ width=300 }

    Para esta práctica trabajarás con el material del **Capítulo 4 — Almacenamiento y transferencia de archivos de forma segura entre sistemas** de *Red Hat Academy: Administración de sistemas en Red Hat II (RH134) 9.3*.

    Accede al portal de [Red Hat Academy](https://www.redhat.com/es/services/training/red-hat-academy) e inicia el entorno de laboratorio. Completa las siguientes secciones del capítulo:

    | Sección | Tipo |
    |---------|------|
    | Gestión de archivos comprimidos tar | Lectura + Ejercicio guiado |
    | Transferencia de archivos entre sistemas de forma segura (SCP, SFTP) | Lectura + Ejercicio guiado |
    | Sincronización de archivos entre sistemas de forma segura (rsync) | Lectura + Ejercicio guiado |
    | Laboratorio final | Laboratorio |

    !!! note "Nota"
        No olvides iniciar el entorno de laboratorio antes de comenzar los ejercicios guiados.

!!! example "Tarea"

    **Práctica 3. Escritorio remoto con VNC**

    Instala y configura un servidor VNC (TigerVNC) en Linux y accede a él desde un cliente Linux.

    1. Instala `tigervnc-standalone-server` en el servidor.
    2. Configura la contraseña VNC.
    3. Inicia una sesión VNC en el display `:1`.
    4. Instala `tigervnc-viewer` en el cliente y conéctate.
    5. Documenta el proceso con capturas de pantalla.

!!! tip "Reto"

    **Práctica 4 (Avanzado). Comparativa de soluciones de escritorio remoto**

    Realiza una comparativa de las diferentes soluciones de escritorio remoto disponibles para Linux (xRDP, TigerVNC, RealVNC, NoMachine, TeamViewer) indicando:

    - Características principales.
    - Ventajas y desventajas.
    - Casos de uso recomendados.
    - Nivel de seguridad.
