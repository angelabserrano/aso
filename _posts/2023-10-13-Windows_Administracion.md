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



## 6. Gestión de los procesos y servicios en Windows

**Administrador de tareas**

Podemos acceder al administrador de tareas pulsando las teclas **Ctrl+Alt+Supr** o ejecutando **taskmgr** desde la línea de comandos.

![image-20231031112346989](/aso/assets/img/windows_server/image-20231031112346989.png)



## 7. Administrar los procesos y servicios utilizando PowerShell

### 7.1 Consultar la información de procesos

El cmdlet **Get-Process (ps)** nos permite mostrar la información de un proceso

**Ejemplo: Mostrar los procesos activos**

```powershell
Get-Process 
Get-Process | Out-GridView
```

**Columnas**:

- **Handles**: nº de referencias abiertas por el proceso

- **NPM y PM(KB)**: memoria utilizada (no paginada y paginada) por el proceso.

- **WS(KB)**: Tamaño del proceso.

- **CPU(s)**: Tiempo de procesador utlizado por el proceso.

- **Id**: Número que identifica al proceso.

- **SI**: Es un número que identifica al dueño del proceso.

- **ProcessName**: Nombre del proceso.

  

**Ejemplo: Mostrar los 10 procesos que consume más CPU**

1. Ordenamos los procesos por consumo de CPU en forma descendente

2. Seleccionamos los 10 primeros .

```powershell
Get-Process | sort cpu -Descending | Select-Object -First 10
```

**Ejemplo: Muestra los procesos del usuario Administrador del dominio EMPRESA**

![img](https://lh7-us.googleusercontent.com/D75pb-J6wK1oKECF5zSeHpZ_D_ZZQPUESe4S3gF-ge2Nyw81oA8SefdGK9CrG-eWw7PSUvwsWLRBP1nVEcb4pGXJAM-_PsP5l05y97r_YofSGfwmOAHLTLcpCdy8IB8ci-1zDOcPDgxHN90N61JW3N3gGw=s2048)



**Ejemplo: Obtener información sobre un proceso: notepad**

Ejecutamos el programa Notepad (Bloc de notas) 

```powershell
Get-Process -Name notepad
Get-Process -Name Notepad  | fl *

#Extraemos una propiedad de un proceso: Ubicación del archivo.
(Get-Process notepad).path
#Extraemos una propiedad de un proceso: Tamaño del proceso.
(Get-Process notepad).ws 
#Tamaño del proceso expresado en MB
(Get-Process notepad).ws/1mb

```

### 7.2 Detener procesos

El cmdlet **Stop-Process** nos permite detener uno o más procesos en ejecución

**Ejemplo: Detener el proceso notepad**

```powershell
#Localizamos el proceso notepad
Get-Process -Name notepad
#Detenemos el proceso notepad
Stop-Process -Name Notepad
#También podemos detenerlo especificando el identificador
Stop-Process -Id 4388
```

### 7.3 Iniciar procesos

El cmdlet **Start-Process** nos permite iniciar procesos.

**Ejemplo: Iniciar un proceso especificando la ruta**

```powershell
Start-Process -FilePath "C:\Windows\notepad.exe"
Start-Process -FilePath "C:\ProgramFiles(x86)\Google\Chrome\Application\chrome.exe"
```

**Ejemplo: Iniciar un proceso especificando solo el nombre**

También se puede iniciar un proceso especificando solo el nombre, ya que la ruta la encuentra el sistema porque se encuentra en la variable de entorno $PATH

```powershell
Start-Process notepad
Start-Process chrome
```

**Ejemplo: Iniciar un proceso pasándole un argumento**

Abrimos Chrome y la página web de google.es

```powershell
Start-Process chrome -ArgumentList google.es
```

**Iniciar una APP de Windows** 

Aunque las apps de Windows tienen un archivo exe asociado que se encuentra en C:\Windows\SystemApps, no se pueden ejecutar desde el archivo.exe. Hay que utilizar el **protocolo asociado**.

**Edge**: Start-Process Microsoft-Edge://

**Edge:** Start-Process Microsoft-Edge:https://google.es

**Windows Store**: Start-Process Ms-Windows-Store://

**Alarmas y reloj**: Start-Process Ms-clock://

**Mapas**:Start-Process BingMaps://

### 7.4 Consultar información de los servicios

El cmdlet **Get-Service** nos proporciona información de los servicios.

```powershell
Get-Service
```

**Columnas por defecto**

**Status**: Estado del servicio (Stopped, running, etc)

**Name**: Nombre del servicio.

**DisplayName**: Nombre para mostrar.

**Ejemplo: Muestra los servicios que están arrancados**

```powershell
Get-Service | Where-Object {$_Status -eq "Running"}
```

**Mostrar información detallada de un servicio.**

Cola de impresión (Spooler): Este servicio pone en cola los trabajos de impresión y administra la interacción con la impresora. Si lo desactiva, no podrá imprimir ni ver las impresoras.

**Ejemplo: Buscar el servicio spooler**

```powershell
#Buscamos el servicio Name
Get-Service -Name "Spoo*"
#Buscamos el servicio por DisplayName
Get-Service -DisplayName "cola*"
#Obtenemos más información del servicio:
Get-Service -Name spooler | fl *
```

![img](https://lh7-us.googleusercontent.com/wEjW9VdqBPwDJcKV-b7QrX3YrlQLCi3BlMhnwmO8zc8unrxmxzfAQq43RuWT__bI1sDHOJjc7MLWo-XieQd_p5hTIJaTrrsAd8x_b1b-iU8HaAfrJdAJsEQA0igGYhnML-W3I5gkG6oRmQRxWIl6z3mi=s2048)

### 7.5 Detener un servicio

El cmdlet **Stop-Service** se utiliza para detener un servicio.

**Ejemplo: Detener el servicio de la cola de impresión**

Debemos ejecutar el siguiente comando como **administrador**

```powershell
Stop-Service -Name spooler
```

**Ejemplo: Detener el servicio Windows Update**

```powershell
Stop-Service -Name wuauserv
#En caso de no detener el servicio utilizamos la opción -force
Stop-Service -Name wuauserv -Force
```

### 7.6 Iniciar un servicio

El cmdlet **Start-Service** se utiliza para iniciar un servicio.

```powershell
#Iniciar el servicio de cola de impresión.
Start-Service -Name Spooler
#Iniciar el servicio de Windows Update
Start-Service -Name wuauserv
```



### 7.7 Modificar propiedades de los servicios

El cmdlet **Set-Service** nos permite modificar algún parámetro de un servicio.

Podemos modificar:

- Description: Descripción del servicio.
- DisplayName: Nombre para mostrar
- Tipo de inicio: StartupType
- Estado del servicio: Status

**Ejemplo: Modificar una propiedad - Tipo de inicio**

Los modos de arranque de un servicio son los siguientes:

- **Manual**: Lo arranca Windows cuando es necesario.
- **Automático**: Se arranca automáticamente con el inicio de Windows .
- **Automático (Inicio retrasado)**: Se arranca automáticamente, pero con cierto retraso respecto al inicio de Windows.
- **Deshabilitado**: El servicio no arrancará en ningún caso.



![img](https://lh7-us.googleusercontent.com/sLU3kIa_QwwU2TwZ7xl6zPb1KjIz81Kg1MZHyhrcd8lT6z4zElAkL8VXpyqOeZD8XyQ3dElfuNYnpY2GrawoRfxARQ7L337cuSM2PWZrc1bq4ZVK0UEPsHszskhto7-L7CWoY1BOOZiqs-4M_s0ObG3l=s2048)
