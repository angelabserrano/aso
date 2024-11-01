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



### Planificación Temporal (5 sesiones / 10 horas)

| Sesión | Contenido                                                    |
| ------ | ------------------------------------------------------------ |
| 1      | Administración de procesos: definición, estados y principales comandos |
| 2      | Comandos para la gestión de procesos                         |
| 3      | Control de servicios y daemons                               |
| 4      | Automatización de tareas                                     |
| 5      | Ampliación y refuerzo                                        |



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

​    <img src="/aso/assets/img/linux/comando_ps.png" alt="img" style="zoom:75%;" />

Las columnas que se muestran cuando ejecutamos el comando **ps** significan:

- La primera columna es el **PID** o identificador de  proceso. Cada proceso tiene un asociado identificador que es único, es  decir que no puede haber dos procesos con el mismo identificador.
- La  segunda  columna  nos  informa  del  terminal  en  el  que  se   está  ejecutando  el proceso.  Si  aparece  una  interrogación  (?),  el  proceso  no  tiene  asociada  ninguna terminal.
- La tercera columna indica el tiempo total que ha estado ejecutándose el proceso.
- La cuarta columna es el nombre del proceso.

#### Parámetros/modificadores ps

- **-e** devuelve un listado de todos los procesos que se están ejecutando. 
- **-f** devuelve un listado extendido. En este último caso veremos en pantalla el **PPID** del proceso (identificador del proceso padre) y la hora en la que se ejecutó el proceso (STIME).

​    ![img](/aso/assets/img/linux/comando_ps2.png)    Resultado comando ps -f

- **-ef** obtendríamos un listado extendido de todos los procesos que se están ejecutando en el sistema.
- **-u**  informa  de  los  procesos  lanzado  por  un  determinado  usuario.  De  tal  forma  que  si escribimos “**ps -u alumno**”, aparecerá un listado de los procesos que está ejecutando el usuario alumno. 

#### 2.3.2 El comando pstree

El comando **pstree** visualiza, en forma de árbol, todos  los procesos del sistema, de esta forma se puede ver las relaciones que  existen entre los procesos.

![img](/aso/assets/img/linux/004.png)



#### 2.3.3 El comando top

El comando top devuelve un listado de los procesos de forma parecida a como lo hace ps, con la diferencia que la **información mostrada se va actualizando periódicamente** lo que nos permite ver la evolución del estado de los procesos.

En la parte superior se muestra la siguiente información adicional:

- El espacio en memoria ocupado por los procesos.
- El espacio ocupado por la memoria de intercambio o swap.
- El número total de tareas o procesos que se están ejecutando.
- El número de usuarios o el porcentaje de uso del procesador.

![img](/aso/assets/img/linux/005.png)



#### 2.3.4 Procesos en primer plano y segundo plano

Los procesos pueden ejecutarse en **primer plano** (Foreground) o **segundo plano** (Background). 

- El proceso que está en **primer plano** es aquel con el que se interactúa. Si ejecutamos, por ejemplo, el comando `ls -l`, se  mostrará  por  pantalla  el  resultado,  y  hasta  que  no  acabe   de  mostrarse  el  listado  no podremos ejecutar ningún otro comando.

- Un proceso en **segundo plano** añadiendo el símbolo ampersand (**&**) al final del comando. Cuando se ejecuta un proceso en segundo plano, se permite al usuario iniciar y trabajar con otros procesos.

  Ejemplo:

  ```bash
  sleep 100 &
  ```

  Para ver que trabajos se están ejecutando en segundo plano, se usa el comando **jobs**.

  <img src="/aso/assets/img/linux/007.png" alt="img" style="zoom:75%;" />

  

  **Pasar procesos en segundo plano a primer plano**

  Para pasar procesos en segundo plano a primer plano, se utiliza el comando **fg**, seguido de **%n**, donde n es el número de proceso que queremos pasar a primer plano.

  <img src="/aso/assets/img/linux/008.png" alt="img" style="zoom:75%;" />

  **Pasar procesos en primer plano a segundo plano**

  El comando **bg** permite pasar procesos desde primer plano a segundo plano. 

  - Para pasar un proceso que se encuentra en primer plano a segundo  plano, debemos suspenderlo primero utilizando la combinación de teclas  Ctrl+Z. Cuando se pulsa esa combinación de teclas, el proceso en  ejecución se para y no vuelve a ejecutarse hasta que se pasa a primer o  segundo plano. 

  Con **bg %n** pasaremos el proceso a segundo plano.

  <img src="/aso/assets/img/linux/009.png" alt="img" style="zoom:75%;" />

#### 2.3.5 El comando kill para finalizar procesos

Para finalizar un proceso se utiliza el comando **kill**, que tiene la siguiente sintaxis: 

```bash
kill [parámetro] PID 
```

Si, por ejemplo, queremos eliminar un proceso con **PID 17122**, tendríamos que escribir: **kill 17122**.

Puede  que  en  ocasiones  el  proceso  no  finalice  al  emplear  el  comando  kill  sin parámetros. Para matar un proceso asegurándonos de  que no ignorará la petición de finalizar su ejecución se emplea el  parámetro -9.

```bash
kill -9 17122 
```

Hay un total de 32 señales que se pueden enviar a los procesos. Las más utilizadas son las siguientes:

```bash
 kill -1 (Sighup). Reinicia el proceso. 
 kill -9 (SigKill). Mata el proceso. 
 kill -15 (SigTerm). Termina el proceso. 
```

Por otra parte, el comando  **killall  nombre_programa** finaliza todos los procesos que estén ejecutando el programa.

#### 2.3.6 El comando nice

Ejecuta un comando con una prioridad distinta a la de por defecto.

Solo los usuarios root pueden establecer prioridades urgentes (negativos).

Sintaxis:

```bash
$ nice -n NUMERO_PRIORIDAD COMANDO
```

#### 2.3.7 El comando renice

El comando renice nos permite modificar la prioridad una vez que el proceso ya está en ejecución

```bash
renice [-n] <niceness> [-p|-g|-u] <identificadores>
```

donde `identificadores` se corresponde con:

- un conjunto de ids de proceso (pid) si no se especifica parámetro o se precede por -p
- un conjunto de id de grupo de proceso si se precede por -g
- un conjunto de usuarios si se precede por -u.

Los usuarios que no sean el superusuario sólo pueden bajar la  prioridad de sus procesos, es decir, aumentar su niceness (en el rango  de 0 a 19). El **superusuario** (root) puede ajustar la prioridad de cualquier proceso usando un valor nice del rango completo (-20 a 19).



## 3. Administración de los servicios del sistema

### 3.1. Concepto de Servicios en Linux

Un **servicio** en Linux es un proceso que se ejecuta en segundo plano, sin interacción directa del usuario, y que proporciona funciones o funcionalidades esenciales al sistema o a los usuarios. Algunos ejemplos comunes incluyen servidores web (como Apache o Nginx), servicios de base de datos (MySQL, PostgreSQL), y servicios de red (SSH, FTP).

### 3.2. Sistema de Inicio y Administración de Servicios

Linux tiene varios sistemas de inicio (init systems) que administran los servicios y procesos de arranque. Algunos de los sistemas de inicio más comunes incluyen:

- **SysVinit**: Uno de los sistemas de inicio más antiguos, basado en scripts de shell que se ejecutan en secuencia para iniciar servicios.
- **Upstart**: Un sistema de inicio más avanzado que reemplazó a SysVinit en algunas distribuciones, diseñado para trabajar con eventos.
- **Systemd**: Actualmente el sistema de inicio más utilizado en distribuciones modernas, que gestiona servicios mediante unidades y soporta arranque paralelo, lo que lo hace más eficiente y rápido que SysVinit y Upstart.

Cada uno de estos sistemas tiene comandos y prácticas distintas para gestionar servicios. Hoy en día, **systemd** es el sistema más común, por lo cual es el que estudiaremos a continuación.

### 3.3 Administración de Servicios con Systemd

Systemd es un sistema de administración de servicios que organiza los servicios mediante archivos de configuración llamados **unidades (units)**, que se encuentran en la ruta `/etc/systemd/system` o `/lib/systemd/system`. Cada unidad representa un servicio, un dispositivo o una tarea de administración.

#### Principales Comandos de Systemd

`systemctl` es el comando principal para gestionar servicios en systemd. Algunos comandos básicos son:

- **Iniciar un servicio**:

  ```bash
  sudo systemctl start nombre_servicio
  ```

Este comando permite iniciar un servicio de forma manual.

  - **Detener un servicio**:

    ```bash
    sudo systemctl stop nombre_servicio
    ```

Detiene el servicio en ejecución.

- **Reiniciar un servicio**:

  ```bash
  sudo systemctl restart nombre_servicio
  ```

  Detiene e inicia nuevamente el servicio, útil para aplicar cambios en la configuración.

- **Recargar un servicio**:

  ```bash
  sudo systemctl reload nombre_servicio
  ```

  Recarga la configuración del servicio sin detenerlo.

- **Habilitar un servicio**: 

  sudo systemctl enable nombre_servicio

  Activa el servicio para que se inicie automáticamente al arrancar el sistema.

- **Deshabilitar un servicio**:

  ```bash
  sudo systemctl disable nombre_servicio
  ```

​	Desactiva el inicio automático del servicio en el arranque.

- **Estado de un servicio**:

```bash
sudo systemctl status nombre_servicio
```

Muestra el estado actual del servicio, incluyendo información de logs y errores recientes.

#### Comprobación del Estado de Todos los Servicios

Para verificar el estado de todos los servicios, se puede usar:

```bash
sudo systemctl list-units --type=service
```

3. Automatización de tareas.

​	[En construcción]

