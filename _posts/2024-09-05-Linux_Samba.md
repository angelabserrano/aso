---
typora-copy-images-to: ../assets/img/linux
typora-root-url: ../../
layout: post
title: Linux - Samba
categories: linux
conToc: true
permalink: linux-samba
---

## 1. Introducción

**Samba** es un software de código abierto muy utilizado en sistemas operativos basados en Unix y Linux para proporcionar servicios de intercambio de archivos e impresoras con sistemas Windows. Su desarrollo comenzó en la década de 1990, y desde entonces, ha sido una herramienta esencial en **entornos de red heterogéneos**, donde conviven sistemas operativos diferentes.

Un **entorno o escenario de red** heterogéneo se refiere a una infraestructura de red informática en la cual coexisten y se comunican múltiples sistemas.

<img src="https://www.redeszone.net/app/uploads-redeszone.net/2015/01/servidor-samba-linux-apertura.jpg" alt="img" style="zoom: 33%;" />



##  2. Conceptos básicos

### Samba 

Samba es una implementación libre de código abierto del protocolo de ficheros compartidos SMB/CIFS para sistemas de tipo UNIX. Samba permite la interoperabilidad entre servidores Linux/Unix y clientes basados en Windows. Samba le ofrece al administrador de red libertad y flexibilidad en términos de ajustes, configuración y elección de sistemas y equipos. 

Samba proporciona servicios de archivos e impresión y puede integrarse en un dominio Windows, ya sea como controlador de dominio principal (PDC) o como miembro del dominio. 

### SMB/CIFS 

**Server Message Block (SMB) y Common Internet File System (CIFS)** son protocolos de red desarrollados para compartir archivos e impresoras entre nodos de una red. El protocolo SMB fue desarrollado originalmente por IBM y posteriormente ampliado por Microsoft y renombrado como CIFS. 

Los términos SMB y CIFS son a menudo intercambiables pero hay características en la implementación de SMB de Microsoft que no son parte del protocolo SMB original. Sin embargo, desde una perspectiva funcional, ambos son protocolos utilizados por Samba. 

![img](https://www.labsmac.es/wp-content/uploads/2022/08/samba-ficheros-compartidos.png)

### Kerberos 

**Kerberos** es un protocolo de seguridad creado por el MIT que usa una criptografía de claves simétricas para validar usuarios con los servicios de red, evitando así tener que enviar contraseñas a través de la red. Al validar los usuarios para los servicios de la red por medio de Kerberos, se frustran los intentos de usuarios no autorizados que intentan interceptar contraseñas en la red. 

Kerberos funciona a base de "tickets" que se otorgan por una tercera parte de confianza llamado centro de distribución de claves (KDC) para autenticar los usuarios a un conjunto de servicios de red. Una vez que el usuario se ha autenticado al KDC, se le envía un ticket específico para esa sesión de vuelta a la máquina del usuario. De esta manera cualquier servicio kerberizado buscará el ticket en la máquina del usuario en vez de preguntarle al usuario que se autentique usando una contraseña. 

**Kerberos** tiene su propia terminología para definir varios aspectos del servicio: 

- **Realm/Reino**: red que usa Kerberos, compuesto de uno o varios servidores (también conocidos como KDCs) y un número potencial de clientes. 

- **Principal**: es el nombre único de un usuario o servicio que puede autenticar mediante el uso de Kerberos. Todos los principales de un reino tienen su propia llave, que en el caso de los usuarios se deriva de su contraseña y en le de los servicios se genera aleatoriamente. 

- **Ticket**: son datos cifrados que el servidor Kerberos facilita a los clientes para su autenticación y que estos almacenan durante la sesión. Los principales tipos de tickets son: 
  - Ticket Granting Ticket (TGT): ticket de autenticación de un usuario en la red y que se solicita al iniciar la sesión. Normalmente los TGT tienen una validez de 10 horas. 
  - Ticket Granting Service (TGS): ticket que solicita un usuario para autenticarse frente a un servidor que también esté en la base de datos de Kerberos. 

- **KDC** (Centro de Distribución de de Claves): servidor Kerberos encargado de la autenticación, compuesto por un AS (Servidor de Autenticación) encargado de repartir los TGT y un Ticket Granting Server encargado de distribuir los TGS. 

### LDAP

**LDAP** son las siglas de **Lightweight Directory Access Protocol (en español Protocolo Ligero de Acceso a Directorios)** que hacen referencia a un 

protocolo a nivel de aplicación que permite el acceso a un servicio de directorio ordenado y distribuido para buscar diversa información en un 

entorno de red. LDAP también se considera una base de datos (aunque su sistema de almacenamiento puede ser diferente) a la que pueden 

realizarse consultas. 

LDAP organiza la información en una jerarquía basada en el uso de directorios. Estos directorios pueden almacenar una variedad de 

información y se pueden incluso usar de forma similar al Servicio de Información de Red (NIS), permitiendo que cualquiera pueda acceder a su 

cuenta desde cualquier máquina de la red. 

### Domain Name System (DNS) 

**Sistema de Nombres de Dominio (DNS)** es un sistema de nomenclatura jerárquica para equipos, servicios o cualquier recurso conectado a Internet o a una red privada. Este sistema asocia información variada con nombres de dominios asignados a cada uno de los participantes. Su función más importante, es traducir (resolver) nombres inteligibles para las personas en identificadores binarios asociados con los equipos conectados a la red, con el propósito de poder localizar y direccionar estos equipos mundialmente. 

El servidor DNS utiliza una base de datos distribuida y jerárquica que almacena información asociada a nombres de dominio en redes como Internet. Aunque como base de datos el DNS es capaz de asociar diferentes tipos de información a cada nombre, los usos más comunes son la asignación de nombres de dominio a direcciones IP y la localización de los servidores de correo electrónico de cada dominio. En Ubuntu Server la configuración del DNS se puede ver en fichero **/etc/resolv.conf**. 

### Network Time Protocol (NTP) 

Network Time Protocol (NTP) es un protocolo de Internet que se utiliza para sincronizar los relojes del sistema del ordenador a una fuente de tiempo de referencia. En Debian, el demonio ntpd maneja la sincronización. Los parámetros de NTP se configuran en el archivo **/etc/ntp.conf**. 

> -reto- ** ACTIVIDAD GRUPAL Análisis y Presentación de Protocolos en Samba como Controlador de Dominio **
>
> **Objetivo General:**
>
> Analizar y presentar el funcionamiento de los protocolos fundamentales para Samba en su rol de controlador de dominio (DC), explorando su configuración y su importancia en la administración y seguridad de redes.
>
>  **Descripción de la Actividad:**
>
> En esta práctica, cada grupo estudiará los protocolos **Kerberos**, **NTP**, **LDAP** y **DNS** en el contexto de Samba como controlador de dominio. Su objetivo es entender en profundidad el papel de cada protocolo, cómo se configuran en un entorno Linux con Samba y de qué manera estos protocolos colaboran para garantizar un entorno de dominio seguro y eficiente.
>
> 
