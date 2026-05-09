# Bash Avanzado

Esta unidad profundiza en Bash orientado a la **administración de sistemas**, asumiendo que ya conoces los fundamentos (variables, condicionales, bucles) trabajados en 1º en el módulo de ISO.

## 1. Funciones

Las funciones permiten reutilizar bloques de código y estructurar scripts complejos.

```bash
nombre_funcion() {
    # cuerpo de la función
    echo "Hola, $1"
    return 0
}

# Llamada
nombre_funcion "mundo"
```

- **`$1`, `$2`...**: parámetros recibidos por la función.
- **`return`**: devuelve un código de salida (0 = éxito, distinto de 0 = error).
- **`$?`**: recoge el código de salida de la última función o comando ejecutado.

**Ejemplo: función que comprueba si un usuario existe**

```bash
usuario_existe() {
    if id "$1" &>/dev/null; then
        return 0
    else
        return 1
    fi
}

if usuario_existe "angela"; then
    echo "El usuario existe"
else
    echo "El usuario no existe"
fi
```

## 2. Manejo de errores

### Códigos de salida

Todo comando devuelve un código de salida: **0** indica éxito, cualquier otro valor indica error.

```bash
ls /ruta/inexistente
echo "Código de salida: $?"   # Mostrará un valor distinto de 0
```

### `set -e` y `set -u`

```bash
#!/bin/bash
set -e   # El script se detiene si cualquier comando falla
set -u   # El script se detiene si se usa una variable no definida
```

### `trap`: capturar señales y errores

`trap` permite ejecutar código cuando el script recibe una señal o termina.

```bash
trap "echo 'Script interrumpido'; exit 1" SIGINT SIGTERM

trap 'echo "Error en la línea $LINENO"' ERR
```

**Ejemplo: limpieza al salir**

```bash
#!/bin/bash
set -e

TMPFILE=$(mktemp)
trap "rm -f $TMPFILE" EXIT

echo "Trabajando con $TMPFILE..."
# Si el script falla o termina, el fichero temporal se elimina siempre
```

## 3. Procesado de texto con `sed`

`sed` (stream editor) permite transformar texto línea a línea.

### Sustitución

```bash
# Sustituir la primera ocurrencia en cada línea
sed 's/antiguo/nuevo/' fichero.txt

# Sustituir todas las ocurrencias (flag g)
sed 's/antiguo/nuevo/g' fichero.txt

# Modificar el fichero directamente (flag -i)
sed -i 's/antiguo/nuevo/g' fichero.txt
```

### Borrar líneas

```bash
# Borrar líneas que contienen "error"
sed '/error/d' fichero.txt

# Borrar líneas en blanco
sed '/^$/d' fichero.txt
```

### Imprimir líneas concretas

```bash
# Imprimir solo la línea 5
sed -n '5p' fichero.txt

# Imprimir líneas de la 3 a la 7
sed -n '3,7p' fichero.txt
```

## 4. Procesado de texto con `awk`

`awk` procesa texto estructurado en columnas.

```bash
awk '{ print $1 }' fichero.txt        # Imprime la primera columna
awk -F: '{ print $1 }' /etc/passwd    # Usa : como separador
awk '$3 > 1000 { print $1 }' /etc/passwd  # Filtra por condición
```

**Ejemplo: listar usuarios del sistema con UID > 1000**

```bash
awk -F: '$3 > 1000 { print $1, $3 }' /etc/passwd
```

**Ejemplo: calcular el total de una columna**

```bash
awk -F: '{ suma += $3 } END { print "Total:", suma }' fichero.csv
```

## 5. Expresiones regulares avanzadas

### `grep` extendido

```bash
grep -E "patron1|patron2" fichero.txt    # OR
grep -E "^[0-9]{3}-[A-Z]{2}" fichero.txt # líneas que empiezan por 3 dígitos, guión y 2 mayúsculas
grep -v "patron" fichero.txt             # líneas que NO coinciden
grep -c "patron" fichero.txt             # cuenta ocurrencias
```

### Caracteres especiales útiles

| Patrón | Descripción |
|--------|-------------|
| `^` | Inicio de línea |
| `$` | Fin de línea |
| `.` | Cualquier carácter |
| `*` | 0 o más repeticiones |
| `+` | 1 o más repeticiones |
| `?` | 0 o 1 repetición |
| `[abc]` | Uno de los caracteres indicados |
| `[^abc]` | Cualquier carácter excepto los indicados |
| `\d` / `[0-9]` | Dígito |
| `\w` / `[a-zA-Z0-9_]` | Carácter alfanumérico |

## 6. Scripts de administración

### 6.1 Parsear logs del sistema

**Ejemplo: extraer errores del syslog de las últimas 24 horas**

```bash
#!/bin/bash
LOG="/var/log/syslog"
SALIDA="/tmp/errores_$(date +%Y%m%d).txt"

grep -i "error\|critical\|failed" "$LOG" | \
    awk '{ print $1, $2, $3, $0 }' > "$SALIDA"

echo "Errores encontrados: $(wc -l < "$SALIDA")"
echo "Informe guardado en: $SALIDA"
```

### 6.2 Gestión masiva de usuarios desde CSV

Dado un fichero `usuarios.csv` con columnas `nombre,apellido,departamento`:

```bash
#!/bin/bash
set -e

FICHERO="usuarios.csv"
DOMINIO="empresa.local"

while IFS=, read -r nombre apellido departamento; do
    LOGIN="${nombre,,}.${apellido,,}"   # minúsculas
    
    if id "$LOGIN" &>/dev/null; then
        echo "Usuario $LOGIN ya existe, omitiendo..."
        continue
    fi
    
    useradd -m -c "$nombre $apellido" -G "$departamento" "$LOGIN"
    echo "$LOGIN:Cambiar2025." | chpasswd
    passwd --expire "$LOGIN"
    echo "Usuario $LOGIN creado en grupo $departamento"
done < <(tail -n +2 "$FICHERO")   # saltar cabecera
```

### 6.3 Script de backup automatizado

```bash
#!/bin/bash
set -e

ORIGEN="/home"
DESTINO="/backups"
FECHA=$(date +%Y%m%d_%H%M%S)
BACKUP="$DESTINO/backup_$FECHA.tar.gz"

mkdir -p "$DESTINO"

tar -czf "$BACKUP" "$ORIGEN"
echo "Backup creado: $BACKUP ($(du -sh "$BACKUP" | cut -f1))"

# Eliminar backups con más de 7 días
find "$DESTINO" -name "backup_*.tar.gz" -mtime +7 -delete
echo "Backups antiguos eliminados"
```

### 6.4 Monitorización de servicios

```bash
#!/bin/bash

SERVICIOS=("ssh" "apache2" "cron")
LOG="/var/log/monitor_servicios.log"

for servicio in "${SERVICIOS[@]}"; do
    if systemctl is-active --quiet "$servicio"; then
        echo "[OK]  $servicio activo" | tee -a "$LOG"
    else
        echo "[FAIL] $servicio caído — reiniciando..." | tee -a "$LOG"
        systemctl start "$servicio"
    fi
done
```

## Ejercicios prácticos

### Expresiones regulares

**Ejercicio 1**. Realiza un script que muestre la lista de los últimos usuarios que iniciaron sesión, incluidas las direcciones IP Origen. (Solo debes mostrar las líneas en las que aparece una IP). Debes hacer uso del comando `last` y `egrep`.

??? tip "Pista"
    El comando `last` muestra el historial de inicios de sesión. Una dirección IP está formada por cuatro grupos de 1 a 3 dígitos separados por puntos. Construye ese patrón con `egrep`.

---

**Ejercicio 2**. Realiza un script que busque cualquier fichero que pueda ser modificado por cualquier usuario (`--- --- rwx`) y guarde la lista de ficheros con la ruta exacta en el archivo `archivos_peligrosos.txt`.

??? tip "Pista"
    Usa `find` con el flag `-perm -o+w` para localizar ficheros con permiso de escritura para otros. Redirige la salida al fichero de destino. El flag `2>/dev/null` evita los errores de permiso al recorrer el sistema de ficheros.

---

### Funciones

**Ejercicio 3**. Reescribe el script de **agenda** utilizando **funciones** para estructurar el código. El programa debe permitir **añadir, listar, buscar, borrar y editar** contactos almacenados en un fichero `agenda.csv` con formato `Nombre;Teléfono;Email`.

**Requisitos mínimos:**

- Cada operación debe implementarse en una **función** (`añadir_contacto`, `listar_contactos`, `buscar_contacto`, `borrar_contacto`, `editar_contacto`, `imprimir_menu`).
- Incluir validaciones básicas de teléfono y correo electrónico (uso de expresiones regulares).
- Mostrar un **menú principal** que permita elegir la acción a realizar.
- Guardar los cambios en el fichero al finalizar cada operación.

??? tip "Pista"
    Usa un `case` para el menú principal. Para validar el teléfono y el email dentro de la función puedes usar el operador `=~`:
    ```bash
    [[ "$tel" =~ ^[0-9]{9}$ ]]
    [[ "$email" =~ ^[^@]+@[^@]+\.[^@]+$ ]]
    ```

---

**Ejercicio 4**. Crea un script que contenga una función `existe` que reciba como parámetro el nombre de un fichero. Si el fichero existe, el script debe cambiar sus permisos a ejecutable para el propietario, pero no para el resto.

??? tip "Pista"
    Usa `[ -f "$1" ]` dentro de la función para comprobar si el fichero existe. Para cambiar los permisos solo al propietario usa `chmod u+x,go-x`.

---

**Ejercicio 5**. Realiza un script utilizando funciones que permita crear un informe de las **IP libres** en la red en la que se encuentra el equipo con las siguientes secciones:

1. Listado de todas las IPs de la red indicando si está libre o no (usa `ping`).
2. Tipo de red (rango CIDR), nombre de la red, broadcast y máscara de subred.

??? tip "Pista"
    - Usa `ip route | grep -v default` para obtener el rango de red del equipo.
    - Extrae el prefijo de red con `cut -d'.' -f1-3` para recorrer las IPs con un bucle `for i in $(seq 1 254)`.
    - `ping -c 1 -W 1 <ip>` devuelve código 0 si la IP responde y distinto de 0 si está libre.
    - `ipcalc` permite obtener la información de red de forma sencilla.

## Práctica 1. Script de administración

!!! example "Tarea"

    Crea un script Bash completo que lea un fichero `empleados.csv` (columnas: `nombre`, `apellido`, `departamento`) y realice las siguientes acciones:

    1. Crear un grupo por cada departamento si no existe.
    2. Crear cada usuario con login `nombre.apellido` (en minúsculas), asignarlo a su grupo y forzar cambio de contraseña en el primer login.
    3. Registrar en un fichero de log (`/tmp/alta_usuarios.log`) cada acción realizada (usuario creado, grupo creado, errores).
    4. Si el usuario ya existe, mostrar un aviso y continuar sin error.

    El script debe usar funciones, gestión de errores (`set -e`, `trap`) y estar correctamente documentado.

    **Entrega:** Sube el script a tu repositorio de GitHub en la carpeta `UT1/` y entrega la URL en Aules.
