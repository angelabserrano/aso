---
typora-copy-images-to: ../assets/img/git
typora-root-url: ../../
layout: post
title: Introducción a Git y Github
categories: git
conToc: true
permalink: git
order: 1
---

Antes de comenzar con los contenidos específicos de administración de sistemas operativos , es fundamental que los estudiantes se familiaricen con las herramientas de control de versiones y colaboración en desarrollo de software. Git y GitHub son herramientas esenciales en el entorno profesional que permitirán a los estudiantes almacenar, gestionar y compartir su trabajo de manera eficiente.

## Objetivos

- Comprender los conceptos básicos de Git y GitHub.
- Configurar un repositorio público en GitHub.
- Almacenar scripts y documentación de la asignatura en el repositorio.

## Contenidos

### 1 Conceptos Básicos de Git

#### 1.1 ¿Qué es Git?

   Git es un sistema de control de versiones distribuido, diseñado para manejar todo, desde proyectos pequeños hasta proyectos muy grandes con rapidez y eficiencia. Fue creado por Linus Torvalds en 2005 para el desarrollo del kernel de Linux. Su objetivo principal es mantener un seguimiento de los cambios en los archivos y coordinar el trabajo en esos archivos entre múltiples personas.

#### 1.2 Importancia en el desarrollo de software y administración de sistemas

   - **Colaboración**: Git permite a múltiples desarrolladores trabajar en el mismo proyecto simultáneamente sin conflictos. Cada desarrollador puede tener una copia completa del historial del proyecto.
   - **Historial de cambios**: Cada cambio en el código se registra con un mensaje de commit, permitiendo un seguimiento preciso de la evolución del proyecto.
   - **Ramas y fusión**: Facilita la creación de ramas para el desarrollo de nuevas características o corrección de errores, las cuales se pueden fusionar al proyecto principal una vez finalizadas.
   - **Recuperación**: Permite revertir a versiones anteriores del proyecto si se introducen errores.

#### 1.3 Instalación de Git en diferentes sistemas operativos

   **Windows**

   1. Descargar el instalador desde el [sitio oficial de Git](https://git-scm.com/).
   2. Ejecutar el instalador y seguir las instrucciones en pantalla, seleccionando las opciones deseadas.

   **Linux**

   - Para distribuciones basadas en Debian/Ubuntu:

     ```
     sudo apt update
     sudo apt install git
     ```


#### 1.4 Configuración inicial de Git

   Después de instalar Git, es importante configurarlo con tu nombre de usuario y correo electrónico, ya que esta información se usará en los commits.

   ```
   git config --global user.name "Tu Nombre"
   git config --global user.email "tuemail@ejemplo.com"
   ```

   Para comprobar la ejecución ejecutamos:

   ```
   git config --list
   ```


#### 1.5 Comandos básicos de Git

   `git init`

   Inicializa un nuevo repositorio de Git en el directorio actual.

   ```
   git init
   ```

   `git clone`

   Clona un repositorio existente desde una URL a tu máquina local.

   ```
   git clone git@github.com:usuario/repositorio.git
   ```

   `git add`

   Agrega archivos al área de preparación (staging area), preparándolos para el commit.

   ```
   git add archivo.txt
   git add .
   ```

   `git commit`

   Guarda los cambios añadidos al área de preparación en el historial del repositorio.

   ```shell
   git commit -m "Mensaje del commit"
   ```

   `git push`

   Envía los commits realizados en la rama local al repositorio remoto (rama principal).

   ```shell
   git push origin main
   ```

   `git pull`

   Actualiza tu repositorio local con los cambios del repositorio remoto.

   ```
   git pull origin main
   ```

   `git status`

   Muestra el estado de los archivos en el directorio de trabajo y el área de preparación.

   ```
   git status
   ```

   `git log`

   Muestra el historial de commits del repositorio.

   ```
   git log
   ```

   

#### 1.6 Flujo de trabajo en Git

   A continuación se muestra un esquema visual del **ciclo de vida de los cambios en Git**:

   ![Desarrollo completo con GitHub](/aso/assets/img/git/image10_1a4384e5fa.avif)

   En este diagrama se distinguen las partes principales:

   - **Working Directory (directorio de trabajo):** donde editas archivos en tu PC.

   - **Staging Area (área de preparación):** donde seleccionas qué cambios quieres guardar. (`git add`)

   - **Local Repo (repositorio local):** base de datos con tus commits en tu máquina. (`git commit`)

   - **Remote Repo (GitHub):** copia del repositorio accesible online para colaborar. (`git push` / `git pull`)

     

   Y los comandos clave:

   - `git add` → mover cambios al **Staging Area**.

   - `git commit` → guardar en el **repositorio local**.

   - `git push` → enviar al **repositorio remoto (GitHub)**.

   - `git pull` → traer cambios del remoto a tu local.

   - `git checkout` / `git merge` → cambiar de rama o fusionar.

     

#### 📚 Resumen de comandos Git

Aquí tienes una ficha de referencia rápida con los comandos más útiles de Git que puedes descargar:

[Descargar PDF — Git Cheat Sheet (GitHub Education)](https://education.github.com/git-cheat-sheet-education.pdf?utm_source=chatgpt.com)


### 2 Conceptos Básicos de GitHub

#### 2.1 ¿Qué es GitHub? 

   GitHub es una plataforma en línea que permite a los desarrolladores alojar y gestionar sus proyectos utilizando Git. Proporciona un entorno colaborativo donde los desarrolladores pueden compartir sus proyectos, trabajar juntos en el código, y gestionar el historial de versiones de manera eficiente.

##### Plataforma para alojar repositorios Git

   - **Alojamiento de Repositorios**: GitHub ofrece almacenamiento para repositorios Git, permitiendo a los desarrolladores guardar y compartir su código con facilidad.
   - **Interfaz Web**: Proporciona una interfaz web intuitiva para interactuar con los repositorios, revisar el historial de commits, gestionar problemas (issues) y realizar solicitudes de extracción (pull requests).

##### Colaboración y control de versiones en la nube

   - **Colaboración**: Permite a múltiples desarrolladores trabajar en el mismo proyecto simultáneamente. Las características como los pull requests y las revisiones de código facilitan la colaboración y revisión de cambios.

   - **Control de Versiones**: Utilizando Git como backend, GitHub proporciona control de versiones robusto, permitiendo a los desarrolladores rastrear y revertir cambios en el código.

     

#### 2.2 Creación de una cuenta en GitHub

   1. **Registro**: Ve a la [página de registro de GitHub](https://github.com/join).
   2. **Formulario de Registro**: Completa el formulario de registro con tu nombre de usuario, correo electrónico y contraseña.
   3. **Verificación**: Sigue las instrucciones para verificar tu cuenta a través del correo electrónico.
   4. **Configuración Inicial**: Opcionalmente, puedes configurar algunas preferencias iniciales como temas y notificaciones.

#### 2.3 Creación de un repositorio público en GitHub

   1. **Iniciar Sesión**: Inicia sesión en tu cuenta de GitHub.
   2. **Nuevo Repositorio**: Haz clic en el botón "+" en la esquina superior derecha y selecciona "New repository".
   3. Detalles del Repositorio
      - **Nombre del Repositorio**: Proporciona un nombre único para tu repositorio.
      - **Descripción**: Opcionalmente, añade una descripción para tu repositorio.
      - **Visibilidad**: Selecciona "Public" para hacer que el repositorio sea accesible para todos.
   4. Opciones Iniciales
      - Puedes inicializar el repositorio con un archivo README, un archivo .gitignore y una licencia.
   5. **Crear Repositorio**: Haz clic en el botón "Create repository" para finalizar.

#### 2.4 Configuración de SSH para autenticación segura

   La autenticación SSH proporciona un método seguro para interactuar con GitHub sin tener que ingresar tu nombre de usuario y contraseña cada vez.

   1. **Generar una clave SSH**:

      - Abre una terminal y ejecuta el siguiente comando (reemplaza  youremail@example.com  con tu correo electrónico):

      ```
      ssh-keygen -t rsa -b 4096 -C "youremail@example.com"
      ```
   2. **Agregar la clave SSH a tu cuenta de GitHub**:

      ```
      cat ~/.ssh/id_rsa.pub
      ```

   3. Ve a [Configuración de SSH en GitHub](https://github.com/settings/keys) y haz clic en "New SSH key".

   - Pega la clave pública en el campo "Key" y proporciona un título descriptivo.

   - Haz clic en "Add SSH key".

     

   3. **Probar la conexión**

      ```
      ssh -T git@github.com
      ```


### Práctica 0
> -reto- **Ejercicio 1** Crea una cuenta en Github. A continuación, crea un repositorio público con el nombre **aso** donde almacenarás todos los scripts que iremos realizando durante el curso en el módulo de **Administración de Sistemas Operativos**. Por último, configura  ssh para autentificación segura en GitHub. 

