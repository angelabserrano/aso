---
typora-copy-images-to: ../assets/img/linux
typora-root-url: ../../
layout: post
title: Linux - Samba PRACTICA 1
categories: linux
conToc: false
permalink: linux-samba-practica1
order: 6
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

```bash
sudo hostnamectl set-hostname dcNombreApellidos
```

**Explicación:**

- Se cambia el nombre del host al formato `dcNombreApellidos`, que identifica de forma única al servidor del alumno.
- Sustituir `NombreApellidos` por el nombre real del alumno sin espacios.

#### 2. Configurar IP estática en el servidor

Abrimos el archivo de configuración de la red  00-installer-config.yaml o 50-cloud-init.yaml depende la instalación que hayas realizado.

```bash
sudo nano /etc/netplan/00-installer-config.yaml
```

![image-20250727124701364](/aso/assets/img/linux/redServerSamba.png)

Para aplicar los cambios ejecuta el siguiente comando

```bash
sudo netplan apply
```



#### 3. Modificar el archivo `/etc/hosts`

```
sudo nano /etc/hosts
Añadir la línea correspondiente, por ejemplo:
192.168.1.2 dcJuanPerez.ieselcaminas.local dcJuanPerez
```

**Explicación:**

- Esta línea asocia el FQDN del servidor y su alias corto con la IP fija `192.168.1.2`.
- Cada alumno deberá personalizarla con su propio nombre de host.

#### 4. Verificar el FQDN

```
hostname -f
Debe mostrar:
dcNombreApellidos.ieselcaminas.local
```



#### 5. Verificar si el FQDN resuelve la dirección IP

```bash
ping -c2 dcNombreApellidos.ieselcaminas.local
```



**Explicación:**

- El comando `ping` permite comprobar si un nombre de dominio se resuelve correctamente y si el host está accesible.
- El parámetro `-c2` indica que se envíen solo 2 paquetes.
- Si la respuesta incluye líneas como:
   `"Respuesta desde dcNombreApellidos.ieselcaminas.local"`,
   significa que el FQDN se ha resuelto correctamente a la IP asignada.

#### 6. Desactivar el servicio systemd-resolved

```bash
sudo systemctl disable --now systemd-resolved
```

**Explicación:**

- El servicio `systemd-resolved` gestiona la resolución de nombres de dominio en sistemas modernos basados en systemd.
- Es necesario desactivarlo porque **Samba AD DC** debe encargarse directamente de la resolución de nombres, sin interferencias externas, para que funcione correctamente como servidor DNS del dominio.



#### 7. Eliminar el enlace simbólico al archivo /etc/resolv.conf

```bash
sudo unlink /etc/resolv.conf
```



**Explicación:**

- El archivo `/etc/resolv.conf` contiene la configuración del sistema para la resolución de nombres de dominio.
- En Ubuntu, este archivo suele ser un **enlace simbólico** gestionado por `systemd-resolved`.
   Para que Samba tenga control completo del DNS, eliminamos ese enlace y gestionamos el archivo de forma manual.

#### 8. Crear el archivo /etc/resolv.conf

```bash
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

  

#### 9. Agregar las siguientes líneas al archivo /etc/resolv.conf

```
nameserver 192.168.1.2
nameserver 8.8.8.8
search ieselcaminas.local
```



**Explicación:**

- Se configura el **servidor DNS principal** como el propio servidor Samba AD DC (`192.168.1.2`), que gestionará la resolución de nombres dentro del dominio.
- Se añade un **servidor DNS externo** (Google, `8.8.8.8`) como respaldo para resolver dominios externos a `ieselcaminas.local`.
- Se define el **dominio de búsqueda** como `ieselcaminas.local`, lo que permite usar nombres cortos en las consultas DNS.



#### 10. Hacer inmutable el archivo /etc/resolv.conf

```bash
sudo chattr +i /etc/resolv.conf
```

**Explicación:**

- El comando `chattr +i` establece el atributo **inmutable** sobre el archivo.
- Esto impide que otros servicios (como resolvconf o systemd) lo sobrescriban o modifiquen accidentalmente.
- Si más adelante necesitas editar el archivo, puedes hacerlo con:

```bash
sudo chattr -i /etc/resolv.conf
```



##  2. Instalación de Samba

#### 1. Actualiza el índice de paquetes disponibles en los repositorios configurados

```bash
sudo apt update
```


#### 2. Instalar el paquete samba y las dependencias necesarias

```bash
sudo apt install -y acl attr samba samba-dsdb-modules samba-vfs-modules smbclient winbind libpam-winbind libnss-winbind libpam-krb5 krb5-config krb5-user dnsutils chrony net-tools
```


| **Paquete**          | **Función**                                                  | **¿Es imprescindible para un AD DC?** |
| -------------------- | ------------------------------------------------------------ | ------------------------------------- |
| `acl`                | Permite configurar listas de control de acceso (ACL) en archivos y carpetas. | Recomendado                           |
| `attr`               | Añade soporte para atributos extendidos en archivos, útil en entornos avanzados. | Recomendado                           |
| `samba`              | Instala el servicio principal Samba, que permite que el servidor funcione como un Controlador de Dominio (AD DC). | **Sí, imprescindible**                |
| `samba-dsdb-modules` | Añade módulos internos necesarios para la base de datos del dominio Samba. | **Sí, imprescindible**                |
| `samba-vfs-modules`  | Extiende las capacidades de Samba para usar funciones como auditorías o cuotas de disco. | Recomendado                           |
| `smbclient`          | Cliente de línea de comandos para conectarse a recursos compartidos SMB. Útil para pruebas. | Opcional pero útil                    |
| `winbind`            | Permite al servidor resolver usuarios y grupos del dominio. También se usa para integrar equipos Linux como clientes del dominio. | Recomendado                           |
| `libpam-winbind`     | Permite iniciar sesión en el sistema Linux con usuarios del dominio, usando PAM. | Opcional                              |
| `libnss-winbind`     | Hace que los usuarios y grupos del dominio aparezcan como usuarios locales para el sistema. | Opcional                              |
| `libpam-krb5`        | Añade autenticación Kerberos al sistema mediante PAM.        | Opcional                              |
| `krb5-config`        | Archivos de configuración para el sistema de autenticación Kerberos. | **Sí, imprescindible**                |
| `krb5-user`          | Herramienta para autenticarse como usuario mediante Kerberos desde consola. | Recomendado                           |
| `dnsutils`           | Incluye herramientas como `dig` para probar y depurar el DNS del dominio. | Recomendado                           |
| `chrony`             | Sincroniza la hora del sistema, lo cual es esencial para que funcione Kerberos correctamente. | **Sí, imprescindible** (o `ntp`)      |
| `net-tools`          | Herramientas clásicas como `ifconfig` o `netstat`, útiles para diagnóstico de red. | Opcional                              |

### 3. Detener y deshabilitar servicios innecesarios

Para evitar conflictos con el controlador de dominio Samba, detenemos y deshabilitamos algunos servicios que no deben estar activos en este modo:

```bash
sudo systemctl disable --now smbd nmbd winbind
```

-  **smbd** y **nmbd** son servicios clásicos de Samba que no se utilizan cuando el servidor actúa como **Controlador de Dominio (AD DC)**.
- En un **Controlador de Dominio Samba**, `winbind` no debe estar activo. Solo se instala y se usa en los **clientes Linux del dominio**.

#### 4. Habilitación del servicio Samba como Controlador de Dominio (AD DC)

Para que el servicio Samba funcione como **Controlador de Dominio Active Directory**, es necesario **desbloquearlo** y **habilitar su arranque automático**:

```bash
sudo systemctl unmask samba-ad-dc
sudo systemctl enable samba-ad-dc

```

- **sudo systemctl unmask samba-ad-dc**: Elimina la "máscara" del servicio, permitiendo que pueda activarse y gestionarse. Algunos servicios vienen bloqueados por defecto.
- **sudo systemctl enable samba-ad-dc**:
  Activa el inicio automático del servicio al arrancar el sistema, dejándolo listo para funcionar como AD DC.
