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

- **Get-Help <Comando> :** Muestra ayuda del comando indicado

  ![img](https://lh4.googleusercontent.com/vdl-YzlGFChqGyNfmfPvza78qpBGxjUz8Pw5uc4ndTbIKO90eeQpvZkGvSLly-V9V-Fr66U_7xeog3CA0Pul1c2ev9XAenYdyNoTSMdUAZjc-mJvxZCFCBsxyibjzF4VTAaCnDpIkUwPk5CcuHa0J9fbIw=s2048)

- **Get-Help <Comando> -examples:** Muestra ayuda del comando indicado, mostrando ejemplos.

![img](https://lh6.googleusercontent.com/WKSh_5cbRsntD99JZI2aJHzUcNgx5yAvqzfOUZsvD83SXA0y083CBEAYWXwIvnVftLtD8EpmyqDqo1Ow6N_NA2FPoS15gQrOvSSUD3fiJmq0tqdbs7YIteCEEEfCPuCsV56725r7UfARi-EYLLTiKt03vw=s2048)



## 3. Comentarios, variables y tipos de datos

Los comentarios en PowerShell se escriben utilizando el símbolo de **almohadilla** (#).

▸ Comentar una línea.

 **#**Este es un comentario.

▸ Comentar un bloque

**<#**

Esto es un comentario

de varias líneas

**#>**

Una **variable** es una porción de memoria principal a la que ponemos un nombre que facilite su identificación y manejo. Su objetivo consiste en permitir el almacenamiento de un valor en particular para su uso posterior a lo largo del *script*. 

Comienzan con el carácter **$** 

**Definición Implícita**

```
$hola = “Hola mundo”
```

**Definición Explícita**

```
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

