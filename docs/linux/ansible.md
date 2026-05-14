# Ansible: Automatización de Infraestructura

## Programación de Aula

### Resultados de Aprendizaje

Esta unidad cubre principalmente el **Resultado de aprendizaje 3 (RA3)** según el **Real Decreto 1629/2009, de 30 de octubre**, ampliando la automatización de tareas más allá de cron/at hacia la gestión de infraestructura:

1. Gestiona la automatización de tareas del sistema, aplicando criterios de eficiencia y utilizando comandos y herramientas gráficas.

Los criterios de evaluación que se trabajan son:

- Se han descrito las ventajas de la automatización de las tareas repetitivas en el sistema.
- Se han utilizado los comandos del sistema para la planificación de tareas.
- Se han realizado planificaciones de tareas repetitivas o puntuales relacionadas con la administración del sistema.
- Se ha automatizado la administración de cuentas.
- Se han documentado los procesos programados como tareas automáticas.

También contribuye al **RA6** (integración de sistemas libres y propietarios) al gestionar entornos heterogéneos Linux/Windows desde un único punto de control.

### Planificación Temporal (4 sesiones / 8 horas)

| Sesión | Contenido |
| ------ | --------- |
| 1 | Introducción a Ansible. Arquitectura. Instalación. Inventario. Comandos ad-hoc |
| 2 | Playbooks: estructura, tareas y módulos esenciales |
| 3 | Variables, handlers y plantillas |
| 4 | Caso práctico integrador: gestión de usuarios y configuración de servicios |

---

## 1. Introducción

### 1.1 ¿Qué es Ansible?

!!! note "Información"
    **Ansible** es una herramienta de automatización de infraestructura de código abierto desarrollada por Red Hat. Permite gestionar la configuración, el despliegue de aplicaciones y la orquestación de tareas en múltiples servidores simultáneamente, desde un único punto de control.

Ansible forma parte del paradigma de **Infraestructura como Código (IaC, Infrastructure as Code)**, que consiste en gestionar y aprovisionar la infraestructura mediante archivos de configuración legibles, versionables y reutilizables, en lugar de procesos manuales.

### 1.2 ¿Por qué Ansible frente a scripts?

Hasta ahora hemos visto cómo automatizar tareas con scripts Bash y cron. Ansible no los reemplaza, sino que los complementa para un nivel superior de automatización:

| Característica | Scripts Bash + cron | Ansible |
| -------------- | ------------------- | ------- |
| Ejecución en múltiples servidores | Requiere bucles y SSH manual | Nativo, en paralelo |
| Idempotencia | Hay que programarla explícitamente | Incorporada en los módulos |
| Legibilidad | Depende del programador | YAML declarativo y autodocumentado |
| Gestión de errores | Manual | Gestionada automáticamente |
| Sistemas heterogéneos (Linux + Windows) | Complejo | Soporte nativo |
| Curva de aprendizaje | Baja (si sabes bash) | Baja (YAML sin agente) |

!!! note "Información"
    **Idempotencia**: Una operación es idempotente cuando ejecutarla varias veces produce el mismo resultado que ejecutarla una sola vez. Por ejemplo, el módulo `user` de Ansible crea el usuario si no existe, pero no hace nada si ya existe. Un script sin idempotencia podría dar error al intentar crear un usuario que ya existe.

### 1.3 Casos de uso habituales en administración de sistemas

- Aprovisionar nuevos servidores con la configuración base (usuarios, paquetes, seguridad).
- Desplegar y actualizar configuraciones en toda la infraestructura de forma simultánea.
- Crear y gestionar usuarios en masa desde un fichero CSV.
- Instalar, configurar y arrancar servicios (Apache, SSH, NTP, etc.).
- Programar tareas cron en múltiples equipos.
- Gestionar entornos mixtos Linux/Windows.

---

## 2. Arquitectura de Ansible

Ansible sigue una arquitectura **agentless** (sin agente): no es necesario instalar ningún software en los equipos gestionados. La comunicación se realiza a través de **SSH** en Linux/Unix y **WinRM** en Windows.

Los componentes principales son:

```
┌─────────────────────────────────────────────┐
│             CONTROL NODE                    │
│  (equipo donde se instala Ansible)          │
│                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  │
│  │Inventario│  │Playbooks │  │  Módulos │  │
│  └──────────┘  └──────────┘  └──────────┘  │
└──────────────────────┬──────────────────────┘
                       │ SSH / WinRM
          ┌────────────┼────────────┐
          │            │            │
   ┌──────▼──┐  ┌──────▼──┐  ┌─────▼───┐
   │ Nodo 1  │  │ Nodo 2  │  │ Nodo 3  │
   │ (Linux) │  │ (Linux) │  │(Windows)│
   └─────────┘  └─────────┘  └─────────┘
        MANAGED NODES
```

| Componente | Descripción |
| ---------- | ----------- |
| **Control Node** | Equipo donde se instala Ansible y desde donde se lanzan las automatizaciones. Debe ser Linux/macOS. |
| **Managed Nodes** | Equipos gestionados. No requieren instalación de Ansible. Solo necesitan Python (Linux) o PowerShell/WinRM (Windows). |
| **Inventario** | Fichero que lista los managed nodes, agrupados según su función. |
| **Playbook** | Fichero YAML que describe las tareas a ejecutar en los managed nodes. |
| **Módulo** | Unidad de trabajo de Ansible (instalar paquete, crear usuario, copiar fichero...). Cada tarea usa un módulo. |
| **Task** | Acción individual dentro de un playbook que invoca un módulo. |
| **Play** | Conjunto de tasks que se aplican a un grupo de hosts. |
| **Role** | Forma de organizar playbooks, variables y ficheros en una estructura reutilizable. |

---

## 3. Instalación

### 3.1 Instalación del Control Node (Ubuntu/Debian)

Ansible solo se instala en el **control node**. Los managed nodes no necesitan ninguna instalación especial.

```bash
# Actualizar repositorios
sudo apt update

# Instalar Ansible
sudo apt install -y ansible

# Verificar la instalación
ansible --version
```

### 3.2 Preparar los Managed Nodes

Los managed nodes Linux necesitan:

1. **Python 3** instalado (en la mayoría de distribuciones ya viene instalado).
2. **Acceso SSH** desde el control node.
3. Preferiblemente, **autenticación por clave SSH** sin contraseña.

**Configurar autenticación SSH por clave desde el control node:**

```bash
# Generar par de claves SSH en el control node (si no existe ya)
ssh-keygen -t ed25519 -C "ansible"

# Copiar la clave pública a cada managed node
ssh-copy-id usuario@192.168.1.10
ssh-copy-id usuario@192.168.1.11

# Verificar que funciona sin contraseña
ssh usuario@192.168.1.10
```

!!! warning "Atención"
    Si el managed node requiere `sudo` para tareas de administración, el usuario debe tener permisos `sudo` sin contraseña, o deberás usar el parámetro `--ask-become-pass` al ejecutar Ansible.

---

## 4. Inventario

El **inventario** es el fichero donde se definen los equipos que Ansible va a gestionar. Por defecto se encuentra en `/etc/ansible/hosts`, aunque es una buena práctica crear un inventario propio por proyecto.

### 4.1 Formato del inventario

```ini
# Inventario en formato INI

# Hosts individuales
192.168.1.10
servidor-web.empresa.local

# Grupos de hosts
[webservers]
192.168.1.10
192.168.1.11

[dbservers]
192.168.1.20
192.168.1.21

[produccion:children]
webservers
dbservers

# Variables por host
[webservers]
192.168.1.10 ansible_user=ubuntu ansible_port=22
192.168.1.11 ansible_user=admin
```

También puede usarse formato **YAML**:

```yaml
# inventory.yml
all:
  children:
    webservers:
      hosts:
        192.168.1.10:
          ansible_user: ubuntu
        192.168.1.11:
          ansible_user: ubuntu
    dbservers:
      hosts:
        192.168.1.20:
          ansible_user: admin
```

### 4.2 Variables de conexión más utilizadas

| Variable | Descripción | Ejemplo |
| -------- | ----------- | ------- |
| `ansible_host` | IP o hostname del nodo | `ansible_host=192.168.1.10` |
| `ansible_user` | Usuario SSH | `ansible_user=ubuntu` |
| `ansible_port` | Puerto SSH | `ansible_port=2222` |
| `ansible_ssh_private_key_file` | Ruta a la clave privada SSH | `ansible_ssh_private_key_file=~/.ssh/id_ed25519` |
| `ansible_become` | Activar escalada de privilegios | `ansible_become=true` |
| `ansible_become_user` | Usuario al que escalar | `ansible_become_user=root` |

### 4.3 Comprobar el inventario

```bash
# Listar todos los hosts del inventario
ansible all --list-hosts -i inventory.ini

# Listar los hosts de un grupo concreto
ansible webservers --list-hosts -i inventory.ini
```

---

## 5. Comandos Ad-hoc

Los **comandos ad-hoc** permiten ejecutar una tarea puntual en los managed nodes sin necesidad de escribir un playbook. Son útiles para tareas rápidas o para comprobar el estado de los sistemas.

```bash
ansible <hosts> -i <inventario> -m <módulo> -a "<argumentos>" [opciones]
```

### 5.1 Módulo ping — Comprobar conectividad

```bash
# Comprobar conectividad con todos los hosts
ansible all -i inventory.ini -m ping

# Comprobar solo un grupo
ansible webservers -i inventory.ini -m ping
```

Salida esperada:
```
192.168.1.10 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

### 5.2 Módulo command — Ejecutar comandos

```bash
# Ver el uptime de todos los servidores
ansible all -i inventory.ini -m command -a "uptime"

# Ver el espacio en disco
ansible all -i inventory.ini -m command -a "df -h"

# Ver los usuarios del sistema
ansible webservers -i inventory.ini -m command -a "cat /etc/passwd"
```

### 5.3 Módulo shell — Ejecutar comandos con shell

A diferencia de `command`, el módulo `shell` permite usar tuberías (`|`), redirecciones y variables de entorno:

```bash
# Usar pipe (no funciona con command)
ansible all -i inventory.ini -m shell -a "df -h | grep /dev/sda"

# Redirigir salida
ansible all -i inventory.ini -m shell -a "ls /etc > /tmp/etc_list.txt"
```

### 5.4 Módulo apt — Gestionar paquetes

```bash
# Instalar un paquete
ansible webservers -i inventory.ini -m apt -a "name=nginx state=present" --become

# Desinstalar un paquete
ansible webservers -i inventory.ini -m apt -a "name=nginx state=absent" --become

# Actualizar todos los paquetes
ansible all -i inventory.ini -m apt -a "upgrade=dist update_cache=yes" --become
```

### 5.5 Módulo service — Gestionar servicios

```bash
# Iniciar un servicio
ansible webservers -i inventory.ini -m service -a "name=nginx state=started" --become

# Reiniciar un servicio
ansible webservers -i inventory.ini -m service -a "name=nginx state=restarted" --become

# Habilitar inicio automático
ansible webservers -i inventory.ini -m service -a "name=nginx enabled=yes" --become
```

!!! note "Información"
    El parámetro `--become` indica a Ansible que ejecute la tarea con privilegios elevados (`sudo`). Es equivalente a poner `become: true` en un playbook.

---

## 6. Playbooks

Un **playbook** es un fichero YAML que describe, de forma declarativa, el estado deseado de los sistemas. Contiene una o más **plays**, y cada play contiene una lista de **tasks**.

### 6.1 Estructura básica de un playbook

```yaml
---
- name: Nombre descriptivo del play
  hosts: webservers          # A qué hosts se aplica
  become: true               # Usar sudo en todas las tasks

  tasks:
    - name: Descripción de la tarea
      nombre_modulo:
        parametro1: valor1
        parametro2: valor2

    - name: Segunda tarea
      otro_modulo:
        parametro: valor
```

### 6.2 Primer playbook: instalar y arrancar Nginx

```yaml
---
- name: Instalar y configurar servidor web Nginx
  hosts: webservers
  become: true

  tasks:
    - name: Actualizar caché de paquetes
      apt:
        update_cache: yes

    - name: Instalar Nginx
      apt:
        name: nginx
        state: present

    - name: Arrancar y habilitar Nginx
      service:
        name: nginx
        state: started
        enabled: yes
```

**Ejecutar el playbook:**

```bash
ansible-playbook -i inventory.ini nginx.yml
```

**Salida:**

```
PLAY [Instalar y configurar servidor web Nginx] ****************************

TASK [Actualizar caché de paquetes] ****************************************
ok: [192.168.1.10]

TASK [Instalar Nginx] ******************************************************
changed: [192.168.1.10]

TASK [Arrancar y habilitar Nginx] ******************************************
changed: [192.168.1.10]

PLAY RECAP *****************************************************************
192.168.1.10  : ok=3  changed=2  unreachable=0  failed=0
```

!!! note "Información"
    En la salida de Ansible, cada tarea puede tener uno de estos estados:

    - **ok**: La tarea se ejecutó y el sistema ya estaba en el estado deseado (no se hizo ningún cambio).
    - **changed**: La tarea se ejecutó y realizó un cambio en el sistema.
    - **failed**: La tarea falló.
    - **skipped**: La tarea fue omitida (por una condición `when`).

---

## 7. Módulos esenciales

### 7.1 Módulo `apt` — Gestión de paquetes (Debian/Ubuntu)

```yaml
- name: Instalar varios paquetes
  apt:
    name:
      - vim
      - curl
      - git
    state: present
    update_cache: yes

- name: Desinstalar un paquete y sus dependencias
  apt:
    name: apache2
    state: absent
    purge: yes
```

| Parámetro | Descripción |
| --------- | ----------- |
| `name` | Nombre del paquete (o lista de paquetes) |
| `state` | `present` (instalar), `absent` (desinstalar), `latest` (actualizar) |
| `update_cache` | Actualizar la caché apt antes de instalar |
| `purge` | Eliminar también los ficheros de configuración |

### 7.2 Módulo `user` — Gestión de usuarios

```yaml
- name: Crear usuario alumno
  user:
    name: alumno
    comment: "Usuario alumno del sistema"
    shell: /bin/bash
    groups: sudo
    append: yes
    state: present
    password: "{{ 'MiContraseña123' | password_hash('sha512') }}"
    create_home: yes

- name: Eliminar usuario
  user:
    name: alumno
    state: absent
    remove: yes
```

| Parámetro | Descripción |
| --------- | ----------- |
| `name` | Nombre del usuario |
| `state` | `present` (crear) o `absent` (eliminar) |
| `groups` | Grupos a los que pertenece |
| `append` | Si es `yes`, añade los grupos sin eliminar los existentes |
| `shell` | Shell por defecto |
| `password` | Contraseña encriptada |
| `remove` | Si es `yes`, elimina también el directorio home al borrar |

### 7.3 Módulo `group` — Gestión de grupos

```yaml
- name: Crear grupo profesores
  group:
    name: profesores
    state: present
    gid: 2000

- name: Eliminar grupo
  group:
    name: profesores
    state: absent
```

### 7.4 Módulo `copy` — Copiar ficheros

```yaml
- name: Copiar fichero de configuración
  copy:
    src: ficheros/sshd_config
    dest: /etc/ssh/sshd_config
    owner: root
    group: root
    mode: '0600'
    backup: yes
```

| Parámetro | Descripción |
| --------- | ----------- |
| `src` | Ruta del fichero en el control node |
| `dest` | Ruta de destino en el managed node |
| `owner` / `group` | Propietario y grupo del fichero |
| `mode` | Permisos (en octal o simbólico) |
| `backup` | Crea copia de seguridad antes de sobreescribir |

### 7.5 Módulo `file` — Gestionar ficheros y directorios

```yaml
- name: Crear directorio
  file:
    path: /var/www/miapp
    state: directory
    owner: www-data
    group: www-data
    mode: '0755'

- name: Crear enlace simbólico
  file:
    src: /etc/nginx/sites-available/miapp
    dest: /etc/nginx/sites-enabled/miapp
    state: link

- name: Eliminar fichero
  file:
    path: /tmp/fichero_temporal.txt
    state: absent
```

| `state` | Resultado |
| ------- | --------- |
| `file` | Asegura que el fichero existe |
| `directory` | Asegura que el directorio existe |
| `link` | Crea un enlace simbólico |
| `absent` | Elimina el fichero o directorio |
| `touch` | Crea el fichero si no existe o actualiza su fecha |

### 7.6 Módulo `service` — Gestión de servicios

```yaml
- name: Gestionar servicio SSH
  service:
    name: ssh
    state: started
    enabled: yes
```

| `state` | Acción |
| ------- | ------ |
| `started` | Arranca el servicio si está parado |
| `stopped` | Para el servicio si está en ejecución |
| `restarted` | Reinicia el servicio siempre |
| `reloaded` | Recarga la configuración sin parar el servicio |

### 7.7 Módulo `cron` — Gestión de tareas cron

```yaml
- name: Programar copia de seguridad diaria
  cron:
    name: "Backup diario"
    minute: "0"
    hour: "2"
    day: "*"
    month: "*"
    weekday: "*"
    job: "/usr/local/bin/backup.sh"
    user: root
    state: present

- name: Eliminar tarea cron
  cron:
    name: "Backup diario"
    state: absent
```

### 7.8 Módulo `lineinfile` — Modificar líneas en ficheros

Permite asegurar que una línea concreta existe (o no existe) en un fichero de configuración, sin necesidad de copiar el fichero entero.

```yaml
- name: Deshabilitar login de root por SSH
  lineinfile:
    path: /etc/ssh/sshd_config
    regexp: '^PermitRootLogin'
    line: 'PermitRootLogin no'
    state: present
    backup: yes

- name: Establecer número máximo de intentos de autenticación
  lineinfile:
    path: /etc/ssh/sshd_config
    regexp: '^MaxAuthTries'
    line: 'MaxAuthTries 3'
```

---

## 8. Variables

Las variables en Ansible permiten reutilizar playbooks para diferentes entornos o configuraciones.

### 8.1 Definir variables en el playbook

```yaml
---
- name: Instalar servidor web con variables
  hosts: webservers
  become: true

  vars:
    paquete_web: nginx
    puerto: 80
    directorio_web: /var/www/html

  tasks:
    - name: Instalar {{ paquete_web }}
      apt:
        name: "{{ paquete_web }}"
        state: present

    - name: Crear directorio web
      file:
        path: "{{ directorio_web }}"
        state: directory
        mode: '0755'
```

!!! warning "Atención"
    Cuando el valor de un parámetro empieza directamente por `{{`, debe ir entre comillas:
    ```yaml
    name: "{{ variable }}"   # Correcto
    name: {{ variable }}     # Error de sintaxis YAML
    ```

### 8.2 Ficheros de variables (`vars_files`)

Para mantener los playbooks limpios, las variables pueden guardarse en ficheros separados:

```yaml
# variables.yml
paquete_web: nginx
puerto: 80
usuarios:
  - nombre: alumno1
    shell: /bin/bash
  - nombre: alumno2
    shell: /bin/bash
```

```yaml
# playbook.yml
---
- name: Playbook con variables externas
  hosts: all
  vars_files:
    - variables.yml

  tasks:
    - name: Instalar {{ paquete_web }}
      apt:
        name: "{{ paquete_web }}"
        state: present
```

### 8.3 Variables de host y grupo (`host_vars` / `group_vars`)

Ansible carga automáticamente variables desde directorios con nombres especiales:

```
proyecto/
├── inventory.ini
├── playbook.yml
├── group_vars/
│   ├── all.yml          # Variables para todos los hosts
│   └── webservers.yml   # Variables solo para el grupo webservers
└── host_vars/
    └── 192.168.1.10.yml # Variables solo para ese host
```

### 8.4 Iterar con bucles (`loop`)

```yaml
- name: Crear varios usuarios
  user:
    name: "{{ item.nombre }}"
    shell: "{{ item.shell }}"
    state: present
  loop:
    - { nombre: "alumno1", shell: "/bin/bash" }
    - { nombre: "alumno2", shell: "/bin/bash" }
    - { nombre: "alumno3", shell: "/bin/sh" }
```

También se puede iterar sobre una lista definida en variables:

```yaml
vars:
  usuarios:
    - alumno1
    - alumno2
    - alumno3

tasks:
  - name: Crear usuarios
    user:
      name: "{{ item }}"
      state: present
    loop: "{{ usuarios }}"
```

### 8.5 Condicionales (`when`)

```yaml
- name: Instalar Apache solo en servidores web
  apt:
    name: apache2
    state: present
  when: "'webservers' in group_names"

- name: Reiniciar servicio solo si el SO es Ubuntu
  service:
    name: nginx
    state: restarted
  when: ansible_distribution == "Ubuntu"

- name: Tarea solo si el fichero existe
  command: cat /etc/configuracion.txt
  when: fichero_config.stat.exists
```

Algunas variables del sistema (`facts`) muy útiles en condicionales:

| Variable | Descripción |
| -------- | ----------- |
| `ansible_distribution` | Distribución (Ubuntu, Debian, CentOS...) |
| `ansible_distribution_version` | Versión de la distribución |
| `ansible_os_family` | Familia del SO (Debian, RedHat...) |
| `ansible_hostname` | Nombre del host |
| `ansible_default_ipv4.address` | Dirección IP principal |

---

## 9. Handlers

Los **handlers** son tasks especiales que solo se ejecutan cuando son notificados por otra task que ha producido un cambio (`changed`). Se usan habitualmente para reiniciar servicios tras modificar su configuración.

```yaml
---
- name: Configurar SSH de forma segura
  hosts: all
  become: true

  tasks:
    - name: Deshabilitar login de root
      lineinfile:
        path: /etc/ssh/sshd_config
        regexp: '^PermitRootLogin'
        line: 'PermitRootLogin no'
      notify: Reiniciar SSH

    - name: Limitar intentos de autenticación
      lineinfile:
        path: /etc/ssh/sshd_config
        regexp: '^MaxAuthTries'
        line: 'MaxAuthTries 3'
      notify: Reiniciar SSH

  handlers:
    - name: Reiniciar SSH
      service:
        name: ssh
        state: restarted
```

!!! note "Información"
    Aunque la task "Deshabilitar login de root" y "Limitar intentos" notifiquen al mismo handler, **el handler solo se ejecuta una vez** al final del play, independientemente de cuántas veces se haya notificado. Esto evita reinicios innecesarios.

---

## 10. Plantillas Jinja2

El módulo `template` permite generar ficheros de configuración dinámicos a partir de plantillas **Jinja2**, sustituyendo variables de Ansible en el contenido del fichero.

Las plantillas tienen extensión `.j2` y se guardan en el directorio `templates/` del proyecto.

**Ejemplo: plantilla de mensaje de bienvenida**

```
# templates/motd.j2
Bienvenido a {{ ansible_hostname }}
Sistema operativo: {{ ansible_distribution }} {{ ansible_distribution_version }}
Administrado por Ansible
Fecha de configuración: {{ ansible_date_time.date }}
```

**Playbook que usa la plantilla:**

```yaml
- name: Configurar mensaje de bienvenida
  template:
    src: templates/motd.j2
    dest: /etc/motd
    owner: root
    group: root
    mode: '0644'
```

**Ejemplo: plantilla de configuración de Nginx con variables**

```nginx
# templates/nginx.conf.j2
server {
    listen {{ puerto }};
    server_name {{ ansible_hostname }};
    root {{ directorio_web }};

    access_log /var/log/nginx/{{ ansible_hostname }}_access.log;
    error_log  /var/log/nginx/{{ ansible_hostname }}_error.log;
}
```

---

## 11. Ansible Vault — Proteger datos sensibles

**Ansible Vault** permite cifrar variables o ficheros enteros que contienen datos sensibles (contraseñas, claves API, tokens), de forma que puedan incluirse con seguridad en el control de versiones.

```bash
# Cifrar un fichero de variables
ansible-vault encrypt variables_secretas.yml

# Editar un fichero cifrado
ansible-vault edit variables_secretas.yml

# Ver el contenido de un fichero cifrado
ansible-vault view variables_secretas.yml

# Descifrar un fichero
ansible-vault decrypt variables_secretas.yml

# Ejecutar un playbook que usa ficheros cifrados
ansible-playbook -i inventory.ini playbook.yml --ask-vault-pass
```

**Ejemplo de uso:**

```yaml
# variables_secretas.yml (cifrado con vault)
db_password: "MiContraseñaSegura123"
api_token: "abc123xyz"
```

```yaml
# playbook.yml
---
- name: Configurar base de datos
  hosts: dbservers
  vars_files:
    - variables_secretas.yml
  tasks:
    - name: Configurar contraseña de BD
      lineinfile:
        path: /etc/myapp/config.ini
        regexp: '^db_password'
        line: "db_password={{ db_password }}"
```

---

## 12. Estructura de un proyecto Ansible

A medida que los proyectos crecen, es recomendable organizar los ficheros siguiendo esta estructura:

```
proyecto-ansible/
├── inventory.ini           # Inventario de hosts
├── playbook_principal.yml  # Playbook principal
├── group_vars/
│   ├── all.yml             # Variables para todos los hosts
│   └── webservers.yml      # Variables para el grupo webservers
├── host_vars/
│   └── servidor1.yml       # Variables para un host específico
├── templates/
│   ├── nginx.conf.j2       # Plantilla Nginx
│   └── motd.j2             # Plantilla MOTD
├── files/
│   └── sshd_config         # Ficheros estáticos para copiar
└── roles/
    └── webserver/          # Rol para servidores web
        ├── tasks/
        │   └── main.yml
        ├── handlers/
        │   └── main.yml
        ├── templates/
        └── vars/
            └── main.yml
```

---

## 13. Entorno de laboratorio

### Escenario

Todos los ejercicios se realizan sobre un entorno de tres máquinas virtuales Ubuntu Server levantadas con **Vagrant** y **VirtualBox**:

| Máquina | Rol | IP |
| ------- | --- | -- |
| `control` | Control node — Ansible instalado aquí | 192.168.56.10 |
| `web01` | Managed node — servidor web | 192.168.56.11 |
| `db01` | Managed node — servidor de base de datos | 192.168.56.12 |

### Vagrantfile

Crea un directorio `laboratorio-ansible/` y guarda dentro el siguiente fichero con el nombre `Vagrantfile`:

```ruby
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"

  config.vm.synced_folder ".", "/vagrant", disabled: true

  vms = [
    { name: "control", ip: "192.168.56.10" },
    { name: "web01",   ip: "192.168.56.11" },
    { name: "db01",    ip: "192.168.56.12" },
  ]

  vms.each do |vm|
    config.vm.define vm[:name] do |node|
      node.vm.hostname = vm[:name]
      node.vm.network "private_network", ip: vm[:ip]

      node.vm.provider "virtualbox" do |vb|
        vb.name   = vm[:name]
        vb.memory = 512
        vb.cpus   = 1
      end

      # Python 3 es la única dependencia de Ansible en los managed nodes
      node.vm.provision "shell", inline: <<~SHELL
        apt-get update -qq
        apt-get install -y python3
      SHELL

      # Ansible y clave SSH solo en el control node
      if vm[:name] == "control"
        node.vm.provision "shell", inline: <<~SHELL
          apt-get install -y ansible
          sudo -u vagrant ssh-keygen -t ed25519 -N "" -f /home/vagrant/.ssh/id_ed25519
        SHELL
      end
    end
  end
end
```

### Levantar el entorno

```bash
# Levantar las tres VMs
vagrant up

# Comprobar el estado de las VMs
vagrant status

# Acceder al control node
vagrant ssh control

# Apagar las VMs al terminar la sesión
vagrant halt

# Destruir el entorno para empezar desde cero
vagrant destroy -f
```

!!! warning "Primera ejecución"
    `vagrant up` descarga la box `ubuntu/jammy64` (~500 MB) la primera vez. Si la conexión del aula es lenta, el profesor puede distribuirla en USB:
    ```bash
    vagrant box add ubuntu/jammy64 /ruta/a/jammy64.box
    ```

!!! note "Información"
    La clave SSH del control node se genera automáticamente durante el aprovisionamiento. La distribución a los managed nodes (`ssh-copy-id`) se realiza en el **Ejercicio 1**, como parte del aprendizaje.

---

## 14. Ejercicios prácticos

!!! example "Tarea"

    **Ejercicio 1. Primeros pasos**

    Desde el control node (`vagrant ssh control`):

    1. Crea el fichero `inventory.ini` con los dos managed nodes del escenario:

        ```ini
        [webservers]
        192.168.56.11

        [dbservers]
        192.168.56.12

        [managed:children]
        webservers
        dbservers
        ```

    2. Distribuye la clave SSH a los managed nodes (usuario `vagrant`, contraseña `vagrant`):

        ```bash
        ssh-copy-id vagrant@192.168.56.11
        ssh-copy-id vagrant@192.168.56.12
        ```

    3. Verifica la conectividad con el módulo `ping`:

        ```bash
        ansible all -i inventory.ini -m ping
        ```

    4. Ejecuta comandos ad-hoc para ver el uptime y el espacio en disco de todos los nodos:

        ```bash
        ansible all -i inventory.ini -m command -a "uptime"
        ansible all -i inventory.ini -m command -a "df -h"
        ```


!!! example "Tarea"

    **Ejercicio 2. Playbook de configuración base**

    Crea un playbook `configuracion_base.yml` que realice las siguientes tareas en `web01` (192.168.56.11) y `db01` (192.168.56.12):

    1. Actualizar la caché de paquetes apt.
    2. Instalar los paquetes: `vim`, `curl`, `git`, `htop`, `net-tools`.
    3. Asegurarse de que el servicio SSH está arrancado y habilitado.
    4. Crear el directorio `/opt/scripts` con permisos `755` y propietario `root`.
    5. Generar un fichero `/etc/motd` con el hostname y la fecha de configuración usando una plantilla Jinja2.

    Ejecuta el playbook y verifica el resultado accediendo por SSH a cada nodo:

    ```bash
    ansible-playbook -i inventory.ini configuracion_base.yml
    ssh vagrant@192.168.56.11
    ssh vagrant@192.168.56.12
    ```


!!! example "Tarea"

    **Ejercicio 3. Gestión de usuarios en masa**

    Dado el fichero de variables `usuarios.yml`:

    ```yaml
    usuarios:
      - nombre: ana.garcia
        grupo: profesores
        shell: /bin/bash
      - nombre: luis.perez
        grupo: alumnos
        shell: /bin/bash
      - nombre: marta.lopez
        grupo: alumnos
        shell: /bin/bash
    ```

    Crea un playbook `gestion_usuarios.yml` que se aplique a todos los managed nodes y que:

    1. Cree los grupos `profesores` y `alumnos` si no existen.
    2. Cree cada usuario de la lista con su grupo y shell correspondientes.
    3. Cree el directorio home de cada usuario.
    4. Asigne a cada usuario una contraseña inicial `Cambiar123!` (cifrada con `password_hash`).

    Comprueba que los usuarios se han creado correctamente en `web01` y `db01`:

    ```bash
    ansible all -i inventory.ini -m command -a "cat /etc/passwd" | grep -E "ana|luis|marta"
    ```


!!! example "Tarea"

    **Ejercicio 4. Playbook de seguridad SSH**

    Crea un playbook `hardening_ssh.yml` que aplique las siguientes medidas de seguridad en el servicio SSH de `web01` (192.168.56.11) y `db01` (192.168.56.12):

    - Deshabilitar el login directo de root (`PermitRootLogin no`).
    - Limitar los intentos de autenticación a 3 (`MaxAuthTries 3`).
    - Deshabilitar la autenticación por contraseña (`PasswordAuthentication no`).
    - Cambiar el puerto SSH al 2222 (`Port 2222`).

    Usa el módulo `lineinfile` para cada cambio y un **handler** para reiniciar el servicio SSH solo cuando se haya producido algún cambio.

    !!! warning "Atención"
        Antes de deshabilitar la autenticación por contraseña, verifica que la autenticación por clave funciona correctamente (hecho en el ejercicio 1). De lo contrario, perderías el acceso a los nodos.

        Tras aplicar el playbook, actualiza el inventario para indicar el nuevo puerto:
        ```ini
        [webservers]
        192.168.56.11 ansible_port=2222

        [dbservers]
        192.168.56.12 ansible_port=2222
        ```


!!! example "Tarea"

    **Ejercicio 5. Automatización de tareas cron**

    Crea un playbook `tareas_programadas.yml` que configure en `web01` y `db01`:

    1. Una tarea cron que ejecute `apt update && apt upgrade -y` todos los domingos a las 03:00.
    2. Una tarea cron que limpie `/tmp` de ficheros con más de 7 días de antigüedad cada día a las 01:00.
    3. Una tarea cron que guarde el uso de disco en `/var/log/espacio_disco.log` cada hora.

    Verifica que las tareas se han registrado en los nodos:

    ```bash
    ansible all -i inventory.ini -m command -a "crontab -l -u root"
    ```


!!! tip "Reto"

    **Ejercicio 6 (Avanzado). Caso integrador: despliegue de servidor web**

    Crea un playbook completo `despliegue_web.yml` que se aplique al grupo `webservers` (`web01`, 192.168.56.11) y que:

    1. Instale y configure Nginx.
    2. Genere la configuración de Nginx desde una plantilla Jinja2 con el nombre del host y el directorio web.
    3. Cree el usuario `webmaster` con permisos sobre el directorio `/var/www/html`.
    4. Copie una página `index.html` básica al directorio web con el nombre del servidor en el título.
    5. Habilite y arranque Nginx usando un handler.
    6. Programe una tarea cron para renovar certificados SSL cada 90 días (comando: `certbot renew`).
    7. Proteja las variables sensibles (si las hay) con **Ansible Vault**.

    Verifica que el servidor web responde correctamente desde el control node:

    ```bash
    curl http://192.168.56.11
    ```
