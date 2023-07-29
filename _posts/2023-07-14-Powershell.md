---
typora-copy-images-to: ../assets/img/powershell
typora-root-url: ../../
layout: post
title: Unidad 1. Scripting en Windows. PowerShell
categories: scripts
conToc: true
permalink: powershell
---


## 1. Introducción

**PowerShell** es un intérprete de línea de comandos orientado a objetos. Fue diseñado para su uso por parte de administradores, con el propósito de automatizar tareas o realizarlas de forma más controlada. 

> -info- Las órdenes incluidas en Powershell son muchas y reciben el nombre de **cmdlets** .

[Manual de PowerShell 5.1 de Microsoft](https://docs.microsoft.com/es-es/powershell/scripting/overview?view=powershell-5.1)

Tenemos dos opciones a la hora de ejecutar PowerShell:
1) Entorno gráfico: PowerShell ISE (del inglés, Integrated Scripting Environment).
2) Entorno comando: Windows Powershell

![image-20230714211446318](/aso/assets/img/powershell/image-20230714211446318.png)



### Execution Policy ###

La política de ejecución de PowerShell es una característica de seguridad destinada a controlar las condiciones bajo las cuales PowerShell carga los archivos de configuración y ejecuta scripts. Esta característica ayuda a controlar la ejecución de scripts maliciosos.

Tenemos las siguientes políticas de ejecución:

- **Unrestricted**: Es la política menos restrictiva. Los usuarios pueden ejecutar todos los scripts.

- **Bypass**: Al igual que unrestricted, esta política de ejecución no bloquea nada. 

- **Undefined**: PowerShell elimina cualquier política de ejecución asignada.

- **RemoteSigned**: Esta política, establece que todos los scripts remotos deben estar firmados.

- **AllSigned**: Todos los scripts deben esta firmados.

- **Restricted**: Es la polícita más restrictiva. Si se establece esta polícita no se puede ejecutar ningún script.

  

## 2. Comandos básicos

- **$psversiontable** : Muestra la versión de PowerShell instalada.

![image-20230715104849336](/aso/assets/img/powershell/image-20230715104849336.png)

-  **Get-Command** : Muestra todos los comandos disponibles

- **Clear-Host** : Limpia la pantalla


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





## 3.  Comandos de fecha y hora

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



## 4.  Comandos de archivos y carpetas

**Get-Location (pwd), Set-Location (cd) y Get-ChildItem (ls)**



**Copiar archivos y carpetas**

El comando **Copy-Item** nos permite copiar archivos o carpetas. Ejemplo: Copia todos los archivos de la carpeta scripts de la unidad E: a la carpeta Users/Scripts de la unidad C:

```powershell
Copy-Item E:\scripts\* C:\Users\scripts\
```

**Crear una nueva carpeta o archivo**

El comando **New-Item** nos permite crear un nuevo archivo o carpeta

Ejemplo: Crea la carpeta scripts en la unidad C:

```powershell
New-Item C:\scripts -ItemType directory
```

Ejemplo: Crea el archivo ejemplo1.ps1 en la carpeta scripts

```powershell
New-Item C:\scripts\ejemplo1.ps1 -ItemType file
```

 

**Borrar un archivo o carpeta**

El comando **Remove-Item** nos permite borrar un archivo o carpeta.

Ejemplo: Borra el archivo prueba1.ps1

```powershell
Remove-Item C:\scripts\prueba1.ps1
```

Ejemplo: Borra todos los archivos de la carpeta scripts

```powershell
Remove-Item C:\scripts\*
```

**Mover un archivo o carpeta**

El comando **Move-Item** nos permite mover un archivo de una ubicación a otra.

Ejemplo: Borra el archivo prueba1.ps1

Remove-Item C:\scripts\prueba1.ps1

Ejemplo: Borra todos los archivos de la carpeta scripts

Remove-Item C:\scripts\*

**Renombrar un archivo o carpeta**

El comando **Rename-Item** nos permite cambiar el nombre de archivos y carpetas

Ejemplo: Cambia el nombre de script1 a script2

Rename-Item C:\scripts\script1.ps1 script2.ps1

**Verificar la existencia de un archivo o carpeta**

Uno de los principales usos de **Test-Path** es verificar la existencia de un archivo o carpeta. Si obtenemos el valor **true** existe, en caso contrario devuelve el valor **false** 

Ejemplo: Devuelve true si script1.ps1 existe

```powershell
Test-Path C:\scripts\script1.ps1
```

**Verificar la existencia de un archivo o carpeta**

Uno de los principales usos de **Test-Path** es verificar la existencia de un archivo o carpeta. Si obtenemos el valor **true** existe, en caso contrario devuelve el valor **false** 

Ejemplo 1: Devuelve true si script1.ps1 existe

```powershell
Test-Path C:\scripts\script1.ps1
```

Ejemplo 2: Devuelve true si $elem existe y es un directorio

Test-Path $elem -PathType container 





## 5. Comentarios, variables y tipos de datos



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

> -info- Una **variable** es una porción de memoria principal a la que ponemos un nombre que facilite su identificación y manejo. 

Su objetivo consiste en permitir el almacenamiento de un valor en particular para su uso posterior a lo largo del *script*.  Comienzan con el carácter **$** 

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

### 5.2 Variables predefinidas

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



### 5.3 Tipos de datos básicos

![img](https://lh5.googleusercontent.com/DrA7lM8sbJRri-68r9yBDKu-C7KT-M2wH21K-PYx7Su6U47UBFGLx-VlD0uDdBQfbQ2sJ3k3CtdsNDI7JfdbMloER6LxjyNi4WNC0DnveEKRGkDmr1r5SN_k0p9xjMTnecwNcSP4D5UshUl7v7JeiHKExw=s2048)

### 5.4 Comando para obtener el tipo de datos de una variable

```powershell
$numero = 15
$numero.GetType()
```

![img](https://lh4.googleusercontent.com/F9bvPpsRN2QNFG6Bszo5AtxsUtkzl_C8OaF2l2wtw0vWtloUAYHNnWJJs-TvHttpP72Sm9oP_uh-4so-ILLM2iHcgBkvkjIYBg0yUrf11d20UP23dq5RO6p5NVfVbmDVdTIlZAMfet09cYSebq5cikOOhQ=s2048)

### 5.5 Definición de variables

Podemos definir explícitamente el tipo de datos de una variable o asignarle un valor y automáticamente se le asignará el tipo de datos correspondiente.

```powershell
[int] $var = 15
```

es equivalente a

```powershell
$var = 15
```



## 6 Operaciones básicas en Powershell

### 6.1 Entrada y salida de información ###

- **Read-Host** . Guarda en una variable lo que escriba el usuario, **pero como texto **

**Pedir información al usuario**

![img](https://lh3.googleusercontent.com/avW1MyAsuCw4WyLTOY4-JoVJMEdE7vGHkohbMvMOKAXRklhAPMZke70n2GNPZRtvrlgoKWZbAjsKR-aDOUxaMl6-Uz_qYjk9_A6MjwyDPVRzLteHp10SCgOQkMVrt_kLOeXZTRJLdXaU3TIlZpVC2s1dtA=s2048)

- **Write-Host**  .Muestra en pantalla un texto o el contenido de una variable.

**Mostrar información al usuario**

![img](https://lh6.googleusercontent.com/G4BO5_x70Jq_pL4u_TlF6NKL9tIPezgAjTzHblJ1ZKfKvyQuG7-T2PDjjd00Nd4bl1s_v1MMOzoxf3LzEx5NUjN0-SosPAEJ-4pkXSErqPnLR0aeHG8CDo4uHR5W9IwRqED4y3SPxlIH0IpHL6M5ElmY1g=s2048)

```powershell
$edad = Read-Host "Escribe tu edad"
```

> -alert- Read-Host  siempre almacena las variables como String (cadena de texto). Esto puede ocasionar problemas cuando estamos intentando almacenar un número.

Para forzar a que sea un entero:

```powershell
[int]$edad = Read-Host "Escribe tu edad"
```

### 6.2 Operadores aritméticos ###



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

### 6.3 **Operadores de comparación**

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

### 6.4 Operadores lógicos

| Operador | Significado                                             | Ejemplo                             |
| -------- | ------------------------------------------------------- | ----------------------------------- |
| -and     | AND lógico. TRUE cuando las dos expresiones son ciertas | (1 -eq 1) -and (1 -eq 2)<br />False |
| -or      | OR lógico. TRUE cuando alguna expresión es cierta       | (1 -eq 1) -or (1 -eq 2) <br />True  |
| -xor     | OR exclusivo. TRUE cuando sólo una expresión es cierta  | (1 -eq 1) -xor (2 -eq 2)<br />False |
| -not     | Negación lógica. Niega la expresión                     | -not (1 -eq 1)<br />False           |
| !        | Idéntico a -not                                         | !(1 -eq 1)<br />False               |





### 6.5 Operaciones con cadenas

- Una de las operaciones más habituales es la **concatenación (+)**, que nos permite unir dos o más variables.

```powershell
$nombre=”Pepe ”
$apellidos=”Garcia Sanchez”
$nombreCompleto=$nombre+$apellidos
```

- El método **IndexOf** nos permite buscar un determinado texto.

  ![image-20230718093834882](/aso/assets/img/powershell/image-20230718093834882.png)

## 7. Estructuras condicionales

### Uso de la orden if

```powershell
if(condicion) { Bloque de codigo 1}
else {Bloque de codigo 2}
```

- C*ondición* se refiere a una expresión lógica. Es decir, que al evaluarla se obtendrá un valor **$true** o **$false**.

- El bloque de código será un conjunto de instrucciones que sólo se ejecutarán cuando la condición ofrezca el valor **$true**. 

  

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



## 8. Estructuras repetitivas

Todos los lenguajes de programación necesitan un método que les permita repetir un bloque de instrucciones. En PowerShell puedes utilizar:

- **do while**: repite mientras la condición vale $true

- **while**: repite mientras la condición vale $true

- **do until**: repite hasta que la condición vale $true

- **for:** repite durante un nº de veces

- **foreach:** repite una vez para cada elemento de la lista

  

### 8.1 La estructura do while

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

### 8.2 La estructura while

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

### 8.3 La estructura do until

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

### 8.4 La estructura for

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

### 8.5 La estructura foreach

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





## 9 Importación de datos ##

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
$empleados = Import-Csv C:\scripts\empleados.csv -Delimiter “;”

foreach ($em in $empleados)
{
 	Write-Host “Usuario: $($em.nombre) $($em.apellido)”
}
```

## 10. Funciones ##

Una función no es más que un conjunto de instrucciones a las que le damos un nombre. 

**Sintaxis**							

```
Function <nombre> { 

<bloque de código> 

}
```

**Ejemplo**

```powershell
Function Sumar ($x, $y) {
	$sumar = $x + $y
	Write-Host "La respuesta es $sumar"
}
```



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

TestPing (‘8.8.8.8’)
