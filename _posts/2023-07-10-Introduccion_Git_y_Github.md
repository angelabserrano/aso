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

## Objetivo:

- Comprender los conceptos básicos de Git y GitHub.
- Configurar un repositorio público en GitHub.
- Almacenar scripts y documentación de la asignatura en el repositorio.

## Contenido:

1. ### **Conceptos Básicos de Git**

   #### ¿Qué es Git?

   Git es un sistema de control de versiones distribuido, diseñado para manejar todo, desde proyectos pequeños hasta proyectos muy grandes con rapidez y eficiencia. Fue creado por Linus Torvalds en 2005 para el desarrollo del kernel de Linux. Su objetivo principal es mantener un seguimiento de los cambios en los archivos y coordinar el trabajo en esos archivos entre múltiples personas.

   #### Importancia en el desarrollo de software y administración de sistemas

   - **Colaboración**: Git permite a múltiples desarrolladores trabajar en el mismo proyecto simultáneamente sin conflictos. Cada desarrollador puede tener una copia completa del historial del proyecto.
   - **Historial de cambios**: Cada cambio en el código se registra con un mensaje de commit, permitiendo un seguimiento preciso de la evolución del proyecto.
   - **Ramas y fusión**: Facilita la creación de ramas para el desarrollo de nuevas características o corrección de errores, las cuales se pueden fusionar al proyecto principal una vez finalizadas.
   - **Recuperación**: Permite revertir a versiones anteriores del proyecto si se introducen errores.

   ### Comandos básicos de Git

   #### `git init`

   Inicializa un nuevo repositorio de Git en el directorio actual.

   ```shell
   git init
   ```

   #### `git clone`

   Clona un repositorio existente desde una URL a tu máquina local.

   ```shell
   git clone https://github.com/usuario/repo.git
   ```

   #### `git add`

   Agrega archivos al área de preparación (staging area), preparándolos para el commit.

   ```shell
   git add archivo.txt
   git add .
   ```

   #### `git commit`

   Guarda los cambios añadidos al área de preparación en el historial del repositorio.

   ```shell
   git commit -m "Mensaje del commit"
   ```

   #### `git push`

   Envía los commits realizados en la rama local al repositorio remoto.

   ```
   git push origin master
   ```

   

2. **Conceptos Básicos de GitHub**

   - ¿Qué es GitHub?
     - Plataforma para alojar repositorios Git.
     - Colaboración y control de versiones en la nube.
   - Creación de una cuenta en GitHub.
   - Creación de un repositorio público en GitHub.
   - Configuración de SSH para autenticación segura.

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