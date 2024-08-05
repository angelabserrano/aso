---
typora-copy-images-to: ../assets/img/git
typora-root-url: ../../
layout: post
title: Introducción a Git y Github
categories: git
conToc: true
permalink: git
---

Antes de comenzar con los contenidos específicos de administración de sistemas operativos , es fundamental que los estudiantes se familiaricen con las herramientas de control de versiones y colaboración en desarrollo de software. Git y GitHub son herramientas esenciales en el entorno profesional que permitirán a los estudiantes almacenar, gestionar y compartir su trabajo de manera eficiente.

## Objetivos

- Comprender los conceptos básicos de Git y GitHub.
- Configurar un repositorio público en GitHub.
- Almacenar scripts y documentación de la asignatura en el repositorio.

## Contenidos

1. ### **Conceptos Básicos de Git**

   #### ¿Qué es Git?

   Git es un sistema de control de versiones distribuido, diseñado para manejar todo, desde proyectos pequeños hasta proyectos muy grandes con rapidez y eficiencia. Fue creado por Linus Torvalds en 2005 para el desarrollo del kernel de Linux. Su objetivo principal es mantener un seguimiento de los cambios en los archivos y coordinar el trabajo en esos archivos entre múltiples personas.

   #### Importancia en el desarrollo de software y administración de sistemas

   - **Colaboración**: Git permite a múltiples desarrolladores trabajar en el mismo proyecto simultáneamente sin conflictos. Cada desarrollador puede tener una copia completa del historial del proyecto.
   - **Historial de cambios**: Cada cambio en el código se registra con un mensaje de commit, permitiendo un seguimiento preciso de la evolución del proyecto.
   - **Ramas y fusión**: Facilita la creación de ramas para el desarrollo de nuevas características o corrección de errores, las cuales se pueden fusionar al proyecto principal una vez finalizadas.
   - **Recuperación**: Permite revertir a versiones anteriores del proyecto si se introducen errores.

   #### Instalación de Git en diferentes sistemas operativos

   **Windows**

   1. Descargar el instalador desde el [sitio oficial de Git](https://git-scm.com/).
   2. Ejecutar el instalador y seguir las instrucciones en pantalla, seleccionando las opciones deseadas.

   **Linux**

   - Para distribuciones basadas en Debian/Ubuntu:

     ```shell
     sudo apt update
     sudo apt install git
     ```

     

   #### Configuración inicial de Git

   Después de instalar Git, es importante configurarlo con tu nombre de usuario y correo electrónico, ya que esta información se usará en los commits.

   ```shell
   git config --global user.name "Tu Nombre"
   git config --global user.email "tuemail@ejemplo.com"
   ```

   

   #### Comandos básicos de Git

   `git init`

   Inicializa un nuevo repositorio de Git en el directorio actual.

   ```shell
   git init
   ```

   `git clone`

   Clona un repositorio existente desde una URL a tu máquina local.

   ```shell
   git clone https://github.com/usuario/repo.git
   ```

   `git add`

   Agrega archivos al área de preparación (staging area), preparándolos para el commit.

   ```shell
   git add archivo.txt
   git add .
   ```

   `git commit`

   Guarda los cambios añadidos al área de preparación en el historial del repositorio.

   ```shell
   git commit -m "Mensaje del commit"
   ```

   `git push`

   Envía los commits realizados en la rama local al repositorio remoto.

   ```shell
   git push origin master
   ```

   `git pull`

   Actualiza tu repositorio local con los cambios del repositorio remoto.

   ```shell
   git pull origin master
   ```

   `git status`

   Muestra el estado de los archivos en el directorio de trabajo y el área de preparación.

   ```shell
   git status
   ```

   `git log`

   Muestra el historial de commits del repositorio.

   ```shell
   git log
   ```

   

2. ### **Conceptos Básicos de GitHub**

   #### ¿Qué es GitHub? 

   GitHub es una plataforma en línea que permite a los desarrolladores alojar y gestionar sus proyectos utilizando Git. Proporciona un entorno colaborativo donde los desarrolladores pueden compartir sus proyectos, trabajar juntos en el código, y gestionar el historial de versiones de manera eficiente.

   ##### Plataforma para alojar repositorios Git

   - **Alojamiento de Repositorios**: GitHub ofrece almacenamiento para repositorios Git, permitiendo a los desarrolladores guardar y compartir su código con facilidad.
   - **Interfaz Web**: Proporciona una interfaz web intuitiva para interactuar con los repositorios, revisar el historial de commits, gestionar problemas (issues) y realizar solicitudes de extracción (pull requests).

   ##### Colaboración y control de versiones en la nube

   - **Colaboración**: Permite a múltiples desarrolladores trabajar en el mismo proyecto simultáneamente. Las características como los pull requests y las revisiones de código facilitan la colaboración y revisión de cambios.

   - **Control de Versiones**: Utilizando Git como backend, GitHub proporciona control de versiones robusto, permitiendo a los desarrolladores rastrear y revertir cambios en el código.

     

   #### Creación de una cuenta en GitHub

   1. **Registro**: Ve a la [página de registro de GitHub](https://github.com/join).
   2. **Formulario de Registro**: Completa el formulario de registro con tu nombre de usuario, correo electrónico y contraseña.
   3. **Verificación**: Sigue las instrucciones para verificar tu cuenta a través del correo electrónico.
   4. **Configuración Inicial**: Opcionalmente, puedes configurar algunas preferencias iniciales como temas y notificaciones.

   #### Creación de un repositorio público en GitHub

   1. **Iniciar Sesión**: Inicia sesión en tu cuenta de GitHub.
   2. **Nuevo Repositorio**: Haz clic en el botón "+" en la esquina superior derecha y selecciona "New repository".
   3. Detalles del Repositorio
      - **Nombre del Repositorio**: Proporciona un nombre único para tu repositorio.
      - **Descripción**: Opcionalmente, añade una descripción para tu repositorio.
      - **Visibilidad**: Selecciona "Public" para hacer que el repositorio sea accesible para todos.
   4. Opciones Iniciales
      - Puedes inicializar el repositorio con un archivo README, un archivo .gitignore y una licencia.
   5. **Crear Repositorio**: Haz clic en el botón "Create repository" para finalizar.

   #### Configuración de SSH para autenticación segura

   La autenticación SSH proporciona un método seguro para interactuar con GitHub sin tener que ingresar tu nombre de usuario y contraseña cada vez.

   1. **Generar una clave SSH**:

      - Abre una terminal y ejecuta el siguiente comando (reemplaza  youremail@example.com  con tu correo electrónico):

      ```
      ssh-keygen -t rsa -b 4096 -C "TU_EMAIL" "youremail@example.com"
      
      ```
   2. **Agregar la clave SSH a tu cuenta de GitHub**:

      ```bash
      cat ~/.ssh/id_rsa.pub
      ```

   3. Ve a [Configuración de SSH en GitHub](https://github.com/settings/keys) y haz clic en "New SSH key".

   - Pega la clave pública en el campo "Key" y proporciona un título descriptivo.

   - Haz clic en "Add SSH key".

     

   3. **Probar la conexión**

      ```bash
      ssh -T git@github.com
      ```

   
### Práctica 0
> -reto- **Ejercicio 1** Crea una cuenta en Github con las credenciales proporcionadas por el instituto. A continuación, crea un repositorio público con el nombre **aso** donde almacenarás todos los scripts que iremos realizando durante el curso en el módulo de **Administración de Sistemas Operativos**. Por último, configura de ssh para autentificación segura. 

3. **Flujo de Trabajo con Git y GitHub**
   - Creación y clonación de repositorios.
   - Estructura de un repositorio Git.
   - Ramas (branches) y fusiones (merges).
   - Trabajo colaborativo con GitHub: pull requests y revisiones de código.
   - Uso de GitHub Issues para seguimiento de tareas y problemas.

4. **Integración de Git y GitHub en la Asignatura**
   - Configuración del repositorio para la asignatura.
     - Creación de carpetas para scripts y documentación.
   - Ejemplo práctico: Almacenamiento del primer script.
     - Creación de un script básico en PowerShell.
     - Adición y commit del script al repositorio local.
     - Push del commit al repositorio remoto en GitHub.
   - Documentación de scripts y prácticas.
     - Uso de Markdown para documentación en GitHub.