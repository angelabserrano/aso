---
typora-copy-images-to: ../assets/img/linux
typora-root-url: ../../
layout: post
title: Linux - Administración de Procesos, Servicios y automatización de tareas
categories: linux
conToc: true
permalink: linux-administracion
---
# Administración de procesos, servicios y automatización de tareas

**Índice**

1. [Introducción](#id1)
2. 



## Programación de Aula

### Resultados de Aprendizaje

Esta unidad cubre el **Resultado de aprendizaje 2 (RA2)** según el **Real Decreto 1629/2009, de 30 de octubre**, el cual es:

1. Administra procesos del sistema describiéndolos y aplicando criterios de
   seguridad y eficiencia.

Los criterios de evaluación asociados son:

- Se han descrito el concepto de proceso del sistema, tipos, estados y ciclo de
  vida.
- Se han utilizado interrupciones y excepciones para describir los eventos internos
  del procesador.
- Se ha diferenciado entre proceso, hilo y trabajo.
- Se han realizado tareas de creación, manipulación y terminación de procesos.
- Se ha utilizado el sistema de archivos como medio lógico para el registro e
  identificación de los procesos del sistema.
- Se han utilizado herramientas gráficas y comandos para el control y seguimiento
  de los procesos del sistema.
- Se ha comprobado la secuencia de arranque del sistema, los procesos
  implicados y la relación entre ellos.
- Se han tomado medidas de seguridad ante la aparición de procesos no
  identificados.
- Se han documentado los procesos habituales del sistema, su función y relación
  entre ellos.







### Planificación Temporal (6 sesiones / 12 horas)

| Sesión | Contenido                                        |
| ------ | ------------------------------------------------ |
| 1      | Administración de procesos: definición, estados, |
|        |                                                  |
|        |                                                  |
|        |                                                  |



<div id="id1" />

## 1. Introducción 
En esta unidad trabajaremos la administración de procesos, servicios del sistema y la automatización de tareas. 



## 2. Administración de procesos

### 2.1 Definición de proceso

Un **proceso** es una instancia de un programa en ejecución. Cada vez que ejecutas un comando o abres una aplicación, el sistema operativo crea un proceso correspondiente para llevar a cabo la tarea. El sistema dispondrá de una ***Tabla de procesos***, conocida como el **Bloque de Control de Procesos** (BCP o Process Control Block en inglés) donde guarda la información relevante de cada proceso. En Linux encontraremos la siguiente información:

| Campo                                 | Descripción                                                  |
| ------------------------------------- | ------------------------------------------------------------ |
| **PID (Process ID)**                  | Identificador único del proceso.                             |
| **PPID (Parent PID)**                 | Identificador del proceso padre.                             |
| **Estado del proceso**                | El estado actual del proceso (ejecutándose, dormido, zombie, etc.). |
| **Contador de programa**              | Dirección de la siguiente instrucción a ejecutar (PC, Program Counter). |
| **Registros del CPU**                 | Estado de los registros del procesador (acumulador, índice, puntero, etc.). |
| **Prioridad**                         | Valor que determina la prioridad del proceso para su ejecución. |
| **Memoria asignada**                  | Información sobre la memoria asignada al proceso (segmentos de código, datos, y pila). |
| **Tabla de descriptores de archivos** | Lista de archivos abiertos por el proceso y sus descriptores. |



### 2.2 Descripción de los estados del proceso

Un proceso puede estar en diferentes estados como:

![](/aso_github/assets/img/linux/process-states.jpg)



- **Running (R):**
  - El proceso se está ejecutando en ese momento o está listo para ejecutarse.
- **Sleeping (S):**
  - El proceso está inactivo, esperando la finalización de una operación o un evento (por ejemplo, espera de entrada/salida).
  - Se clasifica en dos tipos:
    - **Interrumpible (S)**: Puede ser despertado por señales externas o eventos. Aparece como S
    - **No interrumpible (D):** No puede ser interrumpido hasta que complete lo que está esperando (generalmente se usa para operaciones de E/S  en dispositivos). Se muestra como D
- **Stopped (T):**
  - El proceso está detenido, normalmente por una señal como SIGSTOP o mientras se está depurando con un debugger. Aparece como T
- **Zombie (Z):**
  - El proceso ha terminado su ejecución, pero su entrada en la tabla de procesos no ha sido limpiada del todo y sigue teniendo la identidad del proceso (PID). Aparece como Z.
- **Traced o suspendido (T):**
  - Similar al estado detenido, pero ocurre cuando un proceso está siendo depurado. se muestra también como T en algunas versiones del Kernel.
- **Dead (X):**
  - Un estado transitorio, en el que el proceso ha terminado de ejecutarse y está en proceso de ser elminado del sistema.

### 2.3 Crear, supervisar y matar procesos

Cada vez que invocamos un comando, se inician uno o más procesos. Un  administrador de sistemas no solo necesita crear  procesos, sino también poder realizar un seguimiento de ellos y  enviarles diferentes tipos de señales si es necesario. En este apartado veremos el control del trabajo y cómo monitorear los procesos.

#### 2.3.1 Control de trabajos

Los **trabajos (jobs)** son procesos que se han iniciado de forma interactiva a través de un terminal, enviados a un segundo plano y aún no han finalizado la ejecución. El comando que nos permite conocer los trabajos activos (y su estado) es el siguiente:

```bash
jobs
```



3. Administración de los servicios del sistema

   [En construcción]

4. Automatización de tareas.

​	[En construcción]

