---
typora-copy-images-to: ../assets/img/linux
typora-root-url: ../../
layout: post
title: Linux - Administración del servicio de directorio en Linux
categories: linux
conToc: true
permalink: linux-servicio-directorio
order: 4

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



## 3.  LDAP 

   LDAP, que significa **Lightweight Directory Access Protocol** (Protocolo Ligero de Acceso a Directorios), es un protocolo de red utilizado para acceder y administrar servicios de directorio a través de una red IP. Los servicios de directorio son bases de datos especializadas que almacenan información sobre recursos en una red, como usuarios, grupos, dispositivos y otros objetos.

   Algunas características clave de LDAP son:

   1. **Protocolo Ligero**: LDAP es una versión simplificada del protocolo DAP (Directory Access Protocol) que facilita su implementación y uso.
   2. **Acceso y Consulta**: Permite a los clientes consultar, buscar y modificar información en un directorio de forma eficiente.
   3. **Estructura Jerárquica**: Los datos en un directorio LDAP se organizan en una estructura jerárquica similar a un árbol, lo que facilita la administración y búsqueda de información.
   4. **Interoperabilidad**: LDAP es ampliamente utilizado y soportado por muchos sistemas y aplicaciones, lo que facilita la integración y compatibilidad entre diferentes plataformas.
   5. **Autenticación y Autorización**: LDAP se usa comúnmente para gestionar la autenticación de usuarios y controlar el acceso a recursos en una red, especialmente en entornos empresariales y académicos.

   Un ejemplo común de uso de LDAP es en la administración de directorios de usuarios en empresas, donde LDAP se utiliza para gestionar credenciales de acceso y permisos a diversos servicios y aplicaciones.

### 3.1 **Estructura y Funcionamiento del Protocolo LDAP**

LDAP sigue una estructura jerárquica en la que los datos se organizan en un árbol llamado **DIT (Directory Information Tree)**. Cada nodo del árbol representa una entrada (entry), que es una colección de atributos. Cada atributo tiene un nombre y uno o más valores asociados. Por ejemplo, un usuario puede tener atributos como `cn` (Common Name), `uid` (User ID), `mail` (dirección de correo electrónico), y `userPassword` (contraseña).

- **Distinguished Name (DN):** Cada entrada en un directorio LDAP tiene un identificador único llamado DN. Este nombre distingue de manera única cada entrada dentro del directorio. Un DN se construye concatenando los nombres de los elementos desde la entrada hasta la raíz del árbol. Por ejemplo, un DN podría ser `uid=jdoe,ou=users,dc=example,dc=com`, donde:
  - `uid=jdoe`: indica el usuario con ID "jdoe".
  - `ou=users`: indica que esta entrada está dentro de la unidad organizativa "users".
  - `dc=example,dc=com`: indica que el dominio es `example.com`.
- **Relative Distinguished Name (RDN):** El RDN es la parte del DN que identifica una entrada en particular dentro de su nivel jerárquico. En el ejemplo anterior, `uid=jdoe` es el RDN para el usuario "jdoe".

### 3.2 Tipos de Directorios LDAP: DIT, DN, y más

- **DIT (Directory Information Tree):** Es la estructura jerárquica en la que se organizan las entradas LDAP. El DIT se construye como un árbol invertido, con la raíz en la parte superior y las ramas extendiéndose hacia abajo. Las ramas representan las distintas divisiones de la organización, como departamentos o ubicaciones, y las hojas del árbol representan los objetos, como usuarios o dispositivos.

  ![dit](/aso/assets/img/linux/dit.png)

- **DN (Distinguished Name):** Como se mencionó anteriormente, el DN es la ruta completa a una entrada en el DIT. Es un identificador único para cada entrada en el directorio. Se construye concatenando los nombres de los nodos desde la entrada hasta la raíz, utilizando una estructura jerárquica.

  ```
  Ejemplo de un DN:
  
  uid=jperez,ou=clientes,dc=Empresa,dc=com
  ```

  - **uid=jperez**: Identificador único del cliente "jperez".
  - **ou=clientes**: Unidad organizativa "clientes".
  - **dc=Empresa,dc=com**: Dominio principal "Empresa.com".

- **Atributos y Objetos:** Las entradas en LDAP se componen de atributos, que son pares nombre-valor, y de clases de objeto, que definen qué atributos puede o debe tener una entrada. Por ejemplo, una clase de objeto `inetOrgPerson` puede tener atributos como `cn`, `sn` (surname o apellido), y `mail`.

- **Esquemas LDAP:** El esquema define las reglas sobre qué clases de objeto y atributos pueden existir en el directorio. Establece la estructura de los datos permitidos en el directorio, definiendo qué tipos de objetos (como usuarios, grupos, etc.) pueden almacenarse y qué atributos puede tener cada uno. Los esquemas son cruciales para garantizar la coherencia de los datos dentro del DIT.

### 3.3 Formato de intercambio de datos LDIF (LDAP Data Interchange Format)

El formato **LDIF (LDAP Data Interchange Format)** es un estándar basado en **texto plano** que se utiliza para representar datos de un directorio LDAP y definir operaciones de modificación sobre dicho directorio.

En OpenLDAP, LDIF es esencial para:

- Construir la estructura inicial del **DIT**.
- Añadir usuarios, grupos y unidades organizativas en bloque.
- Modificar atributos existentes (correo, contraseña, grupo, etc.).
- Exportar datos del directorio para copias de seguridad o migraciones.
- Automatizar tareas de administración del directorio.

---

#### Sintaxis básica de una entrada LDIF

Una entrada se compone de:

- Una línea con el **DN (Distinguished Name)**.
- Varias líneas con atributos en formato `atributo: valor`.
- Una línea en blanco para separar entradas.

Ejemplo:

```ldif
dn: uid=usuario1,ou=People,dc=ejemplo,dc=com
objectClass: inetOrgPerson
objectClass: posixAccount
objectClass: top
uid: usuario1
cn: Usuario Uno
sn: Uno
uidNumber: 1001
gidNumber: 1001
homeDirectory: /home/usuario1
loginShell: /bin/bash
userPassword: 123456

### Actividades LDAP

> -reto- 
>
> [Práctica 1  Instalacion y configuración básica del servidor Open LDAP](https://angelabserrano.github.io/aso/pdf/UT4_Practica1.pdf)
>
> [Práctica 2  Creación de usuarios y grupos en  Open LDAP](https://angelabserrano.github.io/aso/pdf/UT4_Practica2.pdf)

