---
typora-copy-images-to: ../assets/img/powershell
typora-root-url: ../../
layout: post
title: Powershell
categories: parte1
conToc: true
permalink: powershell
---
## Apuntes Powershell



## 1. Introducción

**PowerShell** es un intérprete de línea de comandos orientado a objetos. Fue diseñado para su uso por parte de administradores, con el propósito de automatizar tareas o realizarlas de forma más controlada.

[Manual de PowerShell 5.1 de Microsoft](https://docs.microsoft.com/es-es/powershell/scripting/overview?view=powershell-5.1)

Tenemos dos opciones a la hora de ejecutar PowerShell:
1) Entorno gráfico: PowerShell ISE (del inglés, Integrated Scripting Environment).
2) Entorno comando: Windows Powershell

![image-20230714211446318](/aso/assets/img/powershell/image-20230714211446318.png)



## 2. Comandos básicos

- **$psversiontable** : Muestra la versión de PowerShell instalada.

![image-20230715104849336](/aso/assets/img/powershell/image-20230715104849336.png)

-  **Get-Command** : Muestra todos los comandos disponibles

- **Clear-Host** : Limpia la pantalla


![image-20230715104944576](/aso/assets/img/powershell/image-20230715104944576.png)

### 2.1 Comandos básicos. Alias

Un **alias** es un nombre alternativo o sobrenombre para un cmdlet o un elemento de un comando, como una funcion, un script, un archivo o un archivo ejecutable. El tema es que podemos utilizar el alias en lugar de el nombre completo del cmdlet. Podemos utilizar en **Windows Powershell** comandos como “dir” o “ls” y muchos más. Estos no son mas que alias definidos a otros comandos de Powershell

- **Get-Alias** : Nos devuelve un listado con todos los alias definidos en el sistema

![](/aso/assets/img/powershell/image-20230715105148686.png)

- **Get-Help  \<Comando> :** Muestra ayuda del comando indicado

  ![img](https://lh4.googleusercontent.com/vdl-YzlGFChqGyNfmfPvza78qpBGxjUz8Pw5uc4ndTbIKO90eeQpvZkGvSLly-V9V-Fr66U_7xeog3CA0Pul1c2ev9XAenYdyNoTSMdUAZjc-mJvxZCFCBsxyibjzF4VTAaCnDpIkUwPk5CcuHa0J9fbIw=s2048)

- **Get-Help  \<Comando> -examples:** Muestra ayuda del comando indicado, mostrando ejemplos.

![img](https://lh6.googleusercontent.com/WKSh_5cbRsntD99JZI2aJHzUcNgx5yAvqzfOUZsvD83SXA0y083CBEAYWXwIvnVftLtD8EpmyqDqo1Ow6N_NA2FPoS15gQrOvSSUD3fiJmq0tqdbs7YIteCEEEfCPuCsV56725r7UfARi-EYLLTiKt03vw=s2048)



## 3. Comentarios, variables y tipos de datos

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

Una **variable** es una porción de memoria principal a la que ponemos un nombre que facilite su identificación y manejo. Su objetivo consiste en permitir el almacenamiento de un valor en particular para su uso posterior a lo largo del *script*. 

Comienzan con el carácter **$** 

**Definición Implícita**

```powershell
$hola = “Hola mundo”
```

**Definición Explícita**

```powershell
New-variable hola
$hola = “Hola mundo”
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

![img](https://lh5.googleusercontent.com/DrA7lM8sbJRri-68r9yBDKu-C7KT-M2wH21K-PYx7Su6U47UBFGLx-VlD0uDdBQfbQ2sJ3k3CtdsNDI7JfdbMloER6LxjyNi4WNC0DnveEKRGkDmr1r5SN_k0p9xjMTnecwNcSP4D5UshUl7v7JeiHKExw=s2048)

### 3.4 Comando para obtener el tipo de datos de una variable

```powershell
$numero = 15
$numero.GetType()
```

![img](https://lh4.googleusercontent.com/F9bvPpsRN2QNFG6Bszo5AtxsUtkzl_C8OaF2l2wtw0vWtloUAYHNnWJJs-TvHttpP72Sm9oP_uh-4so-ILLM2iHcgBkvkjIYBg0yUrf11d20UP23dq5RO6p5NVfVbmDVdTIlZAMfet09cYSebq5cikOOhQ=s2048)

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

- **Read-Host** => Guarda en una variable lo que escriba el usuario, **pero como texto **

**Pedir información al usuario**

![img](https://lh3.googleusercontent.com/avW1MyAsuCw4WyLTOY4-JoVJMEdE7vGHkohbMvMOKAXRklhAPMZke70n2GNPZRtvrlgoKWZbAjsKR-aDOUxaMl6-Uz_qYjk9_A6MjwyDPVRzLteHp10SCgOQkMVrt_kLOeXZTRJLdXaU3TIlZpVC2s1dtA=s2048)

- **Write-Host** => Muestra en pantalla un texto o el contenido de una variable.

**Mostrar información al usuario**

![img](https://lh6.googleusercontent.com/G4BO5_x70Jq_pL4u_TlF6NKL9tIPezgAjTzHblJ1ZKfKvyQuG7-T2PDjjd00Nd4bl1s_v1MMOzoxf3LzEx5NUjN0-SosPAEJ-4pkXSErqPnLR0aeHG8CDo4uHR5W9IwRqED4y3SPxlIH0IpHL6M5ElmY1g=s2048)

```powershell
$edad = Read-Host “Escribe tu edad”
```

**Read-Host siempre almacena las variables como String.**

Para forzar a que sea un entero:

```powershell
[int]$edad = **Read-Host** “Escribe tu edad”
```



#### Operadores aritméticos



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

**Operadores de comparación**

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



#### Operaciones con cadenas

- Una de las operaciones más habituales es la **concatenación (+)**, que nos permite unir dos o más variables.

```powershell
$nombre=”Pepe ”
$apellidos=”Garcia Sanchez”
$nombreCompleto=$nombre+$apellidos
```

- El método **IndexOf** nos permite buscar un determinado texto.

  ![image-20230718093834882](/aso/assets/img/powershell/image-20230718093834882.png)
