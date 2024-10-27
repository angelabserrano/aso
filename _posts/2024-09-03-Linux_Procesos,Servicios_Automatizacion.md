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

| Sesión | Contenido                                                    |
| ------ | ------------------------------------------------------------ |
| 1      | Administración de procesos: definición, estados, crear, supervisar y matar procesos |
| 2      | Prioridad de los procesos                                    |
| 3      | Control de servicios y daemons                               |
| 4      |                                                              |



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

![process-states](/aso/assets/img/linux/process-states.png)



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

### 2.3 Comandos en Linux para la gestión de procesos

Cada vez que invocamos un comando, se inician uno o más procesos. Un  administrador de sistemas no solo necesita crear  procesos, sino también poder realizar un seguimiento de ellos y  enviarles diferentes tipos de señales si es necesario. En este apartado veremos el control del trabajo y cómo monitorear los procesos.

A continuación se muestra una tabla resumen de comandos para la gestión de procesos:

| Comando | Descripción                                                  |
| ------- | ------------------------------------------------------------ |
| jobs    | Lista los procesos en segundo plano y suspendidos en la terminal actual. |
| bg      | Envía un proceso suspendido al segundo plano para que continúe ejecutándose. |
| fg      | Trae un proceso en segundo plano al primer plano.            |
| &       | Operador para ejecutar un comando en segundo plano, permitiendo continuar usando la terminal. |
| ps      | Muestra una lista de procesos en ejecución en el sistema.    |
| pstree  | Muestra los procesos en forma de árbol, mostrando la relación de padre-hijo entre procesos. |
| top     | Muestra los procesos en tiempo real, ordenados por consumo de recursos como CPU y memoria. |
| htop    | Similar a `top`, pero con una interfaz interactiva y colorida (requiere instalación previa). |
| kill    | Envía una señal a un proceso para detenerlo o finalizarlo, usando su PID. |
| killall | Finaliza todos los procesos que coincidan con un nombre específico. |
| nice    | Inicia un proceso con una prioridad específica (valor de "niceness" ajustado). |
| renice  | Cambia la prioridad de un proceso que ya está en ejecución.  |
| nohup   | Ejecuta un comando ignorando la señal de cierre de sesión, útil para tareas de larga duración. |
| lsof    | Lista los archivos abiertos por los procesos, útil para ver qué archivos están en uso. |



#### 2.3.1 El comando ps

El comando **ps** proporciona información sobre los procesos que se están ejecutando en el sistema.  Si  escribimos  en  el  terminal  `ps`,  obtendremos  como  salida  un  listado  de  los procesos lanzados con el usuario actual que aún se están ejecutando.

​    ![img](/aso_github/assets/img/linux/comando_ps.png)

Las columnas que se muestran cuando ejecutamos el comando **ps** significan:

- La primera columna es el **PID** o identificador de  proceso. Cada proceso tiene un asociado identificador que es único, es  decir que no puede haber dos procesos con el mismo identificador.
- La  segunda  columna  nos  informa  del  terminal  en  el  que  se   está  ejecutando  el proceso.  Si  aparece  una  interrogación  (?),  el  proceso  no  tiene  asociada  ninguna terminal.
- La tercera columna indica el tiempo total que ha estado ejecutándose el proceso.
- La cuarta columna es el nombre del proceso.

#### Parámetros/modificadores ps[¶](https://fjavier-hernandez.github.io/aso/03_Procesos/033_GestionProcesosShell.html#parametrosmodificadores-ps)

- **-e** devuelve un listado de todos los procesos que se están ejecutando. 
- **-f** devuelve un listado extendido. En este último caso veremos en pantalla el **PPID** del proceso (identificador del proceso padre) y la hora en la que se ejecutó el proceso (STIME).

​    ![img](/aso_github/assets/img/linux/comando_ps2.png)    Resultado comando ps -f

- **-ef** obtendríamos un listado extendido de todos los procesos que se están ejecutando en el sistema.
- **-u**  informa  de  los  procesos  lanzado  por  un  determinado  usuario.  De  tal  forma  que  si escribimos “**ps -u alumno**”, aparecerá un listado de los procesos que está ejecutando el usuario alumno. 

#### 2.3.2 El comando pstree

El comando **pstree** visualiza, en forma de árbol, todos  los procesos del sistema, de esta forma se puede ver las relaciones que  existen entre los procesos.

![img](/aso_github/assets/img/linux/004.png)



#### 2.3.3 El comando top

El comando top devuelve un listado de los procesos de forma parecida a como lo hace ps, con la diferencia que la **información mostrada se va actualizando periódicamente** lo que nos permite ver la evolución del estado de los procesos.

En la parte superior se muestra la siguiente información adicional:

- El espacio en memoria ocupado por los procesos.
- El espacio ocupado por la memoria de intercambio o swap.
- El número total de tareas o procesos que se están ejecutando.
- El número de usuarios o el porcentaje de uso del procesador.

![img](/aso_github/assets/img/linux/005.png)



#### 2.3.4 Procesos en primer plano y segundo plano

Los procesos pueden ejecutarse en **primer plano** (Foreground) o **segundo plano** (Background). 

- El proceso que está en **primer plano** es aquel con el que se interactúa. Si ejecutamos, por ejemplo, el comando `ls -l`, se  mostrará  por  pantalla  el  resultado,  y  hasta  que  no  acabe   de  mostrarse  el  listado  no podremos ejecutar ningún otro comando.

- Un proceso en **segundo plano** añadiendo el símbolo ampersand (**&**) al final del comando. Cuando se ejecuta un proceso en segundo plano, se permite al usuario iniciar y trabajar con otros procesos.

  Ejemplo:

  ```bash
  sleep 100 &
  ```

  Para ver que trabajos se están ejecutando en segundo plano, se usa el comando **jobs**.

  ![img](/aso_github/assets/img/linux/007.png)

  

  **Pasar procesos en segundo plano a primer plano**

  Para pasar procesos en segundo plano a primer plano, se utiliza el comando **fg**, seguido de **%n**, donde n es el número de proceso que queremos pasar a primer plano.

  ![img](/aso_github/assets/img/linux/008.png)

  **Pasar procesos en primer plano a segundo plano**

  El comando **bg** permite pasar procesos desde primer plano a segundo plano. 

  - Para pasar un proceso que se encuentra en primer plano a segundo  plano, debemos suspenderlo primero utilizando la combinación de teclas  Ctrl+Z. Cuando se pulsa esa combinación de teclas, el proceso en  ejecución se para y no vuelve a ejecutarse hasta que se pasa a primer o  segundo plano. 

  Con **bg %n** pasaremos el proceso a segundo plano.

  ![img](/aso_github/assets/img/linux/009.png)

  

3. Administración de los servicios del sistema

   [En construcción]

4. Automatización de tareas.

​	[En construcción]

