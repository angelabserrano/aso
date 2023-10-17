---
typora-copy-images-to: ../assets/img/windows_server
typora-root-url: ../../
layout: post
title: Windows - Administración de procesos y servicios
categories: wserver
conToc: true
permalink: wserver-administracion
---

## 1. Definición de un proceso

Un **proceso** es una instancia de un programa en ejecución. Es decir, cada vez que se lanza un programa, se crea un proceso.  

## 2. Estructura de los procesos

Los procesos se estructuran de forma **jerárquica**. El sistema operativo lanza el primero y a partir de este se crean todos los demás.

El sistema operativo crea una estructura de control en la que tiene toda la información del proceso. A esta estructura se le llama **BCP** (Bloque de control de proceso).

El **BCP** (Bloque de control del proceso), dependiendo del sistema operativo, suele almacenar :

- **Identificador del proceso** **(PID)**

- Estado del proceso: preparado, activo o bloqueado.

- **Contexto de la ejecución**: registros del procesador, bits de estado.

- Aspectos relacionados con la **administración de la memoria**: espacio de direcciones y cantidad asignada

- Aspectos relacionados con la **administración de ficheros:** ficheros con los que el proceso está operando actualmente.

- **Estadísticas temporales**: Tiempo de lanzamiento del proceso, tiempo en estado activo, etc.

  

## 3. Tipos de procesos

Atendiendo a la interacción con el usuario podemos distinguir:

- **Procesos en primer plano (foreground)**: precisan de la intervención del usuario.
- **Procesos en segundo plano (background):** Se ejecutan sin que el usuario tenga que hacer nada

Atendiendo al modo en que se ejecutan podemos distinguir:

- **Procesos en modo kernel:** Son procesos que tienen acceso privilegiado a todo el equipo. Son mucho más seguros. La mayoría de procesos del sistema operativo son de este tipo.
- **Procesos en modo usuario:**Menos seguros. Todos los que ejecutan los usuarios y/o aplicaciones de usuario suelen ser de este tipo .

Dependiendo de quien lo ejecutó podemos distinguir:

- **Procesos del sistema:** Los que han sido lanzados por el propio sistema operativo.
- **Procesos del usuario:** Los que ha lanzado un usuario

## 4. Estados de un proceso

Hay tres estados básicos en los que puede estar un proceso:

- **En ejecución**: Tiene asignada la CPU
- **En espera:** Está en la lista para que se le conceda el procesador.
- **Bloqueado:** Está esperando a que se libere un recurso para poder seguir con su ejecución.

Al ejecutar un programa:

1- Nueva entrada en la tabla de procesos.

2 - Se le asigna un PID al proceso.

3 - Asignan recursos y memoria

4 - Se cargan las páginas del programa en memoria

5 - Se pone el proceso en la lista de espera

Cuando se le concede el procesador el proceso pasa a estar en **ejecución**. Y si necesita algún recurso que no está disponible pasa al estado de **bloqueado**. En el momento en que el recurso se libere, vuelve a estar en **espera**. También puede pasar que se le acabe su tiempo de CPU y vuelva al estado de **espera.**

![img](https://lh6.googleusercontent.com/qWCv0-QfL7kCwPhGyK7A3HNaLu9L_vhFLHDmdFJ9Vu3wpm9Ju1c47Ip8Of9X1WG3LhZVA35N9asOM4Ky-Wd48Xkz_LG7OS0fSxmea50BPGOGIr1l8yt85ZM5bUZHa-GQ_o8cAovRJCwRA0xqtaPPL4E_=s2048)

## 5. Hilos de ejecución (Threads o procesos ligeros )

Los procesos pueden ejecutarse como **un solo hilo,** es decir, las instrucciones van siguiendo un orden y nunca se pueden ejecutar a la vez dos instrucciones del mismo proceso, o en **multihilo**. Esta última consiste en que partes del mismo proceso pueden ejecutarse en paralelo, es decir, el mismo proceso tiene partes que pueden ejecutarse a la vez.

Un proceso tiene asignado un BCP y los hilos son parte del mismo proceso. La memoria asignada se comparte entre todos los hilos. También se comparten el resto de recursos.

Podemos distinguir:

- **Hilos a nivel de usuario**: Son los cuales crean los programadores y de los cuales el kernel o núcleo del sistema no es consciente de que existan, por lo que el programador debe encargarse de la sincronización.

- **Hilos a nivel de kernel:** Son gestionados por el sistema operativo. Si tenemos un procesador con varios núcleos y/o varios procesadores, se acelerará la ejecución del proceso. 

**Ventajas de los hilos frente a los procesos** 

- Los hilos son mucho más ligeros. En la creación de un proceso se necesita un tiempo para la adjudicación de recursos, cosa innecesaria en el cambio entre hilos.
- En caso de procesadores multinúcleo o sistemas multiprocesador, la eficiencia de los procesos que utilizan hilos es evidente, al poder realizar varias tareas en paralelo

**Administrador de tareas**

Podemos acceder al administrador de tareas pulsando las teclas Ctrl+Alt+Supr o ejecutando **taskmgr** desde la línea de comandos.

![image-20231013202252368](/aso/assets/img/windows_server/image-20231013202252368.png)
