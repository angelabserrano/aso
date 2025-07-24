---
typora-copy-images-to: ../assets/img/linux
typora-root-url: ../../
layout: post
title: Linux - Samba PRACTICA 1
categories: linux
conToc: false
permalink: linux-samba-practica1
---

## PRÁCTICA 1

##  Implementación de un servidor Samba como Controlador de Dominio (AD DC) en Ubuntu Server 22.04 LTS y unión de un cliente Windows 10 al dominio



## Objetivos:

- Implementar un servidor Ubuntu Server 22.04 LTS como controlador de dominio Samba (AD DC).
- Integrar un equipo con Windows 10 en el dominio gestionado por Samba.
- Gestionar usuarios y grupos dentro del dominio Samba desde el servidor.

## 1. Preparación del servidor Ubuntu Server

Una vez que tengamos una máquina con ubuntu Server 22.04 instalado realizamos los siguientes pasos: 



#### 1. Cambiar el nombre del servidor

```
sudo hostnamectl set-hostname dcNombreApellidos

```

**Explicación:**

- Se cambia el nombre del host al formato `dcNombreApellidos`, que identifica de forma única al servidor del alumno.
- Sustituir `NombreApellidos` por el nombre real del alumno sin espacios.

#### 2. Modificar el archivo `/etc/hosts`

```
sudo nano /etc/hosts
Añadir la línea correspondiente, por ejemplo:
192.168.1.2 dcJuanPerez.ieselcaminas.local dcJuanPerez
```

**Explicación:**

- Esta línea asocia el FQDN del servidor y su alias corto con la IP fija `192.168.1.2`.
- Cada alumno deberá personalizarla con su propio nombre de host.

#### 3. Verificar el FQDN

```

hostname -f
Debe mostrar:
dcNombreApellidos.ieselcaminas.local
```



#### 4. Verificar si el FQDN resuelve la dirección IP

```

ping -c2 dcNombreApellidos.ieselcaminas.local
```



**Explicación:**

- El comando `ping` permite comprobar si un nombre de dominio se resuelve correctamente y si el host está accesible.
- El parámetro `-c2` indica que se envíen solo 2 paquetes.
- Si la respuesta incluye líneas como:
   `"Respuesta desde dcNombreApellidos.ieselcaminas.local"`,
   significa que el FQDN se ha resuelto correctamente a la IP asignada.

#### 5. Desactivar el servicio systemd-resolved

```

sudo systemctl disable --now systemd-resolved
```

**Explicación:**

- El servicio `systemd-resolved` gestiona la resolución de nombres de dominio en sistemas modernos basados en systemd.
- Es necesario desactivarlo porque **Samba AD DC** debe encargarse directamente de la resolución de nombres, sin interferencias externas, para que funcione correctamente como servidor DNS del dominio.



```

```

#### 6. Eliminar el enlace simbólico al archivo /etc/resolv.conf

```
sudo unlink /etc/resolv.conf
```



**Explicación:**

- El archivo `/etc/resolv.conf` contiene la configuración del sistema para la resolución de nombres de dominio.
- En Ubuntu, este archivo suele ser un **enlace simbólico** gestionado por `systemd-resolved`.
   Para que Samba tenga control completo del DNS, eliminamos ese enlace y gestionamos el archivo de forma manual.

#### 7. Crear el archivo /etc/resolv.conf

```
sudo nano /etc/resolv.conf
```



```
Contenido recomendado:
nameserver 127.0.0.1
search ieselcaminas.local
```



**Explicación:**

- Creamos un nuevo archivo manual para que la resolución de nombres se realice a través del **propio servidor Samba**, que actuará como DNS interno.

- `nameserver 127.0.0.1` indica que el servidor se consultará a sí mismo para resolver nombres.

- `search ieselcaminas.local` permite completar automáticamente nombres de host del dominio.

  

#### 8. Agregar las siguientes líneas al archivo /etc/resolv.conf

```

nameserver 192.168.1.2
nameserver 8.8.8.8
search ieselcaminas.local
```



**Explicación:**

- Se configura el **servidor DNS principal** como el propio servidor Samba AD DC (`192.168.1.2`), que gestionará la resolución de nombres dentro del dominio.
- Se añade un **servidor DNS externo** (Google, `8.8.8.8`) como respaldo para resolver dominios externos a `ieselcaminas.local`.
- Se define el **dominio de búsqueda** como `ieselcaminas.local`, lo que permite usar nombres cortos en las consultas DNS.

```

```

#### 9. Hacer inmutable el archivo /etc/resolv.conf

```
sudo chattr +i /etc/resolv.conf
```

**Explicación:**

- El comando `chattr +i` establece el atributo **inmutable** sobre el archivo.
- Esto impide que otros servicios (como resolvconf o systemd) lo sobrescriban o modifiquen accidentalmente.
- Si más adelante necesitas editar el archivo, puedes hacerlo con:

```
sudo chattr -i /etc/resolv.conf
```



##  2. Instalación de Samba



> 
