---
typora-copy-images-to: ../assets/img/linux
typora-root-url: ../../
layout: post
title: Linux - Bash
categories: linux
conToc: true
permalink: linux-bash
---
**CFGS Administración de Sistemas Informáticos y Redes**

Material elaborado por Ángela Bañuls Serrano

# Manual de Shell Script

**Índice**

1. [Introducción](#id1)
2. [Nuestro primer Script "Hola mundo"](#id2)
3. [Variables](#id3)
4. [Entrada de datos por el usuario](#id4)
5. [Comentarios](#id5)
6. [Parámetros](#id6)
7. [Arrays](#id7)
8. [Matemáticas en bash](#id8)
9. [Evaluación de expresiones](#id9)
    1. [Expresiones de archivos](#id91)
    2. [Expresiones de cadenas](#id92)
    3. [Expresiones numéricas](#id93)
    4. [Expresiones lógicas](#id94)
10. [Condicionales](#id10)
11. [Bucles](#id11)
    1. [Bucles con for](#id111)
    2. [Bucles con while](#id112)
    3. [Bucles con until](#id113)
    4. [Continue y Break](#id114)
12. [Funciones](#id12) 
13. [Depuración y testeo](#id13)



<div id="id1" />

## 1. Introducción 
Linux dispone de varios intérpretes de comandos (“shells”) diferentes csh, bash, sh,ksh, etc

En este tema nos centraremos en el shell **bash**  (Bourne-again shell).
* Es una alternativa libre a Bourne shell
* Versión mejorada de csh y ksh

Debemos usar bash para:
* Agilizar procesos largos y tediosos
* Automatizar acciones repetitivas
* Mejorar la experiencia del usuario


<div id="id2" />

## 2. Primer script hola mundo
Crearemos un nuevo archivo llamado holamundo.sh
```
touch holamundo.sh
```
También podemos utilizar un editor:
```
nano holamundo.sh
```
A continuación añadimos las siguientes líneas en nuestro archivo `holamundo.sh`:
```bash
#!/bin/bash

echo "Hola mundo"
```
Guardamos el archivo y le damos a salir

Después le damos permisos de ejecución al script
```
chmod +x holamundo.sh
```
Ejecutamos el script
```
./holamundo.sh
```
Mostrará por pantalla el mensaje Hola mundo

Otra forma de ejecutar el script sería
```
bash holamundo.sh
```

<div id="id3" />

## 3. Variables
Como en cualquier lenguaje de programación, podemos utilizar variables. Una variable es un elemento que tiene un nombre y que almacena un valor.

Para asignar un valor a una variable todo lo que necesitas es usar el signo `=`
```bash
nombre="Pepe"
```
>Nota : No pueden haber espacios delante y detrás del signo =

Después, para acceder a la variable debemos utilizar el signo `$` de la siguiente forma:
```bash
echo $nombre
```

Si modificamos nuestro script anterior `holamundo.sh` 
```bash
#!/bin/bash

nombre="Pepe"
echo "Hola $nombre"
```
Si lo ejecutamos nos devuelve 
```
Hola Pepe
```
<div id="id4" />

## 4. Entrada de datos por el usuario
Para leer datos del usuario y almacenarlo en una variable utilizaremos el comando `read`.
```bash
#!/bin/bash
echo "¿Cómo te llamas?"
read nombre

echo "Bienvenido/a $nombre"
```
>Nota: Se puede utilizar el comando `read` con la opción  -p para indicar en la misma línea el mensaje que se mostrará por pantalla

```bash
#!/bin/bash
read -p "¿Cómo te llamas?" nombre

echo "Bienvenido/a $nombre"
```
<div id="id5" />
<br/><br/>

## 5. Comentarios

Como en cualquier lenguaje de programación, puedes añadir comentarios a tu script
Para ello, solo debes añadir el símbolo `#` al principio de la línea.
```bash
#!/bin/bash

#Solicita el nombre al usuario
read -p "¿Cómo te llamas?" nombre

#Saluda al usuario por su nombre
echo "Bienvenido/a $nombre"
```

<div id="id6" />

## 6. Parámetros
Al ejecutar un script podemos pasarle parámetros. Para pasarle un parámetro, sólo debemos escribirlo detrás del nombre del script
```
./script.sh parametro
```
En el script, podemos hacer referencia al primer parámetro pasado con la variable `$1`, al segundo parámetro con la varible `$2` y así sucesivamente.

Vamos a crear el script `parametros.sh` de ejemplo:

```bash
#!/bin/bash
echo "Primer parámetro es $1"
echo "Segundo parámetro es $2"
echo "Tercer parámetro es $3"
```

Guardamos el archivo y le damos permisos de ejecución
```
chmod +x parametros.sh
```
A continuación lo ejecutamos y le pasamos 3 parámetros:
```
./parametros.sh azul amarillo azul
```
Obtenemos la siguiente salida:
```
Primer parámetro es azul
Segundo parámetro es amarillo
Tercer parámetro es azul
```
Para obtener todos los parámetros podemos usar el símbolo `$@`:

```bash
#!/bin/bash

echo "Todos los parámetros: $@"
```

Si ejecutamos de nuevo el script
```
./parametros.sh azul amarillo azul
```
Obtenemos la siguiente salida:
```
Todos los parámetros: azul amarillo azul
```


### Resumen de las variables utilizadas con los parámetros
| Variable | Significado 
| -------- | ----------- 
| $0 | Nombre del script  
| $1 ... $9 |  Parámetros pasados al script 
| $# | Número de parámetros pasados al script 
| $* | Parámetros pasados al script 
| $@ | Parámetros pasados al script 


<div id="id7" />

## 7. Arrays
Si ya sabes programar en algún lenguaje de programación, ya estarás familiarizado con los arrays (matrices). En caso contrario, a diferencia de las variables, los arrays pueden contener varios valores bajo un nombre.

Puedes inicializar un array asignando valores separados por espacios y encerrados entre `()`.

```bash
mi_array=("valor1" "valor2" "valor3" "valor4")
```
Para acceder a los elementos en un array, necesitas referenciarlos con un índice numérico.
>Nota: No debes olvidar que necesitas usar llaves `{}`

+ Esto daría como resultado: valor 2
```bash
echo ${mi_array[1]}
```
+ Esto daría como resultado el último elemento: valor4
```bash
echo ${mi_array[-1]}
```

+ Esto imprimiría el número total de elementos en el array: 4
```bash
echo ${mi_array[@]}
```
<br/><br/>

<div id="id8" />

## 8. Matematicas en bash
Por defecto, una variable, en cualquier script en Bash, con independencia de su contenido, es tratada como una cadena de texto, y no como un número. 
Sin embargo, una observación importante, **Bash solo opera con enteros**. Para realizar operaciones matemáticas en Bash con números reales, necesitas utilizar `bc`

### Operadores matemáticos


|Operador | Descripción |
| ------- | ------------|
| \+      | (adición o suma) |
| \-      | (sustracción o resta) |
| \*      | (producto o multiplicación) |
| /      | (división)  |
| %      | (módulo) |

Ejemplo:
```bash
num1=2
num2=3
num3=$((num1+num2))
echo $num3

```

En Bash, hay varias formas de realizar operaciones matemáticas, y la elección de cuál utilizar dependerá del tipo de operación que se desea realizar y de las necesidades específicas de cada situación.

### 8.1 Doble paréntesis (( )) 
Esta sintaxis permite realizar operaciones aritméticas básicas y avanzadas, así como comparaciones numéricas y lógicas. Los doble paréntesis permiten utilizar variables sin necesidad de utilizar el signo "$" y también permiten la asignación de valores a variables en la misma línea de código. Por ejemplo:
```bash
num1=5
num2=3
resultado=$((num1 + num2))
echo $resultado
```
### 8.2 Expr 
Esta herramienta se utiliza para realizar operaciones aritméticas básicas utilizando la línea de comandos de Bash. Expr no permite la asignación de valores a variables ni la realización de operaciones avanzadas, pero es útil para operaciones sencillas. Por ejemplo:
```bash
num1=5
num2=3
resultado=$(expr $num1 + $num2)
echo $resultado

```

### 8.3 Let
 Esta sintaxis también se utiliza para realizar operaciones aritméticas básicas utilizando la línea de comandos de Bash. Let es similar a los doble paréntesis, pero no permite la comparación ni la asignación de valores en la misma línea de código. Por ejemplo:
```bash
num1=5
num2=3
let resultado=$num1+$num2
echo $resultado
```
En general, se recomienda utilizar los `doble paréntesis (( )) `cuando se necesite realizar operaciones avanzadas y/o comparaciones numéricas o lógicas. Si se desea realizar operaciones aritméticas básicas, se puede utilizar `expr o let` según las preferencias del usuario.

Ejemplo:
```bash
num1=5
num2=3
resultado=$((num1 * (num2 + 2)))
echo $resultado
```
En este ejemplo, se utiliza los doble paréntesis para realizar la operación (num2 + 2) antes de multiplicar el resultado por num1. Si se utilizara let para realizar esta operación, tendríamos que almacenar el resultado de la suma en una variable temporal antes de multiplicarla por num1, como se muestra a continuación:
```bash
num1=5
num2=3
temp=$(($num2 + 2))
resultado=$(($num1 * $temp))
echo $resultado
```
En este caso, es más fácil y legible utilizar los doble paréntesis para realizar la operación en una sola línea de código.

### 8.4 Matemáticas en bash con bc
Todas las operaciones matemáticas realizadas hasta el momento solo implican números enteros. Sin embargo, cuando quieres realizar operaciones con numeros reales, necesitarás recurrir a una herramienta como es `bc`.
Ejemplos:
```bash
echo '4.1+5.2' | bc #devuelve 9.3
echo '4.1*5.2' | bc #devuelve 21.3
```
Si quieres guardar el resultado de la operación en una variable, tienes que modificar los ejemplos anteriores como sigue,

```bash
z=$(echo '4.1+5.2' | bc);echo $z #devuelve 9.3
z=$(echo '4.1*5.2' | bc);echo $z #devuelve 21.3
```
<div id="id9" />

## 9. Evaluación de expresiones
En informática, las evaluación de expresiones condicionales son características de un lenguaje de programación, que realizan diferentes cálculos o acciones dependiendo de si una condición booleana especificada por el programador se evalúa como verdadera o falsa.

Para evaluar expresiones utilizaremos el comando `test expresion` o su equivalente `[ expresion ]`. También podemos utilizar los dobles corchetes `[[ expresion ]]` que representa una mejora respecto a los simples.



A continuación veremos las expresiones condicionales más utilizadas.

<div id="id91" />

### 9.1 Expresiones de archivos

+ Devuelve verdadero si el archivo existe y se trata de un archivo especial de bloque
```bash
[[ -b $archivo ]]
```
>Nota: Los archivos especiales se utilizan para representar un dispositivo físico real que se utilizan para operaciones de entrada/salida. Los archivos especiales de bloque leen/escriben en bloque, como por ejemplo un disco /dev/sda1 y los de carácter realizan las operaciones de lectura/escritura carácter a carácter como por ejemplo una impresora, terminal, etc.


+ Devuelve verdadero si el archivo existe y se trata de un archivo especial de carácter
```bash
[[ -c $archivo ]]
```

+ Devuelve verdadero si el archivo existe y se trata de un directorio
```bash
[[ -d $archivo ]]
```

+ Devuelve verdadero si el archivo existe
```bash
[[ -e $archivo ]]
```

+ Devuelve verdadero si el archivo existe y se trata de un archivo regular
```bash
[[ -f $archivo ]]
```

+ Devuelve verdadero si el archivo existe y se trata de un enlace simbólico
```bash
[[ -h $archivo ]]

[[ -L $archivo ]]
```


+ Devuelve verdadero si el archivo existe y es legible
```bash
[[ -r $archivo ]]
```

+ Devuelve verdadero si el archivo existe y tiene un tamaño superior a cero.
```bash
[[ -s $archivo ]]
```

+ Devuelve verdadero si el archivo existe y se puede escribir
```bash
[[ -w $archivo ]]
```

+ Devuelve verdadero si el archivo existe y es ejecutable
```bash
[[ -x $archivo ]]
```

<div id="id92" />

### 9.2 Expresiones de cadenas

| Expresión | Descripción |
| :-------- | ------------|
| -v $cadena | Devuelve verdadero si a la variable se le ha asignado algún valor |
| -z $cadena | Devuelve verdadero si la longitud de la cadena es igual a cero |
| -n $cadena | Devuelve verdadero si la longitud de la cadena no es cero |
| $cadena1 = $cadena 2  | Devuelve verdadero si las dos cadenas son iguales.|
| $cadena1 != $cadena2 | Devuelve verdadero si las cadenas NO son iguales |
| $cadena1 < $cadena2 | Devuelve verdadero si la cadena1 es más pequeña que la cadena2 |
| $cadena 1 > $cadena2 | Devuelve verdadero si la cadena1 es mayor que la cadena 2 |

**Ejemplo**: Supongamos que queremos comprobar si una variable llamada "fruta" contiene el valor "manzana". Si es así, imprimimos un mensaje que dice "La fruta es una manzana", de lo contrario, imprimimos un mensaje que dice "La fruta no es una manzana". 

```bash
#!/bin/bash
fruta="manzana"

if [ "$fruta" == "manzana" ]; then
    echo "La fruta es una manzana"
else
    echo "La fruta no es una manzana"
fi
```


<div id="id83" />

### 9.3 Expresiones numéricas

| Expresion | Descripción |
|----------------|------------------|
| $num1 **-eq** $num2 | Devuelve verdadero si los dos números **son iguales** "equal" |
| $num1 **-ne** $num2 | Devuelve verdadero si los dos números **NO son iguales** "not equal"|
| $num1 **-lt** $num2 | Devuelve verdadero si el num1 **es menor que** "less than" num2 |
| $num1 **-le** $num2 | Devuelve verdadero si el num1 **es menor o igual** "less or equal " num2 |
| $num1 **-gt** $num2 | Devuelve verdadero si el num1 **es mayor que** "greater than" num2 |
| $num1 **-ge** $num2 | Devuelve verdadero si el num1 **es mayor o igual que** "greater or equal than" num2 | 



<div id="id94" />

### 9.4 Expresiones lógicas
+ Devuelve verdadero si ambas expresiones son verdaderas, en otro caso devuelve falso
```bash
#Doble corchete
[[ $expresion1 && $expresion2 ]]
#Corchete simple
[ $expresion1 ] && [ $expresion2 ]
[ $expresion1 -a $expresion2 ]
```

+ Devuelve verdadero si al menos una de las expresiones es verdadera
```bash
#Doble corchete
[[ $expresion1 || $expresion2 ]]
#Corchete simple
[ $expresion1 -o $expresion22 ]
[ $expresion1 ] || [ $expresion2 ]
```


Así, las principales diferencias entre usar corchete simple o doble corchete son las siguientes:

1. No tienes que utilizar las comillas con las variables, los dobles corchetes trabajan perfectamente con los espacios. Así `
[ -f "$file" ]` es equivalente a `[[ -f $file ]]`.

2. Con [[ puedes utilizar los operadores || y &&, así como < y >` para las comparaciones de cadena.

3.  Puedes utilizar el operador `=~` para expresiones regulares, como por ejemplo 
```bash 
[[ $respuesta =~ ^s(i)?$ ]]
```
4. También puedes utilizar comodines como por ejemplo en la expresión 
```bash
[[ abc = a\* ]]
```

<div id="id10" />

## 10. Condicionales
En la sección anterior estudiamos las expresiones condicionales más populares. Ahora las usaremos con declaraciones `if`.

Esta estructura permite controlar qué serie de instrucciones se ejecutarán, de acuerdo a si se cumplen las condiciones o no.

![image-20240301114643538](/aso/assets/img/linux/image-20240301114643538.png)

 

El formato de una declaración `if` es de la siguiente forma:

```bash
if [[ expresion ]]
then
    <comandos>
fi
```
También podemos utilizar la siguiente sintaxis:

```bash
if [[ expresion ]]; then
    <comandos>
fi

```
La estructura condicional con else tiene este aspecto:
```bash
if [[ expresion ]]; then
    <comandos>
else
    <comandos>
fi
```
Ejemplo:
```bash
#!/bin/bash

#Ejemplo de uso de if

read -p "¿Cómo te llamas?" nombre

if [[ -z $nombre ]]; then
   echo "Por favor, introduce tu nombre."
else
   echo "Hola $nombre"
fi

```

La estructura condicional con todas las alternativas sería así:
```bash
if [[ expresion ]]; then
    <comandos>
elif [[ expresion ]] ; then
    <comandos>
else
    <comandos>
fi
```

Cuando queremos comparar un elemento con muchos supuestos viene mejor utilizar  una estructura de control `case`
```bash
case expresion in
    patron1)
        comandos
        ;;
    patron2)
        comandos
        ;;
    *)
        comandos
        ;;
```

Ejemplo1:
```bash
#!/bin/bash

case $1 in
    alta)
        # comandos para realizar un alta
        ;;
    baja)
        #comandos para realizar una baja
        ;;
    modificar)
        #comandos para realizar una modificacion
        ;;
    *)
        echo "Parametro no reconocido"
        ;;
esac


```
Ejemplo 2:
```bash
#!/bin/bash
read –p “Introduzca un carácter alfanumérico: ” caracter
case $caracter in
[A-Z])
    echo “$caracter es una letra mayúscula”
    ;;
[a-z])
    echo “$caracter es una letra mayúscula”
    ;;
[0-9])
    echo “$caracter es un dígito”
    ;;
*)
    echo “carácter no identificado”
    ;;

esac
```

<div id="id11" />

## 11. Bucles
Un bucle es una secuencia de instrucciones de código que se ejecuta repetidas veces, hasta que la condición asignada a dicho bucle deja de cumplirse.
<div id="id111" />

### 11.1 Bucles con for
Esta es la estructura de un bucle for:
```bash
for var in lista
do
    comandos
done
```

Ejemplos:
```bash
#!/bin/bash

users="Maria Juan Pepe"

for user in $users
do
    echo "$user"
done
```
Al ejecutar el script nos devuelve este resultado:
```bash
Maria
Juan
Pepe
```
```bash
for i in `ls` ; do
    echo "El fichero es $i"
done
```
Si lo ejecutamos nos devuelve un listado de los ficheros que encuentra
```bash
El fichero es Descargas
El fichero es Documentos
El fichero es Escritorio
El fichero es Imágenes
El fichero es Música
El fichero es Vídeos
```
El bucle for tiene también otra sintaxis posible mucho más parecida a la de los lenguajes de programación convencionales (Java,C,C++,etc.)

```bash
for ((inicialización; condición; incremento))
do
    comandos
done
```
Ejemplo: Imprime los números del 1 al 10
```bash
for (( i=1; i<=10; i++ ))
do
    echo "$i"
done
```
<div id="id112" />

### 11.2 Bucles con while
El bucle while repite una serie de comandos mientras una condición sea cierta.

```bash
while [[ condicion ]]
do
    comandos
done
```
Ejemplo: Imprime los numeros del 1 al 10
```bash
#!/bin/bash

contador=1
while [[ $contador -le 10 ]]
do
    echo $contador
    ((contador++))
done
```
Ejemplo: Solicita un nombre al usuario. Se repite una y otra vez, hasta que el usuario introduce un nombre válido
```bash
#!/bin/bash

read -p "¿Cómo te llamas? " name

while [[ -z $name ]]
do
    echo "Tu nombre no puede estar en blanco, porfavor introduzca un nombre válido!
    read -p "Introduce tu nombre de nuevo. " name
done

echo "Hola $name"
```

<div id="id113" />

### 11.3 Bucles con until
El bucle until se repite hasta que la condición sea cierta

```bash
until [[ condicion ]] 
do
    comandos
done
```

Ejemplo: Imprime los números del 1 al 10
```bash
#!/bin/bash

count=1
until [ $count -gt 10 ]
do
    echo $count
    ((count++))
done
```

<div id="id114" />

### 11.4 Continue y Break
+ `continue` para la iteración actual del bucle y comienza la siguiente iteración.
+ `break` finaliza el bucle 

 <div id="id12" />

## 12. Funciones

Las funciones nos van a permitir reutilizar el código, y no tener que repetir una y otra vez el mismo código.
```bash
function nombre_funcion() {
    comandos
}
```
Ejemplo:
```bash
#!/bin/bash
function saluda(){
    echo "Hola mundo"
}

saluda
```
>Nota: Debes tener en cuenta que cuando llamas a la función no pones los paréntesis.

Podemos pasar argumentos a una función, de la misma forma que lo hacemos con los scripts.
```bash
#!/bin/bash
function saluda(){
    echo "Hola $1"
}

saluda Pepe
```
Imprimirá por pantalla
```bash
Hola Pepe
```

<div id="id13" />

## 13. Depuración y testeo

Para depurar nuestros scripts, podemos usar `-x` al ejecutar el script
```bash
bash -x ./script.sh
```

También puedes añadir `set -x` antes de la línea que quieres depurar, `set -x` habilita un modo en el que todos los comandos ejecutados son impresos por pantalla.

Otra forma de testear nuestros scripts es usar esta herramienta [ShellCheck](https://www.shellcheck.net/)



## 14. Buenas prácticas y recomendaciones

Durante la creación de nuestros scripts, es importante seguir unas buenas prácticas para prevenir errores comunes, mejorar la legibilidad del código y asegurar la compatibilidad entre diferentes entornos.

**Estilo de Codificación**

- **Indentación y Espaciado:** Mantén una consistencia en la indentación y usa espacios (o tabs) de forma coherente para mejorar la legibilidad.
- **Nomenclatura de Variables:** Usa nombres descriptivos y sigue un estilo consistente 
- **Agrupación de Código:** Organiza tu código en secciones lógicas y usa comentarios para describir bloques de código importantes.

**Manejo de Errores**

- **Comprobación de Errores:** Verifica el estado de salida de los comandos importantes y maneja los errores de forma adecuada.
- **Uso del Comando `exit`:** Utiliza valores de salida específicos para indicar diferentes tipos de errores o éxito.

**Herramientas y recursos para mejorar la calidad del código**

- **Linters y Analizadores de Código:** Usa herramientas como `shellcheck` para detectar problemas y posibles mejoras en tus scripts.
- **Guías de Estilo:** Refiérete a guías de estilo como [Google's Shell Style Guide](https://google.github.io/styleguide/shellguide.html) para mantener un código coherente y bien organizado. 
