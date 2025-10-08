---
layout: default
title: Expresiones Regulares
nav_order: 13
parent: Linux Bash
permalink: /regex/
---

# Guía de Expresiones Regulares en Linux

## 1. Introducción

Las expresiones regulares (regex o regexp) son patrones utilizados para buscar y manipular texto.  
En Linux son fundamentales para trabajar con archivos y flujos de texto, especialmente en herramientas como **grep**, **sed**, **awk** y editores como **vim**.

### ¿Por qué son útiles?

- 🔍 **Búsqueda rápida:** encuentra patrones específicos en grandes volúmenes de texto.  
- ✏️ **Edición automatizada:** modifica texto de manera eficiente y repetitiva.  
- ✅ **Validación de datos:** comprueba formatos como correos o números de teléfono.

### Herramientas que utilizan regex

| Herramienta | Uso principal |
|--------------|----------------|
| `grep` | Buscar patrones en texto |
| `sed` | Sustituir o editar texto |
| `awk` | Procesar y extraer columnas o patrones |
| `vim` | Edición avanzada con búsqueda y reemplazo |

---

## 2. Tipos de expresiones regulares

### Expresiones Regulares Básicas (BRE)

| Carácter | Significado | Ejemplo |
|-----------|--------------|----------|
| `^` | Principio de línea | `grep "^a" ejemplo.txt` |
| `$` | Fin de línea | `grep "s$" ejemplo.txt` |
| `*` | Repite 0 o más veces | `ho*la` → `hla`, `hooola` |
| `[]` | Cualquier carácter entre corchetes | `[aeiou]` |
| `.` | Cualquier carácter salvo salto de línea | `h.t` → `hat`, `hot` |

### Expresiones Regulares Extendidas (ERE)

Usadas con `grep -E` o `sed -r`.  
No requieren el uso de `\` antes de `?`, `+`, `{}` o `|`.

| Carácter | Significado | Ejemplo |
|-----------|--------------|----------|
| `?` | Cero o una vez | `colou?r` → `color`, `colour` |
| `+` | Una o más veces | `ho+la` → `hola`, `hooola` |
| `x\|y` | x o y | `gato|perro` |
| `{n}` | Exactamente n veces | `a{3}` → `aaa` |
| `{n,m}` | Entre n y m veces | `a{2,4}` → `aa`, `aaa`, `aaaa` |

---

## 3. Conceptos básicos

### Literales y caracteres especiales
- Un literal coincide exactamente con el texto escrito.
- Los caracteres especiales tienen significados específicos: `.`, `*`, `^`, `$`, etc.

### Escapado
Usa `\` para tratar un carácter especial como literal.  
Ejemplo: `\.` busca un punto literal.

---

## 4. Patrones fundamentales

### Coincidencia de caracteres
`.` : cualquier carácter excepto salto de línea.

```bash
grep 'h.t' archivo.txt   # Coincide con hat, hot
```

### Anclas
- `^Hola` → líneas que empiezan por “Hola”.  
- `mundo$` → líneas que terminan en “mundo”.

### Grupos y rangos
- `[aeiou]` → cualquier vocal.  
- `[^0-9]` → no dígitos.  
- `[a-z]` → letras minúsculas.

### Metacaracteres comunes
| Símbolo | Significado |
|----------|-------------|
| `\w` | Cualquier carácter de palabra |
| `\d` | Dígito (0–9) |
| `\s` | Espacio, tabulación o salto de línea |

### Repeticiones
- `*` → cero o más  
- `+` → una o más  
- `?` → opcional  
- `{n,m}` → entre *n* y *m* veces

---

## 5. Grupos y retroreferencias

### Uso de paréntesis
`(ab)+` → `ab`, `abab`, `ababab`

### Retroreferencias
`\1`, `\2`, etc., hacen referencia a los grupos capturados.  
Ejemplo: `(\w)\1` → letras duplicadas como `ee`, `ss`, `tt`.

---

## 6. Expresiones avanzadas

### Alternancia
`gato|perro` → coincide con “gato” o “perro”.

### Lookahead / Lookbehind
- `foo(?=bar)` → busca `foo` seguido de `bar`.  
- `(?<=foo)bar` → busca `bar` precedido de `foo`.

*(No todas las herramientas de Linux admiten lookahead/lookbehind; funcionan en `grep -P` o en lenguajes como Python o Perl.)*

---

## 7. Aplicaciones prácticas

### Buscar y reemplazar con sed
```bash
sed 's/gato/perro/' archivo.txt
```

### Filtrar texto con grep
```bash
grep '^Error' log.txt
```

### Manipular texto con awk
```bash
awk '/^Usuario/ {print $2}' datos.txt
```

---

## 8. Ejemplos comunes

| Caso | Expresión Regular | Descripción |
|------|--------------------|--------------|
| Correo electrónico | `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$` | Valida emails simples |
| Teléfono (España) | `^[67][0-9]{8}$` | Móviles de 9 cifras que empiezan por 6 o 7 |
| IP básica | `^[0-9]{1,3}(\.[0-9]{1,3}){3}$` | Formato IPv4 simple |
| Línea de error | `^[Ee]rror` | Coincide con “Error” o “error” |

---

## 9. Ejercicios propuestos

1. Muestra las líneas de un archivo que terminen con un número.  
2. Busca palabras que contengan tres vocales seguidas.  
3. Sustituye todas las apariciones de “foo” por “bar” en un archivo.  
4. Extrae las direcciones IP válidas de un log.  
5. Crea una expresión regular para validar un DNI (8 dígitos + letra).

---

## 10. Referencias
- [GNU grep manual](https://www.gnu.org/software/grep/manual/grep.html)  
- [GNU sed manual](https://www.gnu.org/software/sed/manual/sed.html)  
- [Google RE2 syntax](https://github.com/google/re2/wiki/Syntax)

---

## 🔗 Volver al temario principal
➡️ [Volver a Linux Bash](linux-bash.md)

