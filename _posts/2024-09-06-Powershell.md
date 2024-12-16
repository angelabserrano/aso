---
typora-copy-images-to: ../assets/img/powershell
typora-root-url: ../../
layout: post
title: Scripting en Windows. PowerShell
categories: scripts
conToc: true
permalink: powershell
---

## Programación de Aula

### Resultados de Aprendizaje

Esta unidad cubre el **Resultado de aprendizaje 7 (RA7)** según el **Real Decreto 1629/2009, de 30 de octubre**, el cual es:

1. Utiliza lenguajes de guiones en sistemas operativos, describiendo su aplicación y administrando servicios del sistema operativo.

Los criterios de evaluación asociados son:

​	a. Se han utilizado y combinado las estructuras del lenguaje para crear guiones.

​	b. Se han utilizado herramientas para depurar errores sintácticos y de ejecución.

​	c. Se han implantado guiones en sistemas libres y propietario.

​	d. Se han realizado cambios y adaptaciones de guiones del sistema.

​	e. Se han implantado guiones en sistemas libres y propietarios

​	f. Se han consultado y utilizado librerías de funciones.

​	g. Se han documentado los guiones creados.



### Planificación Temporal (6 sesiones / 12 horas)

| Sesión | Contenido                                                    |
| ------ | ------------------------------------------------------------ |
| 1      | Introducción PowerShell, Creación Primer Script, Comentarios y depuración. |
| 2      | Comandos básicos, Variables, Tipos de Datos y Operaciones Básicas |
| 3      | Estructuras condicionales                                    |
| 4      | Estructuras repetitivas                                      |
| 5      | Importación de datos y funciones                             |
| 6      | Refuerzo y Ampliación                                        |



## 1. Introducción

### 1.1 ¿Qué es PowerShell? ###

**PowerShell** es un intérprete de línea de comandos orientado a objetos de Microsoft. Fue diseñado para su uso por parte de administradores, con el propósito de automatizar tareas o realizarlas de forma más controlada. Se incluye por defecto desde WS 2008 R2 y Windows 7.

> -info- Las órdenes incluidas en Powershell son muchas y reciben el nombre de **cmdlets** . Un cmdlet se nombra siempre mediante el siguiente formato: Verbo-Sustantivo

PowerShell se ejecuta en Windows, Linux y MacOS. 



### **1.2 Versiones de PowerShell**

A partir de la versión 6, PowerShell se puede instalar en varios sistemas operativos. A esta versión se la conoce como **PowerShell Core**. A continuación, se muestran las diferentes versiones de PowerShell:



| Versión                | Fecha de lanzamiento | Descripción                                                  |
| ---------------------- | -------------------- | ------------------------------------------------------------ |
| PowerShell 7.2         | Noviembre de 2024    | Compilado en .NET 6.0                                        |
| PowerShell 7.1         | Noviembre de 2020    | Compilado en .NET 5.0                                        |
| PowerShell 7.0         | Marzo de 2020        | Compilado en .NET Core 3.1                                   |
| PowerShell 6.2         | Marzo de 2019        |                                                              |
| PowerShell 6.1         | Septiembre de 2018   | Compilado en .NET Core 2.1                                   |
| PowerShell 6.0         | Enero de 2018        | Primera versión compilada en .NET Core 2.0 . Instalable en Windows, MacOS y Linux. |
| Windows PowerShell 5.1 | Agosto de 2016       | Publicado en Windows 10 Anniversary Update y Windows Server 2016, WMF 5.1 |
| Windows PowerShell 5.0 | Febrero de 2016      | Publicado en Windows Management Framework [WMF] 5.0          |
| Windows PowerShell 4.0 | Octubre de 2013      | Integrado en Windows 8.1 y con Windows Server 2012 R2, WMF 4.0 |
| Windows PowerShell 3.0 | Octubre de 2012      | Integrado en Windows 8 y con Windows Server 2012, WMF 3.0    |
| Windows PowerShell 2.0 | Julio de 2009        | Integrado en Windows 7 y Windows Server 2008 R2              |
| Windows PowerShell 1.0 | Noviembre de 2006    | Componente opcional en Windows Server 2008                   |

Para obtener la versión de PowerShell instalada:

```
$PSVersionTable
```

![image-20230715104849336](/aso/assets/img/powershell/image-20230715104849336.png)



### 1.3 Ejecución de PowerShell ###

 En **Windows** tenemos dos opciones a la hora de ejecutar PowerShell:

1. Entorno gráfico: PowerShell ISE (del inglés, Integrated Scripting Environment).
2. Entorno comando: Windows Powershell

![image-20230714211446318](/aso/assets/img/powershell/image-20230714211446318.png)



En **Linux** tenemos varios métodos para instalar PowerShell.

Instalación de PowerShell en Ubuntu:

Accedemos al respositorio oficial de PowerShell https://github.com/PowerShell y nos descargamos el paquete .deb para la versión de Ubuntu que tenemos instalada en nuestro PC.

```
dpkg -i powershell-lts_7.2.13-1.deb_amd64.deb
```

Una vez instalado,  para abrir PowerShell tecleamos en el terminal:

```
pwsh
```



### 1.4 Execution Policies

La **política de ejecución** (execution policy) de PowerShell es una característica de seguridad destinada a controlar las condiciones bajo las cuales PowerShell carga los archivos de configuración y ejecuta scripts. Esta característica ayuda a controlar la ejecución de scripts maliciosos.

Tenemos las siguientes políticas de ejecución:

**Unrestricted**: Es la política menos restrictiva. Los usuarios pueden ejecutar todos los scripts.

**Bypass**: Al igual que unrestricted, esta política de ejecución no bloquea nada. 

**Undefined**: PowerShell elimina cualquier política de ejecución asignada.

**RemoteSigned**: Esta política, establece que todos los scripts remotos deben estar firmados.

**AllSigned**: Todos los scripts deben esta firmados.

**Restricted**: Es la polícita más restrictiva. Si se establece esta polícita no se puede ejecutar ningún script.



Para consultar la política de ejecución configurada ejecutamos el siguiente comando:

```powershell
Get-ExecutionPolicy
```

Si deseamos consultar todas las políticas de ejecución disponibles:

```powershell
Get-ExecutionPolicy -List
```

Por razones de seguridad, PowerShell está configurado de forma predeterminada para permitir solo la ejecución de scripts firmados. La ejecución del siguiente comando le permitirá ejecutar scripts sin firmar (debe ejecutar PowerShell como administrador para hacer esto)

```powershell
Set-ExecutionPolicy RemoteSigned
```

### 1.5 Creación de mi Primer Script 

Vamos a crear nuestro primer script, y como en todos los lenguajes de  programación el primero programa siempre es un "Hola mundo", pues ese  será también nuestro primer script.

Para comenzar a crear nuestros script utilizaremos el IDE llamado **PowerShell ISE**

<iframe id="aswift_8" name="aswift_8" style="left: 0px; top: 0px; border: 0px; width: 892px; height: 0px;" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" width="892" height="0" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" src="https://googleads.g.doubleclick.net/pagead/ads?npa=1&amp;gdpr=1&amp;gdpr_consent=CQBsaMAQBsaMAEsACBESA9EoAP_gAEPgABi4INJB7C7FbSFCwH5zaLsAMAhHRsAAQoQAAASBAmABQAKQIAQCgkAQFASgBAACAAAAICZBIQIECAAACUAAQAAAAAAEAAAAAAAIIAAAgAEAAAAIAAACAAAAEAAIAAAAEAAAmAgAAIIACAAAhAAAAAAAAAAAAAAAAgCAAAAAAAAAAAAAAAAAAQOhSD2F2K2kKFkPCmwXYAYBCujYAAhQgAAAkCBMACgAUgQAgFJIAgCIFAAAAAAAAAQEiCQAAQABAAAIACgAAAAAAIAAAAAAAQQAABAAIAAAAAAAAEAAAAIAAQAAAAIAABEhCAAQQAEAAAAAAAQAAAAAAAAAAABAAA&amp;addtl_consent=2~70.89.93.108.122.149.196.236.259.311.313.323.358.415.449.486.494.495.540.574.609.827.864.981.1029.1048.1051.1095.1097.1126.1205.1276.1301.1365.1415.1423.1449.1514.1570.1577.1598.1651.1716.1735.1753.1765.1870.1878.1889.1958.2072.2253.2299.2357.2373.2415.2506.2526.2568.2571.2575.2624.2677~dv.&amp;client=ca-pub-2309336300368049&amp;output=html&amp;h=280&amp;adk=4117628194&amp;adf=3198517752&amp;pi=t.aa~a.1261311059~i.51~rp.4&amp;w=892&amp;abgtt=6&amp;fwrn=4&amp;fwrnh=100&amp;lmt=1718754728&amp;num_ads=1&amp;rafmt=1&amp;armr=3&amp;sem=mc&amp;pwprc=6208560315&amp;ad_type=text_image&amp;format=892x280&amp;url=https%3A%2F%2Fwww.respuestasit.com.mx%2F2021%2F02%2Fprimer-script-powershell.html&amp;host=ca-host-pub-1556223355139109&amp;fwr=0&amp;pra=3&amp;rh=200&amp;rw=892&amp;rpe=1&amp;resp_fmts=3&amp;wgl=1&amp;fa=27&amp;dt=1720868866528&amp;bpp=1&amp;bdt=6186&amp;idt=1&amp;shv=r20240709&amp;mjsv=m202407110101&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;cookie=ID%3Dc921c266f382e703%3AT%3D1720868865%3ART%3D1720868865%3AS%3DALNI_MYFk732uBxTEsgkl5sxBWT0g1DAaQ&amp;gpic=UID%3D00000e87fc7edd10%3AT%3D1720868865%3ART%3D1720868865%3AS%3DALNI_MZzzYdfnTktkbRcuGmBN_GcMX9sRw&amp;eo_id_str=ID%3D3f6753cbc647a9d5%3AT%3D1720868865%3ART%3D1720868865%3AS%3DAA-AfjZtc4aIfTGj8kC_ZcMEGcrO&amp;prev_fmts=0x0%2C1044x280%2C120x600%2C200x200%2C120x600%2C120x600%2C120x600%2C120x600&amp;nras=2&amp;correlator=5734655040389&amp;frm=20&amp;pv=1&amp;ga_vid=1434918925.1720868861&amp;ga_sid=1720868865&amp;ga_hid=385865076&amp;ga_fc=1&amp;u_tz=120&amp;u_his=1&amp;u_h=1080&amp;u_w=1920&amp;u_ah=1048&amp;u_aw=1854&amp;u_cd=24&amp;u_sd=1&amp;adx=391&amp;ady=4768&amp;biw=1854&amp;bih=963&amp;scr_x=0&amp;scr_y=2287&amp;eid=44759875%2C44759926%2C44759837%2C31085138%2C31085211%2C95331689%2C95334508%2C95334529%2C95334828%2C31085242%2C31084184%2C95331954&amp;oid=2&amp;pvsid=2301904729429406&amp;tmod=1375128532&amp;uas=3&amp;nvt=1&amp;ref=https%3A%2F%2Fwww.google.com%2F&amp;fc=1408&amp;brdim=66%2C32%2C66%2C32%2C1854%2C32%2C1854%2C1048%2C1854%2C963&amp;vis=1&amp;rsz=%7C%7Cs%7C&amp;abl=NS&amp;fu=128&amp;bc=31&amp;bz=1&amp;ifi=9&amp;uci=a!9&amp;btvi=6&amp;fsb=1&amp;dtd=12" data-google-container-id="a!9" tabindex="0" title="Advertisement" aria-label="Advertisement" data-load-complete="true" data-google-query-id="CJWM_Yvwo4cDFflRpAQdkq0AsA"></iframe>

Cuando entremos al ISE daremos clic en el botón de Nuevo, que se encuentra en la esquina superior izquierda.

![img](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjJ1KQ2ehgir96N1_9IQ_twRpAyFSdAzfKxpcsmKEuzdJKmOmY1YQxlsR9YblVzT8s6qHcQvqA-472WPKgYgvbdMAnMHtbSQsoM-HbTjGcSFzOpNauxIqu4CiQ-HC65x-lCOtYCBMy_Axpi/w640-h274/Captura.PNG)

En la parte de la derecha, encontramos una lista de comandos  disponibles y un poco de ayuda con ellos, una vez abierto el documento  para el script procedemos a mostrar en pantalla nuestro "Hola Mundo"

Write-Host "Hola Mundo" 

![img](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiwt60KwyENbAHNSIPCq5NF-yy_Em51aNAxSgBr1Nfjj2PfYVejcibIa5dr7QMsKszIQgpucQYK0-E2IVmH40urbmmqOufBfUyqq5VhD7lYM1R5yCSfs27n-hIzYqMdm1fFuP1dUhnieclU/w640-h274/Captura.PNG)

### 1.6 Comentarios

Los comentarios en PowerShell se escriben utilizando el símbolo de **almohadilla** (#).

▸ **Comentar una línea.**

```powershell
 #Este es un comentario.
```

▸ **Comentar un bloque**

```powershell
<#
Esto es un comentario
de varias líneas
#>
```

### 1.7 Depuración

PowerShell es un potente lenguaje de scripting que puede  automatizar tareas y administrar sistemas. Sin embargo, escribir y  ejecutar scripts de PowerShell también puede introducir errores y  errores que deben corregirse. La depuración es el proceso de buscar y  resolver estos problemas en el código. A continuación se describe como depurar scripts en un equipo local mediante Windows PowerShell ISE.

- ####  Tipos de puntos de interrupción (breakpoint)

  Un punto de interrupción es una zona designada en un script que desee  que la operación entre en pausa para poder examinar el estado actual de  las variables y el entorno en que se ejecuta el script.

  Puede establecer tres tipos de puntos de interrupción en el entorno de depuración de Windows PowerShell:

  1. **Punto de interrupción de línea**. El script se pausa cuando se alcanza la línea designada durante la operación del script.

  2. **Variable breakpoint.** El script se pausa cuando cambia el valor de la variable designada.

  3. **Command breakpoint.** El script se pausa cada vez  que el comando designado está a punto de ejecutarse durante la operación del script. Puede incluir parámetros para filtrar aún más el punto de  interrupción solo para operación deseada. El comando también puede ser  una función que ha creado.

     

     En el entorno de depuración Windows PowerShell ISE, solo se pueden  establecer puntos de interrupción de línea usando el menú o los métodos  abreviados de teclado. Los otros dos tipos de puntos de interrupción se  pueden establecer, pero debe hacerse desde el panel de consola mediante  el cmdlet [Set-PSBreakpoint](https://learn.microsoft.com/es-es/powershell/module/Microsoft.PowerShell.Utility/Set-PSBreakpoint).

     

- #### Establecer un punto de interrupción.

Solo se puede establecer un punto de interrupción en un script después  de guardarlo. Haga clic con el botón derecho en la línea donde desee  establecer un punto de interrupción y después haga clic en **Alternar punto de interrupción**. O bien, haga clic en la línea donde desee establecer un punto de interrupción y presione F9 o, en el menú **Depurar**, haga clic en **Alternar punto de interrupción**.

El script siguiente es un ejemplo de cómo establecer un punto de  interrupción de variable desde el panel de consola mediante el cmdlet [Set-PSBreakpoint](https://learn.microsoft.com/es-es/powershell/module/Microsoft.PowerShell.Utility/Set-PSBreakpoint).

```powershell
# This command sets a breakpoint on the Server variable in the Sample.ps1 script.
Set-PSBreakpoint -Script sample.ps1 -Variable Server
```

- #### Enumerar todos los puntos de interrupción

  Muestra todos los puntos de interrupción de la sesión actual de Windows PowerShell.

  En el menú **Depurar**, haga clic en **Mostrar puntos de interrupción**. El script siguiente es un ejemplo de cómo enumerar todos los puntos de  interrupción desde el panel de consola mediante el cmdlet [Get-PSBreakpoint](https://learn.microsoft.com/es-es/powershell/module/Microsoft.PowerShell.Utility/Get-PSBreakpoint).

  ```powershell
  # This command lists all breakpoints in the current session.
  Get-PSBreakpoint
  ```

- #### Quitar un punto de interrupción.

  Al quitar un punto de interrupción, este se elimina. Haga clic con el botón derecho en la línea donde desee quitar un punto de interrupción y después haga clic en **ToggleBreakpoint**. O bien, haga clic en la línea donde desee quitar un punto de interrupción y, en el menú **Depurar**, haga clic en **Alternar punto de interrupción**.

  

- #### Quitar todos los puntos de interrupción

  Para quitar todos los puntos de interrupción definidos en la sesión actual, en el menú **Depurar**, haga clic en **Quitar todos los puntos de interrupción**.
  
  El script siguiente es un ejemplo de cómo quitar todos los puntos de interrupción del panel de consola mediante el cmdlet [Remove-PSBreakpoint](https://learn.microsoft.com/es-es/powershell/module/Microsoft.PowerShell.Utility/Remove-PSBreakpoint).
  
  ```powershell
  # This command deletes all of the breakpoints in the current session.
  Get-PSBreakpoint | Remove-PSBreakpoint
  ```

- #### Deshabilitar todos los puntos de interrupción
  Al deshabilitar un punto de interrupción, este no se quita; permanece desactivado hasta que se vuelve a habilitar. Para deshabilitar todos los puntos de interrupción de la sesión actual, en el menú **Depurar**, haga clic en **Deshabilitar todos los puntos de interrupción**.  El script siguiente es un ejemplo de cómo deshabilitar todos los  puntos de interrupción desde el panel de consola mediante el cmdlet [Disable-PSBreakpoint](https://learn.microsoft.com/es-es/powershell/module/Microsoft.PowerShell.Utility/Disable-PSBreakpoint).

  ```powershell
  # This command disables all breakpoints in the current session.
  # You can abbreviate this command as: "gbp | dbp".
  Get-PSBreakpoint | Disable-PSBreakpoint
  ```

- #### Habilitar un punto de interrupción

  Para habilitar un punto de interrupción específico, haga clic con el  botón derecho en la línea donde desee habilitar un punto de interrupción y después haga clic en **Habilitar punto de interrupción**. O bien, haga clic en la línea donde desee habilitar un punto de interrupción y presione F9 o, en el menú **Depurar**, haga clic en **Habilitar punto de interrupción**. El script siguiente es un ejemplo de cómo habilitar puntos de interrupción desde el panel de consola mediante el cmdlet [Enable-PSBreakpoint](https://learn.microsoft.com/es-es/powershell/module/Microsoft.PowerShell.Utility/Enable-PSBreakpoint).

  ```powershell
  # This command enables breakpoints with breakpoint IDs 0, 1, and 5.
  Enable-PSBreakpoint -Id 0, 1, 5
  ```

- #### Habilitar todos los puntos de interrupción

  Para habilitar todos los puntos de interrupción definidos en la sesión actual, en el menú **Depurar**, haga clic en **Habilitar todos los puntos de interrupción**. El script siguiente es un ejemplo de cómo habilitar todos los puntos de interrupción desde el panel de consola mediante el cmdlet [Enable-PSBreakpoint](https://learn.microsoft.com/es-es/powershell/module/Microsoft.PowerShell.Utility/Enable-PSBreakpoint).

  ```powershell
  # This command enables all breakpoints in the current session.
  # You can abbreviate the command by using their aliases: "gbp | ebp".
  Get-PSBreakpoint | Enable-PSBreakpoint
  ```

- #### ¿Cómo administrar una sesión de depuración?

  Antes de iniciar la depuración, debe establecer uno o varios puntos de  interrupción. No se puede establecer un punto de interrupción si no se  guarda el script que desea depurar. Después de iniciar la depuración, no se puede editar un script hasta  que la depuración se detenga. Un script con uno o más puntos de  interrupción establecidos se guarda automáticamente antes de ejecutarse.

  - **Iniciar la depuración**

    Presione F5 o haga clic en el icono **Ejecutar script** en la barra de herramientas, o bien, en el menú **Depurar**, haga clic en **Ejecutar o continuar**. El script se ejecuta hasta que encuentra el primer punto de  interrupción. Detiene la operación en este punto y resalta la línea en  la que se produce la pausa.

  - **Continuar la depuración**

    Presione F5 o haga clic en el icono **Ejecutar Script** en la barra de herramientas, o bien, en el menú **Depurar**, haga clic en **Ejecutar o continuar**. También puede escribir `C` en el panel de consola y presionar ENTRAR. Esto hace que el script se siga ejecutando hasta el punto de  interrupción siguiente o hasta el final si no se encuentran más puntos  de interrupción.	

  - **Ver la pila de llamadas**    

    La pila de llamadas muestra la ubicación de ejecución actual en el  script. Si el script se ejecuta en una función que llamó una función  diferente, se representa mediante filas adicionales en la salida. La  última fila muestra el script original y la línea en la que se llamó a  una función. La siguiente línea muestra esa función y la línea en la que se podría haber llamado a otra función. La primera fila muestra el  contexto actual de la línea actual en la que se estableció el punto de  interrupción.

    Mientras está en pausa, para ver la pila de llamadas actual, presione CTRL+MAYÚS+D o, en el menú **Depurar**, haga clic en **Mostrar pila de llamadas**. También puede escribir `K` en el panel de consola y presionar ENTRAR.

  - **Detener la depuración** 


​		Presione MAYÚS+F5 o, en el menú **Depurar**, haga clic en **Detener el depurador**. También puede escribir `Q` en el panel de consola y presionar 		ENTRAR.

### 1.8 Ejercicios

#### Práctica 1

> -reto- **Ejercicio 1** . Ejecuta Windows PowerShell en Windows 2019 Server  el cmdlet adecuado para visualizar la política de ejecución de scripts actual  y cambia las políticas de ejecución de scripts (execution policy) para que se pueda ejecutar cualquier script en PowerShell. Ejecuta el cmdlet correspondiente para mostrar la versión instalada en el sistema.

> -reto- **Ejercicio 2.** Realiza una instalación de PowerShell Core en un contenedor Docker o una máquina virtual con Ubuntu . Ejecuta el cmdlet necesario para mostrar la versión de PowerShell instalada.  
> [Instalacion Powershell Linux] (https://learn.microsoft.com/ca-es/powershell/scripting/install/install-ubuntu?view=powershell-7.4)
> Se obtendrá mejor puntuación en el ejercicio si se realiza la instalación en un contenedor Docker. Tip: [Docker cheat sheet](/aso/assets/img/docker/dockercheatsheet.png)

## 2. Comandos básicos

A continuación, abordaremos los comandos básicos de PowerShell 

-  **Get-Command** : Muestra todos los comandos disponibles

-  **Clear-Host** : Limpia la pantalla


![image-20230715104944576](/aso/assets/img/powershell/image-20230715104944576.png)

### 2.1 Comandos básicos. Alias

> -info- Un **alias** es un nombre alternativo o sobrenombre para un cmdlet o un elemento de un comando, como una funcion, un script, un archivo o un archivo ejecutable. 

Podemos utilizar el alias en lugar de el nombre completo del cmdlet. Por ejemplo, podemos utilizar los comandos  “dir” o “ls” y muchos más. Estos no son mas que alias definidos a otros comandos de Powershell

- **Get-Alias** : Nos devuelve un listado con todos los alias definidos en el sistema

![](/aso/assets/img/powershell/image-20230715105148686.png)

- **Get-Help  \<Comando> :** Muestra ayuda del comando indicado

  ![img](https://lh4.googleusercontent.com/vdl-YzlGFChqGyNfmfPvza78qpBGxjUz8Pw5uc4ndTbIKO90eeQpvZkGvSLly-V9V-Fr66U_7xeog3CA0Pul1c2ev9XAenYdyNoTSMdUAZjc-mJvxZCFCBsxyibjzF4VTAaCnDpIkUwPk5CcuHa0J9fbIw=s2048)

- **Get-Help  \<Comando> -examples:** Muestra ayuda del comando indicado, mostrando ejemplos.

![img](https://lh6.googleusercontent.com/WKSh_5cbRsntD99JZI2aJHzUcNgx5yAvqzfOUZsvD83SXA0y083CBEAYWXwIvnVftLtD8EpmyqDqo1Ow6N_NA2FPoS15gQrOvSSUD3fiJmq0tqdbs7YIteCEEEfCPuCsV56725r7UfARi-EYLLTiKt03vw=s2048)





### 2.3  Comandos de fecha y hora

El comando **Get-Date** nos permite recuperar la fecha y hora actuales.

![img](https://lh5.googleusercontent.com/MK-rKiIKftaAdXM1udwa3RhsKc2lvDnC4zPEQdd5efHfWS2sXlGFkLStL-e6IguOWU3NA5bXs2c37QswEDzCy8g6wKx1J_QZz1OfhliyexElpJNyVacfydwP3qJTgUsAAHj6cBbiUeIysG1ar4kE0V-HKA=s2048)

Si deseamos obtener solo la fecha o la hora usaremos el parámetro **-DisplayHint**

![img](https://lh6.googleusercontent.com/IkyNbYIvrSHRJ0GfoBXNVqyBxsUlwfIave4619wmxhBmCS3nuoSRH2v3AntY7pRme5fSSOjLKJ9adArN-5Yz0QhSx6HvW5ZGFdJdu12LTUJMAM-bOYLw7YfI4B_i7PZrT9oBeid-2XIU2nk9l53yHFawpw=s2048)![img](https://lh3.googleusercontent.com/a4W7xSMe99adzt1HPDZI7dmZ3lbicQOLKna77O1nYTD-e35G_DGH5pSrIHspWUP4rdSSJwSwZSFu9EV-KN_PL1lP3ImVKifIQGM8yqvfN5XOeRQTZm5xwNGiXobpEqZCQVbb1yVXRwMOMK3FAdKpObhOxw=s2048)



Podemos asignar a una variable el resultado del comando Get-Date para almacenar la fecha, hora.

```powershell
$fechaActual = Get-Date
$fechaHora=Get-Date “01/12/2018 11:00 AM” 
$fecha = Get-Date “01/12/2018”
```



### 2.4.  Comandos de archivos y carpetas

**Ruta del directorio actual**

El cmdlet **Get-Location (gl,pwd)** se utiliza para obtener la ruta del directorio actual en el que se está trabajando

```powershell
Get-Location 
```

**Navegar entre directorios**

El cmdlet **Set-Location(sl, cd)** establece la ubicación de trabajo en una ubicación especificada. Esa ubicación puede ser un directorio, subdirectorio, una ubicación del registro o cualquier ruta de acceso del proveedor.

```powershell
Set-Location D:\scripts
```

**Listar archivos en una carpeta** 

El cmdlet **Get-ChildItem (gci, ls,dir) **  en PowerShell se utiliza para obtener una **lista de los elementos que se encuentran en el directorio actual**, incluyendo archivos y subdirectorios.

Puedes usarlo para buscar archivos o carpetas específicos y para explorar el contenido del directorio actual. 

```powershell
Get-ChildItem -Path C:\ -Recurse
```

**Copiar archivos y carpetas**

El cmdlet **Copy-Item (copy, cp, cpi)** nos permite copiar archivos o carpetas. Ejemplo: Copia todos los archivos de la carpeta scripts de la unidad E: a la carpeta Users/Scripts de la unidad C:

```powershell
Copy-Item E:\scripts\* C:\Users\scripts\
```

**Crear una nueva carpeta o archivo**

El cmdlet **New-Item (ni)**  nos permite crear un nuevo archivo o carpeta

Ejemplo: Crea la carpeta scripts en la unidad C:

```powershell
New-Item C:\scripts -ItemType directory
```

Ejemplo: Crea el archivo ejemplo1.ps1 en la carpeta scripts

```powershell
New-Item C:\scripts\ejemplo1.ps1 -ItemType file
```

 

**Borrar un archivo o carpeta**

El cmdlet **Remove-Item (del, erase, rm, ri, rmdir)** nos permite borrar un archivo o carpeta.

Ejemplo: Borra el archivo prueba1.ps1

```powershell
Remove-Item C:\scripts\prueba1.ps1
```

Ejemplo: Borra todos los archivos de la carpeta scripts

```powershell
Remove-Item C:\scripts\*
```

**Mover un archivo o carpeta**

El cmdlet **Move-Item (mi, move, mv)** nos permite mover un archivo de una ubicación a otra.

Ejemplo: Mueve el archivo fichero1.txt a la ruta indicada

```powershell
Move-Item -Path "C:\fichero1.txt" -Destination "C:\copias" 
```

**Renombrar un archivo o carpeta**

El cmdlet **Rename-Item** nos permite cambiar el nombre de archivos y carpetas

Ejemplo: Cambia el nombre de script1 a script2

```powershell
Rename-Item C:\scripts\script1.ps1 script2.ps1
```

**Muestra el contenido de un archivo** 

El cmdlet **Get-Content** nos permite mostrar el contenido de un archivo.

Ejemplo:

```powershell
Get-Content -Path "C:\copias\fichero1.txt"
```

**Verificar la existencia de un archivo o carpeta**

Uno de los principales usos de **Test-Path** es verificar la existencia de un archivo o carpeta. Si obtenemos el valor **true** existe, en caso contrario devuelve el valor **false** 

Ejemplo 1: Devuelve true si script1.ps1 existe

```powershell
Test-Path C:\scripts\script1.ps1
```

Ejemplo 2: Devuelve true si $elem existe y es un directorio

```powershell
Test-Path $elem -PathType container 
```





## 3. Variables y tipos de datos

> -info- Una **variable** es una porción de memoria principal a la que ponemos un nombre que facilite su identificación y manejo. 

Su objetivo consiste en permitir el almacenamiento de un valor en particular para su uso posterior a lo largo del *script*.  Comienzan con el carácter **$**. Los nombres de variable en PowerShell no distinguen **mayúsculas de minúsculas ** .

**Definición Implícita**

```powershell
$hola = "Hola mundo"
```

**Definición Explícita**

```powershell
New-variable hola
$hola = "Hola mundo"
```

- **Get-Variable** : Devuelve un listado completo de las variables que se han definido

![img](https://lh3.googleusercontent.com/mJwXgV3s86CFMH801um9mlUmqbYHkKb_VQbRDvnz6jW5S1tXZdUVUAVgv7XG7bvXxb0NA-Ww4IV7JjxKc3eAcsh2VEqnHIFFjCRsRYKD3uDMmPzhGRZWpacHaLUkn5bdpVXWABM29t7eXsXT4bNMIla2pw=s2048)

### 3.2 Variables predefinidas

**Windows Powershell** dispone de muchas variables predefinidas también llamadas “*variables integradas*” o “*variables internas*“.



| $true      | Valor true.                                                  |
| ---------- | ------------------------------------------------------------ |
| **$false** | Valor false.                                                 |
| **$home**  | El directorio home del usuario actual.                       |
| **$host**  | Información de instalación del host.                         |
| **$error** | Lista de los errores que han ocurrido desde que se ha iniciado WPS. |

PowerShell puede acceder a las **variables de entorno**. Estas variables se exponen a través de una unidad denominada env:.

- Muestra todas las variables de entorno

```powershell
Get-ChildItem env:
```

- Muestra el usuario del sistema

```powershell
$env:USERNAME
```

- Muestra el nombre del equipo

```powershell
$env:COMPUTERNAME
```



### 3.3 Tipos de datos básicos

![img](https://lh5.googleusercontent.com/DrA7lM8sbJRri-68r9yBDKu-C7KT-M2wH21K-PYx7Su6U47UBFGLx-VlD0uDdBQfbQ2sJ3k3CtdsNDI7JfdbMloER6LxjyNi4WNC0DnveEKRGkDmr1r5SN_k0p9xjMTnecwNcSP4D5UshUl7v7JeiHKExw=s2048)D

### 3.4 Comando para obtener el tipo de datos de una variable

```powershell
$numero = 15
$numero.GetType()
```

![img](https://lh4.googleusercontent.com/F9bvPpsRN2QNFG6Bszo5AtxsUtkzl_C8OaF2l2wtw0vWtloUAYHNnWJJs-TvHttpP72Sm9oP_uh-4so-ILLM2iHcgBkvkjIYBg0yUrf11d20UP23dq5RO6p5NVfVbmDVdTIlZAMfet09cYSebq5cikOOhQ=s2048)



> -task-**Pregunta: ¿Qué tipo de dato almacena la variable $a=8.5?**
>
> - [ ] Int
> - [ ] Long
> - [ ] Double
> - [ ] String

>  -toogle-Ver la respuesta correcta
> 
>El tipo de dato almacenado es **double**

### 3.5 Definición de variables

Podemos definir explícitamente el tipo de datos de una variable o asignarle un valor y automáticamente se le asignará el tipo de datos correspondiente.

```powershell
[int] $var = 15
```

es equivalente a

```powershell
$var = 15
```



## 4 Operaciones básicas en Powershell

### 4.1 Entrada y salida de información ###

- **Read-Host** . Guarda en una variable lo que escriba el usuario, **pero como texto **

**Pedir información al usuario**

![img](https://lh3.googleusercontent.com/avW1MyAsuCw4WyLTOY4-JoVJMEdE7vGHkohbMvMOKAXRklhAPMZke70n2GNPZRtvrlgoKWZbAjsKR-aDOUxaMl6-Uz_qYjk9_A6MjwyDPVRzLteHp10SCgOQkMVrt_kLOeXZTRJLdXaU3TIlZpVC2s1dtA=s2048)

- **Write-Host**  .Muestra en pantalla un texto o el contenido de una variable.

**Mostrar información al usuario**

![img](https://lh6.googleusercontent.com/G4BO5_x70Jq_pL4u_TlF6NKL9tIPezgAjTzHblJ1ZKfKvyQuG7-T2PDjjd00Nd4bl1s_v1MMOzoxf3LzEx5NUjN0-SosPAEJ-4pkXSErqPnLR0aeHG8CDo4uHR5W9IwRqED4y3SPxlIH0IpHL6M5ElmY1g=s2048)

```powershell
$edad = Read-Host "Escribe tu edad"
```

> -alert- **Read-Host**  siempre almacena las variables como String (cadena de texto). Esto puede ocasionar problemas cuando estamos intentando almacenar un número.

Para forzar a que sea un entero:

```powershell
[int]$edad = Read-Host "Escribe tu edad"
```

### 4.2 Operadores aritméticos ###



| Operador | Función        | Ejemplo             |
| :------: | -------------- | ------------------- |
|    +     | Suma           | $resultado = $x + 3 |
|    -     | Resta          | $resultado = $x - 3 |
|    *     | Multiplicación | $resultado = $x * 3 |
|    /     | División       | $resultado = $x / 3 |
|    %     | Resto          | $resultado = $x % 3 |

**Operadores aritméticos especiales**

| Operador | Significado                        | Ejemplo | Equivalencia |
| :------: | ---------------------------------- | ------- | ------------ |
|    +=    | Incrementa el valor de la variable | $x+=3   | $x = $x + 3  |
|    -=    | Reduce el valor de la variable     | $x-=3   | $x = $x - 3  |
|    *=    | Multiplica el valor de la variable | $x*=3   | $x = $x * 3  |
|    /=    | Divide el valor de la variable     | $x/=3   | $x = $x / 3  |

### 4.3 **Operadores de comparación**

|   Operador   | Significado                                                  | Ejemplo <br />($true)   |
| :----------: | ------------------------------------------------------------ | ----------------------- |
|     -eq      | Igual                                                        | 1 -eq 1                 |
|     -ieq     | Igual <br />Con valores de tipo texto, no tendrá en cuenta la diferencia entre mayúsculas y minúsculas. | "Hola" -ieq "HOLA"      |
|     -ceq     | Igual<br />Con valores de tipo texto, tendrá en cuenta la diferencia entre mayúsculas y minúsculas. | "HOLA" -ceq "HOLA"      |
|     -ne      | Diferente                                                    | 3 -ne 5                 |
|     -lt      | Menor                                                        | 3 -lt 5                 |
|     -le      | Menor o igual                                                | 5 -le 5<br />3 -le 5    |
|     -gt      | Mayor                                                        | 5 -gt 3                 |
|     -ge      | Mayor o igual                                                | 5 -ge 5<br />5 -ge 3    |
|    -like     | Es como                                                      | "Fermín" -like "Fer*"   |
|   -notlike   | No es como                                                   | "Fermín" -notlike "Fa*" |
|  -contains   | Contiene                                                     | 9,5,2 -contains 5       |
| -notcontains | No contiene                                                  | 9,5,2 -notcontains 1    |



------

### 4.4 Operadores lógicos

| Operador | Significado                                             | Ejemplo                             |
| -------- | ------------------------------------------------------- | ----------------------------------- |
| -and     | AND lógico. TRUE cuando las dos expresiones son ciertas | (1 -eq 1) -and (1 -eq 2)<br />False |
| -or      | OR lógico. TRUE cuando alguna expresión es cierta       | (1 -eq 1) -or (1 -eq 2) <br />True  |
| -xor     | OR exclusivo. TRUE cuando sólo una expresión es cierta  | (1 -eq 1) -xor (2 -eq 2)<br />False |
| -not     | Negación lógica. Niega la expresión                     | -not (1 -eq 1)<br />False           |
| !        | Idéntico a -not                                         | !(1 -eq 1)<br />False               |





### 4.5 Operaciones con cadenas

- Una de las operaciones más habituales es la **concatenación (+)**, que nos permite unir dos o más variables.

```powershell
$nombre="Pepe "
$apellidos="Garcia Sanchez"
$nombreCompleto=$nombre+$apellidos
```

- El método **IndexOf** nos permite buscar un determinado texto.

  ![image-20230718093834882](/aso/assets/img/powershell/image-20230718093834882.png)

### 4.6 Ejercicios

#### Práctica 2

> -reto- **Ejercicio 1.** Crea un script en lenguaje PowerShell que muestre al usuario los siguientes mensajes:
>
> - Hola *nombre de usuario*
> - Tu directorio de trabajo es *directorio*
> - Perteneces al dominio *Nombre_dominio*
> - Tu equipo se llama *Nombre_equipo.*

> -reto- **Ejercicio2**.  Crea un script en PowerShell que pida dos números al usuario e imprima por pantalla su suma, la resta, la multiplicación, división y resto.

> -reto- **Ejercicio3**. Crea un script en PowerShell que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla el salario que debemos pagarle.

## 5. Estructuras condicionales

### Uso de la orden If, Else, ElseIf

```powershell
If(condicion) { Bloque de codigo 1}
Else {Bloque de codigo 2}
```

- C*ondición* se refiere a una expresión lógica. Es decir, que al evaluarla se obtendrá un valor **$true** o **$false**.

- El bloque de código será un conjunto de instrucciones que sólo se ejecutarán cuando la condición ofrezca el valor **$true**. 

**Bloque If** 

```powershell
If ($x  -gt 50) {
	Write-Host "La variable x es mayor que 50"
}
```

**Bloque if-else**

```powershell
If ($x -gt 50){
	Write-Host "La variable x es mayor que 50"
}Else {
	Write-Host "La variable es menor o igual que 50"
}
```

**Bloque if-ElseIf** 

```powershell
If ($x -gt 50){
	Write-Host "La variable x es mayor que 50"
}ElseIf ($x -eq 50) {
	Write-Host "La variable x es igual a 50"
}Else {
	Write_host "La variable es es menor que 50"
}
```



### Uso de la orden switch

La instrucción **switch** permite organizar bloques de código de forma que se ejecutan cuando se cumpla la condición.

```powershell
switch(valor de prueba) {
Patron 1 {Bloque de codigo 1}
Patron 2 {Bloque de codigo 2}
Patron n {Bloque de codigo n}
default {Bloque por defecto}
}
```
**Ejemplo 1:**

```powershell
[Int]$x = Read-Host "Introduce un valor"
#Bloque Switch
switch ($x) { 
	1 {
		#Bloque de instrucciones cuando $x es igual a 1
		Write-Host "Has introducido el valor 1"
	}
	2 {
		#Bloque de instrucciones cuando $x es igual a 2
		Write-Host "Has introducido el valor 2"
	}
	3 {
		#Bloque de instrucciones cuando $x es igual a 3
		Write-Host "Has introducido el valor 3"
	}
	default {
		#Cualquier otro valor
		Write-Host "Has introducido cualquier otro valor"
	}
}
```

**Ejemplo 2:**

```powershell
[int]$nota = Read-Host "Escribe una nota"
switch ($nota) {
	{$_ -lt 5}						{Write-Host "Suspenso"}
	{($_ -ge 5) -and ($_ -le 10)}	{Write-Host "Aprobado"}
	{$_ -in 1..4}					{Write-Host "Insuficiente"}
	5								{Write-Host "Suficiente"}
	6								{Write-Host "Bien"}
	{$_ -in 7,8}					{Write-Host "Notable"}
	{$_ -in 9,10}					{Write-Host "Sobresaliente"}
	default							{Write-Host "No conozco esa nota"}
}
```

### Ejercicios

#### Práctica 3


> -reto- **Ejercicio 1**. Crea un script que solicite un número al usuario. El programa debe indicar si el número es impar o par.

> -reto- **Ejercicio2**. Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

> -reto- **Ejercicio 3.** Crea un script en el que se pida dos números enteros al usuario. El script debe indicar si el primer número es mayor, menor o igual que el otro.

> -reto- **Ejercicio 4**. Crea una calculadora muy sencilla, en la que se preguntará al usuario dos números y que operación desea realizar.
>
> Ejemplo:
>
> **************** CALCULADORA ********************
>
> 1. Sumar 
> 2. Restar 
> 3. Multiplicar 
> 4. Dividir
>
> ¿Qué desea hacer?Elige una opción:

> -reto- **Ejercicio 5**. Crea un script en el que pidas un fichero o carpeta por teclado y te diga si existe o no. 

> -reto- **Ejercicio 6.**  Crea un script   que diga si lo que se pasa por teclado es un directorio. En ese caso sacará una lista con los archivos que contiene y subdirectorios. Debes utilizar el parámetro Recurse.

> -reto- **Ejercicio 7.**  Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas. 

> -reto- **Ejercicio 8.**  Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto.
> Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

> -reto- **Ejercicio 9.** Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes: 

| Renta | Tipo Impositivo |
| ----- | -----|
| Menos de 10000€ | 5% |
| Entre 10000€ y 20000€ | 15% |
| Entre 20000€ y 35000€ | 20% |
| Entre 35000€ y 60000€ | 30% |
| Más de 60000€ | 45% |

 Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

> -reto- **Ejercicio 10.** En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel. 

| Nivel | Puntuación |
| ----- | ------|
| Inaceptable | 	0.0 |
| Aceptable |	0.4 |
| Meritorio |	0.6 o más |

> Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.

> -reto- **Ejercicio 11.** Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

> -reto- **Ejercicio 12.** La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación. 
>
> - Ingredientes vegetarianos: Pimiento y tofu.
> - Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
> Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

Los enunciados de estos ejercicos están extraidos de la siguiente página web:

https://aprendeconalf.es/docencia/python/ejercicios/condicionales/

## 6. Estructuras repetitivas

Todos los lenguajes de programación necesitan un método que les permita repetir un bloque de instrucciones. En PowerShell puedes utilizar:

- **do while**: repite mientras la condición vale $true

- **while**: repite mientras la condición vale $true

- **do until**: repite hasta que la condición vale $true

- **for:** repite durante un nº de veces

- **foreach:** repite una vez para cada elemento de la lista

  

### 6.1 La estructura do while

```powershell
do { 
	Bloque de codigo
}
while (condicion)
```
**Ejemplo:**

```powershell
$a = 1
do 
{
	Write-Host $a
	$a++
}while ($a -le 5)

```
**Resultado por pantalla:** 
1
2
3
4
5

### 6.2 La estructura while

```powershell
while (condicion){
	Bloque de codigo
}
```

**Ejemplo:**

```powershell
$a = 1
while ($a -le 5)
{
	Write-Host $a
	$a++
}
```

**Resultado por pantalla:**

1
2
3
4
5

### 6.3 La estructura do until

```powershell
do {
	Bloque de codigo
}
until (condicion)
```

**Ejemplo:**

```powershell
$a = 1
do
{
	Write-Host $a
	$a++
} until ($a -gt 5)
```

**Resultado por pantalla:**

1
2
3
4
5

### 6.4 La estructura for

```powershell
for (inicializacion; condicion; incremento)
{
	Bloque de codigo
}
```

Ejemplo:

```powershell
for ($a = 1; $a -le 5; $a++)
{
	Write-Host $a
} 
```

**Resultado por pantalla:**

1
2
3
4
5

### 6.5 La estructura foreach

La estructura **foreach** funciona en cualquier situación donde pueda obtenerse una lista de elementos.

```powershell
foreach (elemento in coleccion)
{
	Bloque de codigo
}
```

Ejemplo:

```powershell
foreach ($a in 1,2,3,4,5)
{
	Write-Host $a
} 
```

**Resultado por pantalla:**

1
2
3
4
5

**Ejemplo:**

```powershell
$ruta = "C:\Windows\System32"
$texto = Read-Host "Escribe el texto a buscar"
foreach ($archivo in Get-ChildItem $ruta) {
	if($archivo.Name.IndexOf($texto) -ge 0) {
		Write-Host $archivo.Name
	}
}
```

![image-20230720204431719](/aso/assets/img/powershell/image-20230720204431719.png)

### 6.6 Ejercicios

#### Práctica 4

> -reto- **Ejercicio1**. Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

> -reto- **Ejercicio 2**. Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

> -reto- **Ejercicio3**. Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

> -reto- **Ejercicio4** Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

> -reto- **Ejercicio 5**. Crea un script  que utilice for para mostrar la tabla de multiplicar de un número que se solicita al usuario. 

> -reto- **Ejercicio 6.**  Crea un script en lenguaje PowerShell que sea un juego de adivinar un número de 0 a 100. El número se pondrá fijo al principio del procedimiento. Se irá preguntando al usuario números y se dirá si es mayor o menor en caso de no adivinar el numero. Al adivinar el número mostrará un mensaje de enhorabuena y se detendrá el juego.

> -reto- **Ejercicio 7** Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
>
> ![image-20230924192557853](/aso/assets/img/powershell/image-20230924192557853.png) 

> -reto- **Ejercicio 8** Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
>
> ![image-20230926115734084](/aso/assets/img/powershell/image-20230926115734084.png)

> -reto- **Ejercicio 9** Escribir un programa que almacene la cadena de caracteres `contraseña` en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

> -reto- **Ejercicio 10**. Crea un script  que muestre un menú con las siguientes opciones: 
>
> a) Crear una carpeta 
>
> b) Crear un fichero nuevo 
>
> c) Cambiar el nombre de un fichero o carpeta 
>
> d) Borrar un archivo o carpeta 
>
> e) Verificar si existe un fichero o carpeta 
>
> f) Mostrar el contenido de un directorio. 
>
> g) Mostar la fecha y hora actuales 
>
> x) Salir 
>
> El menú se mostrará hasta que el usuario seleccione la opción Salir. Todos los datos que necesite el usuario se pedirán por teclado al usuario. 

## 7 Importación de datos ##

1. **Importación de un archivo de texto**

Para importar los datos de un fichero .txt usaremos el comando **Get-Content** para almacenar los datos en una variable.

```powershell
$ciudades = Get-Content ciudades.txt
foreach($ciudad in $ciudades)
{
	Write-Host $ciudad
}
```

![img](https://lh3.googleusercontent.com/TtRQwDNRx_itz1YhGKWjOxzqRlFjLfDpntT3nXOGIk3msPmFo7ovMJk_SC6dRgQ7pGEunsFXNXQc-3yR994285QmRKEMKLsKkiCd5deFoy_tIy2Uh7oCKqY2UqMDcFnAqkR6x238xNMtaSTLYn5EqbWwpg=s2048)

**Importación de un archivo CSV**

Para importar los datos de un fichero csv usaremos el método **Import-CSV** para almacenar los datos en una variable.

```powershell
$ordenadores = import-CSV computers.csv
foreach($pc in $ordenadores) {
	Write-Host "Equipo: $($pc.Nombre) $($pc.IP) $($pc.Oficina)"
}
```



![img](https://lh4.googleusercontent.com/oWQbVFqzpSUTpMwWeFuHDdnleWjJXb_DVh7yepZPq_T6YKo8Emfwk_eGLgxklv4uUl7EiwEvKOAFAI_yZ-ZrS82KiZul1bZ3HpqT1Wj3XPFrP15CK2z04zc0D_mpfJWwRiu0tvlt1pcJpYah8gFgsqow8g=s2048)

![img](https://lh5.googleusercontent.com/lv4H5XO8V1iKYKGhpxDfHFPQC9PW7MxtQlXsnybhZbfyNBEQP4DnQDe9ZRsX0a43CKL8cmIfx_zwlrGD7UsBIiOC0HcvDOQMWQwVCFLgnTMV8-m4DNttOY5VANeJGEKg_jIsbOFsmpWtwmod-fGRUo1wNQ=s2048)



**Import-CSV**: con powershell podemos importar cualquier archivo CSV. Por defecto el delimitador es la coma, pero se puede indicar otro.La cabecera del archivo pasan a ser los nombres de las propiedades pero también se pueden indicar otros.

![img](https://lh6.googleusercontent.com/uS2-CyRXvA04jp9IZbw9dbrctMhrR-MFsKJXddh7A_wnKKnewzJq4_AXdaaPu292f2PKmuVm1AXFsaSwVTZHEKF1Y0Hysnd_0BQmwbo4BiocpBOhAljub2NdZSk7F-L25mF4WUe3079-Bty2Lu-oH52RjA=s2048)

```powershell
$empleados = Import-Csv C:\scripts\empleados.csv -Delimiter ";"

foreach ($em in $empleados)
{
 	Write-Host "Usuario: $($em.nombre) $($em.apellido)"
}
```

## 8. Funciones ##

Una función no es más que un conjunto de instrucciones a las que le damos un nombre. 

Las funciones tienen varias ventajas en la programación:

1. **Reutilización de código**: Puedes definir una función una vez y luego llamarla en múltiples partes de tu programa. Esto evita la necesidad de repetir el mismo código una y otra vez.
2. **Modularidad**: Las funciones permiten dividir un programa grande y complejo en partes más pequeñas y manejables. Cada función se encarga de una tarea específica, lo que facilita la comprensión y mantenimiento del código.
3. **Abstracción**: Una función te permite encapsular un conjunto de operaciones en un nombre significativo. Esto hace que el código sea más legible y fácil de entender.
4. **Facilita la depuración**: Al dividir un programa en funciones más pequeñas, es más fácil identificar y corregir errores o fallos en el código.
5. **Permite la organización**: Al utilizar funciones, puedes organizar tu código de manera lógica y estructurada, lo que facilita su comprensión y mantenimiento.
6. **Mejora la colaboración**: Al trabajar en equipo, las funciones permiten a diferentes programadores trabajar en diferentes partes del código al mismo tiempo sin interferir con el trabajo de los demás.

**Sintaxis**							

```
Function <nombre> { 

<bloque de código> 

}
```

**Ejemplo 1** 



En PowerShell, hay dos formas de definir parámetros en una función:

1. Usando la palabra clave `param`:

   ```powershell
   Function Sumar {
       param (
           [int]$x,
           [int]$y
       )
       $sumar = $x + $y
       Write-Host "La respuesta es $sumar"
   }
   ```

   

2. Especificando los parámetros directamente en la definición de la función:

```powershell
Function Sumar ($x, $y) {
	$sumar = $x + $y
	Write-Host "La respuesta es $sumar"
}
```

Para usar esta función, simplemente llama a `Sumar` y proporciona los valores para `$x` y `$y`. Por ejemplo:

```powershell
Sumar 3 5
```

Ambas formas son correctas y válidas en PowerShell. Sin embargo, la primera opción (`param`) proporciona una mayor claridad en cuanto a la declaración de los tipos de datos esperados para cada parámetro. Esto puede hacer que tu código sea más legible y menos propenso a errores si los tipos de datos incorrectos se pasan a la función.

**Ejemplo 2** 

```powershell
function TestPing($Address) {
    $Result=Test-Connection -ComputerName $Address -ErrorAction SilentlyContinue

    if ($? -eq $true) {

            write-output "ICMP Test to ${Address}: OK"

    }else{

            write-output "ICMP Test to ${Address}: Error"
    }
}
```

En nuestro ejemplo, creamos una función denominada **TestPing** para probar la conectividad a una dirección variable.

Para utilizar la función, debemos realizar la llamada:

```powershell
TestPing  "8.8.8.8" 
```

### Ejercicios

#### Práctica 5

En esta práctica vas a reescribir algunos de los scripts realizados anteriormente, pero haciendo uso de las funciones.

> -reto- **Ejercicio 1**  Crea una calculadora muy sencilla, en la que se preguntará al usuario dos números y que operación desea realizar.
>
> Ejemplo:
>
> **************** CALCULADORA ********************
>
> 1. Sumar 
> 2. Restar 
> 3. Multiplicar 
> 4. Dividir
> 5.  Salir
>
> ¿Qué desea hacer?Elige una opción: 
>
> Debes crear las funciones Sumar, Restar, Multiplicar y Dividir. Cada una de estas funciones tendrá dos parámetros.
>
> 



> -reto- **Ejercicio 2** Haciendo uso de la estructura repetitiva foreach, debes leer todos los datos del archivo [usuarios.csv](/aso/assets/usuarios.csv) e imprimir el nombre, apellidos y grupo del usuario

