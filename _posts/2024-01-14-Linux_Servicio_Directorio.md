---
typora-copy-images-to: ../assets/img/linux
typora-root-url: ../../
layout: post
title: Linux - Administración del servicio de directorio en Linux
categories: linux
conToc: true
permalink: linux-servicio-directorio
---

## 1. Introducción

Un servicio de directorio es un sistema especializado que almacena,  organiza y proporciona acceso a información relacionada con los recursos de la red y los usuarios, actuando como un nexo centralizado para la  gestión de la infraestructura de TI.

**Los servicios de directorios**, son un conjunto de aplicaciones que guardan y administran toda la información sobre los elementos de una red.

- Cada **recurso** de la red se considera como un **objeto**, donde su **información se almacena como atributos**.
- Para la gestión de esta información, el **servicio de directorio** establece una serie de **permisos de acceso y condiciones de seguridad** que la salvaguardan esta información.
- Ofrecen una **infraestructura** para localizar, manejar, administrar, y organizar los componentes y recursos comunes de una red.

## 2. Servicios de directorio destacados

### **Windows: Active Directory**

- **Active Directory (AD):** La solución de Microsoft para servicios de directorio en entornos Windows. Es una base de datos y un conjunto de servicios que permiten la administración centralizada de usuarios, computadoras y otros recursos en un dominio de red.
- Características clave:
  - Integración con Windows Server y otros productos Microsoft.
  - Gestión de políticas de grupo y autenticación de usuarios.
  - Soporte para LDAP y Kerberos.

###  **Linux: OpenLDAP y Samba**

- OpenLDAP:
  - Un servicio de directorio de código abierto que implementa el protocolo LDAP.
  - Utilizado para gestionar usuarios y recursos en redes Linux y multiplataforma.
- Samba:
  - Permite la integración de servidores Linux/Unix en redes dominadas por Windows.
  - Proporciona compatibilidad con Active Directory y servicios de directorio de Windows.

## 3. LDAP

Atendiendo a la interacción con el usuario podemos distinguir:

- **Procesos en primer plano (foreground)**: precisan de la intervención del usuario.
- **Procesos en segundo plano (background):** Se ejecutan sin que el usuario tenga que hacer nada

Atendiendo al modo en que se ejecutan podemos distinguir:

- **Procesos en modo kernel:** Son procesos que tienen acceso privilegiado a todo el equipo. Son mucho más seguros. La mayoría de procesos del sistema operativo son de este tipo.
- **Procesos en modo usuario:**Menos seguros. Todos los que ejecutan los usuarios y/o aplicaciones de usuario suelen ser de este tipo .

Dependiendo de quien lo ejecutó podemos distinguir:

- **Procesos del sistema:** Los que han sido lanzados por el propio sistema operativo.
- **Procesos del usuario:** Los que ha lanzado un usuario

