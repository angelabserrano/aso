---
typora-copy-images-to: ../assets/img/windows_server
typora-root-url: ../../
layout: post
title: Windows Server - Directorio Activo
categories: wserver
conToc: true
permalink: wserver-directorio-activo
---

## 1. Conceptos básicos de Active Directory

El **Directorio Activo** (también conocido como **Active Directory** en inglés) es un servicio de directorio de red desarrollado por Microsoft. Su objetivo principal radica en proporcionar un servicio centralizado para la gestión y organización de recursos de red, como usuarios, grupos, impresoras y otros dispositivos, facilitando así la administración, autenticación y autorización en entornos empresariales de manera eficiente y segura.

El Directorio Activo incluye componentes **lógicos y físicos**.

![image-20240411133253794](/aso/assets/img/windows_server/image-20240411133253794.png)

### 1.1 Componentes lógicos del Directorio Activo

La **estructura lógica** se centra en la administración de los recursos de  la red organizativa, independientemente de la ubicación física de dichos recursos, y de la topología de las redes subyacentes.  

Los componentes de la estructura lógica del Directorio Activo son:

- **Objetos**: Son los componentes básicos de la estructura lógica representan a  usuarios y recursos como equipos e impresoras. Las clases de objetos son esquemas o plantillas de los tipos de objetos que pueden crear en  el directorio activo.

- **Unidades organizativas**: Es un contenedor para organizar los objetos en un dominio, a la que se pueden asignar valores de configuración de directivas de grupo.

- **Dominios (Domain)**:  Colección de objetos: usuarios, grupos, equipos, etc. Se representa por un nombre de dominio DNS. Ejemplo: empresa.local

- **Árboles de dominios (Tree)**: Los árboles están compuestos por uno o varios dominios. Estos dominios están dentro del mismo espacio de nombres.

  ![image-20230910113519819](/aso/assets/img/windows_server/image-20230910113519819.png)

- **Bosque (Forest)**: Colección de árboles. Los dominios dentro de un bosque establecen relaciones de confianza, y esto les permite compartir recursos. Los dominios dentro del bosque no comparten el mismo espacio de nombres.

  ![image-20230910115708152](/aso/assets/img/windows_server/image-20230910115708152.png)

### 1.2 Componentes físicos del Directorio Activo

Los elementos de la estructura física son los siguientes:

- **Sitios**: En una red física, un sitio representa un conjunto de equipos conectados mediante una línea de alta velocidad, como una red de área local. En AD, los sitios representan la estructura física, o topología de red. Es importante distinguir entre sitios y dominios. Lo sitios representan la estructura física de red, mientras que los dominios representan la estructura lógica de la organización.
- **Controlador de dominio (Domain Controller):** Es el servidor ejecutando Windows Server  con el directorio activo instalado, que contiene la base de datos de objetos del directorio para un determinado dominio. 

Cada **controlador de dominio** contiene varias particiones del Directorio Activo:

1. **Particiones del dominio:** contienen las réplicas de todos los objetos en ese dominio. Esta partición se replica solamente a otros Controladores de Dominio del mismo dominio. 
2. **Particiones de configuración**: contienen la topología del bosque. La topología que es el esquema de conexión de los sitios, registra todas las conexiones de los controladores de dominio en el mismo bosque.
3. **Particiones del esquema**: contiene el esquema del bosque. Cada bosque tiene un esquema para que la definición de cada clase del objeto sea única. Las particiones de configuración y esquema se replican en cada Controlador de Dominio del bosque.
4. **Particiones de aplicaciones**: contienen los objetos relacionados a la seguridad y se utilizan en las aplicaciones. Se replican en Controladores de Dominio especificados en el bosque. 

![img](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEja0uuhQ2tw0530Vsgcmc5pmB7lrZ9creC3LMTbK-moDTslUv22VDfvsYZ8-U9L2GyEUfqp-Nd2mpXms9V3jRiCo2buvA0unWV9baOAfQUfS842ZOOZmH7vqMKyMAVRU40tTsaJZE9ysEDV/s1600/7.png)

- **Catálogo Global (Global Catalog):**   Es un servidor que almacena una copia completa de todos los objetos del directorio para su dominio host y una copia parcial de solo lectura de todos los objetos del resto de dominios del bosque. 

  ![image-20230910115844695](/aso/assets/img/windows_server/image-20230910115844695.png)



## 2. Instalación de Active Directory

Existen 3 métodos de instalación:

- Mediante PowerShell

- - Install-WindowsFeature AD-Domain-Services
  - Install-ADDSDomainController

- Mediante el administrador del servidor

- Mediante dcpromo /unattend:<path> 

### 2.1 Instalación de Active Directory mediante el Administrador del Servidor

- Realizamos una instalación limpia de Windows Server 2019 con interfaz gráfica (GUI) en VirtualBox. 

  ![image-20230910121125218](/aso/assets/img/windows_server/image-20230910121125218.png)

- El adaptador de red en VirtualBox lo cambiamos a **Red Interna.**

![image-20230910121215311](/aso/assets/img/windows_server/image-20230910121215311.png)

- Instalamos VirtualBox Guest Additions 

![image-20230910121259019](/aso/assets/img/windows_server/image-20230910121259019.png)

- Renombramos el nombre del equipo a **empresa-DC1**

![image-20231007202930334](/aso/assets/img/windows_server/image-20231007202930334.png)

- Abrimos el **Administrador del Servidor**

  - Seleccionamos **Servidor Local**

    ![image-20230910121710000](/aso/assets/img/windows_server/image-20230910121710000.png)

- Un controlador de dominio (DC) no puede tener una IP dinámica, así que la cambiamos por la siguiente estática:

![image-20230910121803201](/aso/assets/img/windows_server/image-20230910121803201.png)



- A continuación hacemos click en **Administrar -> Agregar roles y características** (Parte superior derecha del Administrador del Servidor)

![image-20230910121844060](/aso/assets/img/windows_server/image-20230910121844060.png)

![img](https://lh4.googleusercontent.com/Y5areCLP1bKHQ-iTCb89jfMnE4qnmUbBk9UplMlAMunAipnZ0f5XDhoBPhR8Rbjdxm46Po2cvAZpoxYFmfQLx9eoyPWJrMWlzi9aXRu6gPUZo-bM_NdRA9JOOy1760dU8K-wSun7_qCMY5eHXFuPe4Jk=s2048)

![img](https://lh4.googleusercontent.com/IJLTPO1XUX0QTxemfPECs8LjP1VO5jw-TzMsxplaVnKoCbhfZDX0Rb3YJ0ZtFk4q7ZACFRY7y0hKO4r0M6rEaqMIVZUglfOn_71G1V8O4xft91O7jHxT2mpQawUAmc-BYFc-P6ZdcxD3w7NtmuHr4Ff6=s2048)



![image-20230910122001429](/aso/assets/img/windows_server/image-20230910122001429.png)

- En las siguientes pantallas hacemos clic en Siguiente y dejamos las opciones por defecto. Finalmente presionamos el botón de **Instalar**

![img](https://lh6.googleusercontent.com/3lGshqsZ3s49c7fxaH2EnCNU4sLnGftoWMjcaOYS65OxnfM4ifrP4x2CS4cuWtRxeibVV8-A_sfiZI7yuPkkXuii9AhMM2G-zD7ktwjIy6pli-w7GRrT-Bw8UlTV5l50F1KCShxtp8XiSfhIXJhr6STY=s2048)

![img](https://lh4.googleusercontent.com/eEE-jvDDhbGiABwjbpOKlVCneSW9zEl-UYF7DPOx1kPasyL_yLtav5kbt2h8PpNN9keOFFNiBEmMqR7A4xN8q6DAH6OQKVX5wyowTaZx7vSH607YIwOeKLAMQM0FHW6c0ezRiiwfSWqhk6xzs7Fn5CHk=s2048)



En esta pantalla debemos indicar el tipo de operación que queremos realizar. En este caso, como no disponemos de infraestructura previa, seleccionamos la opción de **Agregar un nuevo bosque**.



![img](https://lh5.googleusercontent.com/Y-uBy35sDydQuu3RaGicxKMh7_t92npEunPy-h5FGcviszT52pfgJRakRBZBW2WIWLmWpalh7WK9yCSAGXjfcnbajOrThaMgB_lZ0FyYyR5kcPNShLvrrgeySEAOZ578ZKwptPKlMprifZAaJwzX5K0i=s2048)

En el siguiente paso (*Opciones del controlador de dominio*) indicamos el nivel de funcionalidad del controlador.

![img](https://lh4.googleusercontent.com/B_Bew_qhCmNfTdaSTAQYMqyFXdgvjIj_zqybRNCnyu21MvPAJOu-4jVoMCuuUORDNamCo8ytBXSMZzzBDIRZeEj6h3IZhpZ6yRUP6gnrJdyCxRTWVFhhv9U4JkFX4cA7UhjnoJewLJ6zQZe3YnWBzUyn=s2048)

![image-20230910135549160](/aso/assets/img/windows_server/image-20230910135549160.png)



![image-20230910135626044](/aso/assets/img/windows_server/image-20230910135626044.png)

![image-20230910135654515](/aso/assets/img/windows_server/image-20230910135654515.png)



![image-20230910135709834](/aso/assets/img/windows_server/image-20230910135709834.png)

> -info- Ver script nos permite obtener un script en PowerShell para automatizar la instalación sin tener que volver a introducir de nuevo todos los datos. 

![image-20230910135739606](/aso/assets/img/windows_server/image-20230910135739606.png)

En la pantalla de **Comprobación de requisitos**, se verifica que el sistema cumple todos los requisitos para convertirse en controlador de dominio. 

![image-20230910135904288](/aso/assets/img/windows_server/image-20230910135904288.png)



### 2.2 Verificación de la instalación

- Accedemos a Windows Server con la cuenta del Administrador.

![img](https://lh4.googleusercontent.com/_pzepUPUa9uAJgd64nLVq_Cyx4O1sOAMh-Km4dp-FKzPiFaL4SGFy1J-WwHfGYxLmNDwrphjVoO5BziKPcyut0Dtk7aIpqXw7lQcRT-epU24wjcm3e1Mbp4-uEmEhXsWUWRDOLtAJ4jxB_bE_JEVnjlx=s2048)



- Accedemos al "Administrador del Servidor" => Herramientas => Usuarios y equipos de Active Directory.

![image-20230910140658068](/aso/assets/img/windows_server/image-20230910140658068.png)



- Observamos como muestra el dominio EMPRESA.LOCAL que ha sido creado.

![img](https://lh4.googleusercontent.com/XMNFOPF6eD602OgPNsYUfxJLu99CpQQO0mcDOb4C5KWXw4UAVCVQpDnuYc57KeFziRTcAHgQgJyMm-bqZxqhnEk_FdeSgLKOeL4d0JoIevliBSqiLsLTdcmdSe_5v4AEBm8lOZ08-MQN8vYRULlqA0_F=s2048)

![image-20230910140734020](/aso/assets/img/windows_server/image-20230910140734020.png)

![img](https://lh4.googleusercontent.com/yUmDVglpYez9_IevKSIxAq85vDDmcoanZImBxXvEOVMyQlTQD1GaLa7_XylzpVjq1jiyPez5EmiloBSZG5FmBXXjScZA5GB5sk_kHDSRa8DycTl2UAFNOdcerHY0KnuqB2WyPw6VmDS-lbkUEvaCjs-8=s2048)

![image-20230910140821280](/aso/assets/img/windows_server/image-20230910140821280.png)



### 2.3 Unir un cliente Windows a un dominio

- Importamos en VirtualBox la máquina virtual de Windows 10 o Windows 11. No olvides marcar la opción de resetear MAC Address de las tarjetas de red.
- El adaptador de red en VirtualBox lo cambiamos a **Red Interna**.
- Arrancamos la máquina y accedemos a la configuración de red y cambiamos la dirección IP y la dirección de servidor DNS:

![img](https://lh6.googleusercontent.com/DClXtRLy_ykYb6i2GpuQoZYWRApAlmgr7Tt_96fZ21jIUIjK6au9lM6iRrn2BlNQ1WEwzapF81kw3plkN1LDWtBOc3yIy7yIB8H8aXuFfeCslvA031tfL-A6X6vyJ1PWRFoebxlyWjW1SKiDWoxgvf4D=s2048)

- Accedemos a las propiedades del equipo para unir al dominio EMPRESA.LOCAL

![img](https://lh4.googleusercontent.com/epg1ZGhuuG_AX-rBv2srTRyGk_8JXYEBGx2ZkHFCPCMaZ0ue_ixhmnbLIHbF_WzFkqeLV8PogvJouGoBY863NGRwYF-Wb3LHU4r77sRIlyFVMFqpKBfOy_1rWtDXSZpwZpCbALDi8AVpeNKuKw_MpZ7O=s2048)

![img](https://lh5.googleusercontent.com/EIH2MrLwMu99fpTre9bzCoTaLcGZDg1RhbGOk0tGhqwwetRDqk7T4FAkBYvc4lPqf2P9HCKApAzWE5a_kvTSBZKsnEw8kjanKexMxsUcsbVHLpKKXTYihPyukGbf8wpKKHQ_2te_q3vaZ346bhXK8odb=s2048)![img](https://lh5.googleusercontent.com/KKpciExE__zrDR_dERIZfS0Po23AuAysGFu49BovLcgfSJChLK9ZGNjYa5UelqzvirfTIsbQhVNd-gycm7H2uhPV4o1LeQdV53yAIdzA-JAV51eWf18rSRgQs_KPk2w8aLcV4sPM7Dl956pXf3jDrUhl=s2048)



> -alert- En caso de error:
>
> - Verificar la dirección IP del cliente y del servidor que se encuentren en la misma red
>   - Realizar ping del cliente a la dirección IP del servidor: **ping 172.16.0.10**
> - Verificar el servidor DNS
>   - Realizar **ping empresa.local**

- En caso de estar todo bien configurado nos pedirá las credenciales de Administrador del servidor para poder unir el cliente al dominio.

  ![img](https://lh6.googleusercontent.com/QD8nqguTaESykSu8ubgkESKdAYldxqxCKxWKtxlMAtYa20CgxyoFKy1eoX6S3VNDu0vDU0zRgULAL4LjO5D4We9wt69RPKnUHWB-Mo5PDY3-jrldYDGWAOYf63ThYxkX7jRrBDWWFb55tbcjX-qJg_k4=s2048)![img](https://lh3.googleusercontent.com/qGEF309tmQmpKGThQWXFpOF2QFETP4OvPj6NnJRwq39vrul9yAEq4vjMq7z39cAN6Lne7677jrOfhE6Rm9aEoyqUoJlBoqy5wbZzZzSplsDZ6_gVORu2gCzHM0ZuoEgGVT1MxlHe1qhYW9ZZv-D_ayrg=s2048)

  

## 3. Degradar un controlador de dominio desde la interfaz gráfica

La degradación del controlador de dominio se divide en dos pasos:

- En primer lugar procederemos a la degradación del controlador de dominio. Al final de este paso, el servidor dejará de actuar como controlador de dominio.
- A continuación, desinstalaremos los roles *Servicios de dominio de Active Directory y DNS*.



En el **Administrador del servidor**, desplegaremos el menú **Administrar** y elegiremos la opción **Quitar roles y funciones**.

![image-20231007195424356](/aso/assets/img/windows_server/image-20231007195424356.png)



A continuación elegimos la opción "**Seleccionar un servidor del grupo de servidores**".

![image-20231007203317189](/aso/assets/img/windows_server/image-20231007203317189.png)

En la página Quitar roles de servidor, buscamos en la lista la entrada Servicios de dominio de Active Directory y hacemos clic para desmarcarla.

![image-20231007195714453](/aso/assets/img/windows_server/image-20231007195714453.png)



Después nos aparece un diálogo que nos indica que para eliminar los Servicios de dominio, también tendremos que eliminar las características.

![image-20231007195908139](/aso/assets/img/windows_server/image-20231007195908139.png)



Se realiza una validación para ver si se cumplen todos los requerimientos que permitan desinstalar el rol y muestra un error. 

![image-20231007203356399](/aso/assets/img/windows_server/image-20231007203356399.png)



Hacemos clic en **disminuir el nivel del controlador de dominio** para poder proceder con la desinstalación.

Hacemos clic sobre **Forzar la eliminación de este controlador de dominio.** 

![image-20231007203507554](/aso/assets/img/windows_server/image-20231007203507554.png)



Para continuar, debemos marcar la opción *Continuar con la eliminación*.

![image-20231007203609424](/aso/assets/img/windows_server/image-20231007203609424.png)



Escribimos la contraseña para la cuenta de Administrador.

![image-20231007203713083](/aso/assets/img/windows_server/image-20231007203713083.png)



Hacemos clic en **Disminuir nivel**

![image-20231007203809019](/aso/assets/img/windows_server/image-20231007203809019.png)



Después, el sistema comenzará a reiniciarse.

![image-20231007204612720](/aso/assets/img/windows_server/image-20231007204612720.png)





Una vez terminado el proceso de Disminur nivel, debemos desinstalar los roles *Servicios de dominio de Active Directory* y *DNS*. 

En el *Administrador del servidor*, desplegaremos el menú *Administrar*. Y elegimos la opción Quitar roles y funciones.

![image-20231007204912200](/aso/assets/img/windows_server/image-20231007204912200.png)



Seleccionar un servidor del grupo de servidores

![image-20231007204947091](/aso/assets/img/windows_server/image-20231007204947091.png)

Y desmarcamos la opción de "Servicios de dominio de Active Directory"





## 4. Gestión del directorio activo a través de la interfaz gráfica

### 4.1 Cuentas de usuario y equipo

- Una **cuenta de usuario** es un objeto que posibilita el acceso a los recursos del dominio. No siempre representan a personas concretas, sino que también pueden ser utilizadas como mecanismos de acceso para determinados servicios o aplicaciones de la máquina local o, incluso, de un equipo remoto. 

>  -info- Cada cuenta de usuario dispone de un identificador de seguridad (**SID****,** **Security IDentifier**) que es único en el dominio.

- Una **cuenta de equipo** sirve para autenticar a los diferentes equipos que se conectan al dominio, permitiendo o denegando su acceso a los diferentes recursos del dominio. Aunque una cuenta de equipo se puede crear de forma manual (como veremos más adelante), también se puede crear en el momento en el que el equipo se une al dominio.

Para crear una cuenta de usuario acceder al menú **Herramientas** del **Administrador del Servidor**

![img](https://lh4.googleusercontent.com/2AO1H1nDtDIACHLJw9H4AMT3k4L5oMe_lI6gF1mbSAaa_IlLBBY1u6bmfrw7NrwGYZFxq2Gj8SR27OfQnZcKtAGWFbgUj4AI3WUTH64dADTEW6jSJtyiIxkaEA5acyzk4fdodRUgyJvjoaS2a5xSInllVQ=s2048)

![img](https://lh5.googleusercontent.com/0KARPXuboJSRtPBVECjA0A2kO7jaNfFy1PHEjNF3pGie6qaSakIcLjjT4kZdfPFDSNH2m3Zd3yChjhyvdC0tfTthk10FppSt-SCF60SZSTyS7pHF_X3-tsRrOzTjVPzNlNiTw4COWITLiJiCHgH6b2Vf4g=s2048)

- Creación de un nuevo Usuario

  ![img](https://lh6.googleusercontent.com/7erZe9BrNMNVOq_bZ3lCuXWwhn3jQmnkSU-mVY432IlFKK5Q87eds14wTbuBZ6zhGMiKKahwTzIIt3WhSumJ5hcl-QcnmkLo_Aa_stZfdKsEdLqACvsRbL34bABl8gn6cKn_wzBfYHo_Xbz0BeYxKNjikw=s2048)

  Una vez creado un usuario, podemos cambiar sus propiedades.

  ![image-20230917113354040](/aso/assets/img/windows_server/image-20230917113354040.png)

  ![image-20230917113410413](/aso/assets/img/windows_server/image-20230917113410413.png)

  **Pestaña: Cuenta**

  **Establecer horas de inicio de sesión**

  ![image-20230917113501840](/aso/assets/img/windows_server/image-20230917113501840.png)

**Pestaña: Cuenta**

**Limitar los equipos desde los que un usuario puede acceder**

![image-20230917113539602](/aso/assets/img/windows_server/image-20230917113539602.png)

El **perfil de un usuario** consiste en la personalización del entorno. Por defecto, se crea una carpeta en el equipo en el que se inicia sesión, pero esto puede modificarse.

- **Perfil móvil:** El usuario dispondrá de su personalización en todos los equipos del bosque en los que se autentifique.
- **Perfil obligatorio**: El usuario no podrá personalizar su entorno. Podrá hacer modificaciones pero al iniciar sesión de nuevo se habrán perdido los cambios. 

**Pestaña: Perfil** 



![img](https://lh3.googleusercontent.com/CZSjYC_lkk2J9FXSihvmVcm9WSQcWRH66MjO7Vr0jURtoO7BQCXtcLEqQHzmQncbO7xpjcdRIM8j_mgs1PZhgOX6T4fySZgX8CJflClGEkfJPz9M17FLhZJpxThPfrSF8MrugMO4ww6XQEgc7KkUhym8fw=s2048)

**Ruta de acceso al perfil**: Indica donde se guardará el perfil. Si ponemos una ruta de red tendremos un perfil móvil.

**Script de inicio de sesión:** Se puede asociar un script para que se ejecute cada vez que el usuario inicie sesión.

**Pestaña: Miembro de**

**Agregar / quitar grupos a los que pertenece un usuario**

![img](https://lh3.googleusercontent.com/VfkW3SdhutiPhQt8GvRAAwdPUpoLkk0ewPc4Qto_HAB1isPS7JhRUa1CZtpXRm5F5ruFhasZmiGfs0ycfkjLUvSE76wzURjE6Zmvb8XbKWpAZgXzWymtTo17-uSvr8Wmjxd9xwlABlBxenMeReNv_7y7Ag=s2048)

![img](https://lh6.googleusercontent.com/fLJFYWdoDXQISQQ18L9EBRi_N_IZYWIYbhC1EmWXDZIh14Yv-QQHU-boxqcmbqT9rbMmgUV2tPjXDQOJiHYX2mg-vNqhL1KE7P1eyE__fKspYGtlZUqtYYpTti4wcbA3wS23BBWAork3KsKRbLe9oY9pbA=s2048)







- Creación de un nuevo equipo

  ![img](https://lh3.googleusercontent.com/pDqRQFN0xQg6A30QEiSAPp_n5klyxB0W5ab45Rnu_zIfbGhqBixYM-hel02yqBuv2jyQtuzEP_Dkv3PbX7C50sIin0t4Ndq1QCezmMwLGJHNVyi8kF0pylgjhEL3pvkP6QuuAZHrnJUyEOir29vAqhCivw=s2048)



### 4.2 Cuentas de grupo

Una cuenta de grupo es una colección de cuentas de usuario que se puede utilizar para asignar un conjunto de permisos y derechos a varios usuarios al mismo tiempo. Un grupo también puede contener contactos, equipos y otros grupos.

Para crear una cuenta de grupo acceder al menú **Herramientas** del **Administrador del Servidor => Usuarios y equipos de AD**

![img](https://lh6.googleusercontent.com/EeaYgp_eN8g7ARDIVlQubgJ0-sOLztriJmSgl8XHv-t3GQwn355FYZM2Je7xezky6fQcvBsOMFo4IywHlcDhCHFLjcrdHrzVEEEzrk8_v2iG4ZZGFVzwfmWH8SaQtXmeC1dwHgl5Sb7oCUHhDwmSzmAOYQ=s2048)

#### 4.2.1 Tipos de grupos

Existen dos tipos de grupos:

- **Distribución**: Para crear listas de distribución de correo electrónico.

- **Seguridad:** Para asignar permisos a los recursos compartidos

  

#### 4.2.2 Ámbitos de un grupo

El ámbito de un grupo establece su alcance, es decir, en qué partes de la red puede utilizarse, y el tipo de cuentas que pueden formar parte de él.



| Ámbito de grupo   | El grupo puede incluir como miembros ...                     | Al grupo se le pueden asignar permisos en ... |
| ----------------- | ------------------------------------------------------------ | --------------------------------------------- |
| **Universal**     | - Cuentas de cualquier dominio del bosque<br />- Grupos globales de cualquier dominio del bosque <br />- Grupos universales de cualquier dominio del bosque | Cualquier dominio del bosque                  |
| **Global**        | - Cuentas del mismo dominio del grupo<br />- Grupos globales del mismo dominio del grupo | Cualquier dominio del bosque                  |
| **Dominio local** | - Cuentas de cualquier dominio <br />- Grupos globales de cualquier dominio<br />- Grupos universales de cualquier dominio<br />- Grupos locales de su dominio | Su dominio                                    |





> -alert- Los grupos universales se replican en los controladores de dominio que albergan el **catálogo global**. Cada vez que se deben comprobar los permisos se debe consultar el catálogo global. 

![image-20231003113646220](/aso/assets/img/windows_server/image-20231003113646220.png)

### 4.3 Unidades organizativas

Una **Unidad Organizativa** es un contenedor de objetos que permite organizarlos en subconjuntos, dentro del dominio, siguiendo una jerarquía. De este modo, podremos establecer una estructura lógica que represente de forma adecuada nuestra organización y simplifique la administración. Me permiten delegar permisos y asignar políticas de seguridad para uno o varios objetos.

Las unidades organizativas que vienen creadas por defecto son:

- **Builtin**: Grupos creados por defecto del sistema.
- **Computers**: Cuentas de equipo incorporadas al dominio.
- **DomainControllers**: Equipos que son controladores. 
- **Users:** Usuarios del dominio que se crean
- **ForeignSecurityPrincipals**: Contenedor para entidades principales de seguridad de dominios externos de confianza. No se debe modificar manualmente.

### 4.4 Directivas de grupo 

Las directivas de grupo son un **conjunto de reglas** que controlan el entorno de trabajo de **cuentas de usuario** y **cuentas de equipo**. Las directivas de grupo proporcionan la gestión centralizada y configuración de sistemas operativos, aplicaciones y configuración de los usuarios en un entorno de[ ](https://es.wikipedia.org/wiki/Active_Directory)Active Directory. 

Para gestiona las directivas de grupo:

 **Herramientas->Administración de directivas de grupo**

Las configuraciones de las directivas de grupo se encuentran en los objetos de directiva de grupo (**GPO**), que se vinculan con los siguientes contenedores de servicio de directorio de Active Directory: **sitios, dominios o unidades organizativas**. 

> -alert- **No pueden aplicarse a grupos.** Si se desea aplicar una GPO a un grupo debemos crear una UO y dentro de esta un nuevo grupo e incorporar a este los grupos y/o usuarios a los que queremos aplicar dicha política.

![img](https://lh5.googleusercontent.com/uqSkI1Ldm7Oq5BMkxluRynNo6-eXJ9ye4R20EwXi5eG6G3Ojruo71_FoYG_aWihZM774f-_HbqbNBP2T7qBIHE0Yyh1l_D-GJ9o5mukGS59Sp4S-2oxPKorGzXljT1UJZG6hDHT40Pc051Jss7CChdqK6Q=s2048)

**Default domain policy:** Es la política que se aplica a todo el dominio empresa.local, es decir, a todos sus usuarios y equipos. 

#### 4.4.1 Creación de una nueva directiva

![img](https://lh6.googleusercontent.com/YtBkDGrDpDXkj7pbLxr5YB_Vo3X5138JsG6ZBey6_BsNLfl_NhICI0flLYcf_Etuh-ubxqaO5rUwL5wzpdXaV86VKz9bonIjM_wPDjGIXzjnfKoGFJyTTgIb8hrXtSDMIhyXi10JBSeSqIu5TWj2kJlHXg=s2048)

![img](https://lh5.googleusercontent.com/6mft6rJXdqQE_pHz63wGu0t5BPIbexEWfIIzUZLk8JrJk1GXADSOmn5ymbiNSUmrb4Fl7PKtDLB_IiVOdQDquEFUxOhXFGEmpCtRDvMNsXsHfN1hlj8FLF8S2Cx18uqXhXFBQSWmvSRhvC-2QFPOtmz4lg=s2048)

![img](https://lh5.googleusercontent.com/6lxprGWu4okDhCf5za2FxZPxkuUn-O_SCCbE1toHSr9lD0W9T3fU-ZHzeKRdwUBIVCy6wtTP0-I7Nlbkh5vMGqLiwphn--vq4FW2yMQ2oQF4U71jkl-DkiscqEeBs09wkKs2VSDH1yR55HBpmh3OSGUtCw=s2048)



#### 4.4.2 Vinculación de una directiva a una Unidad Organizativa

Para ello, desde el Administrador de directivas de grupo (**gpmc.msc**), pulsaremos con el botón derecho sobre la unidad organizativa a la que queramos asignarle la directiva creada.

![img](https://lh3.googleusercontent.com/6Y75mWXtl9APPigTMyhXZ5FkqjL_RvNes0TQfW6ZPXzaX1YbCsiMwYxzkSBQb-UiX3IqB8dAWYCdjXpRR6IovgKvOQRxYr8ax6fx5g2Y9bltI_vjQdOJliOpk23ZI06r6I581N0dHGEeg33-4R95Eitzig=s2048)





#### 4.4.3 Orden de prioridad de las directivas de grupo

![img](https://lh4.googleusercontent.com/ab2V7DtF4PJFTgYGN5_NTnjXlPlELrrYCXK5Q9NPlu745l8d7keLmQJpNPBKK7EFF3ca54uHyYj4nvxo8leuKFSvE8KMRCEa1qlxuzshifUF6EHtlJXnh-6ul_lJCPDU0eDbW2Z5tM488t96cjFgBeGQfg=s2048)

Las GPO’s de una OU prevalecen sobre las del dominio, que a su vez prevalecen sobre las de sitio, las cuales a su vez prevalecen sobre las del equipo local. 

![img](https://lh5.googleusercontent.com/vikG8tpbK-RuFvBG8ValDRiNvURmUiKtmxPtZyuZNrq2_YONbXNsk8eXauDv1O8ob2dE2O_xaV9j_y6L1PdSY3oqUiEzslE3v2hMWAHR3qiLveIH1KzI_SW4OcLb1wkO0dka_iC0sZY-OGR2Al-DyJ3QCQ=s2048)



### 4.5 Permisos

Los sistemas operativos de la familia Windows poseen dos niveles de permisos para los recursos compartidos:

- **Permisos para carpetas compartidas**: se aplican cada vez que un usuario quiere acceder a un archivo o carpeta de la red.
- **Permisos para archivos y carpetas (NTFS)**: se aplican sobre dispositivos con formato NTFS para definir en mayor detalle las acciones permitidas.

- Si accedemos en modo **local** a los archivos o carpetas sólo intervienen los **permisos NTFS**

- Si se accede a través de la red se aplican los **dos niveles de permisos**: 

- - 1º Permisos de carpetas compartidas
  - 2º Permisos NTFS

- ![img](https://lh3.googleusercontent.com/L4rjQfrGZi7nrRN4T51M39YB0xZYvjciSiZY2J1i3tJhLwNbDihCSPlNRDeJ6_6J9haU90KVEH8T0bTsoaDMOR8L-9VoGwzEfMOnANVSIPuETBSX_bVUaeXGam4_RjKREgELFzRBz_oJz4-KlfkpedQBAw=s2048)

#### 4.5.1 Permisos de recursos compartidos

![img](https://lh3.googleusercontent.com/aFVKj4-bLFtYL8IjjcjDTfPBr9mtTBl8Bg17vqe51dm5W3K0mjt-rIAaxgiOBEJr7oEqx_yaghgrbV20dAYTaaqYotPzZmfRUDmbr020hAbGl4vXLBJYzdQBm6IiqkfyI2A4IStjRF_vNhL_U-D7wOc0xA=s2048)

![img](https://lh3.googleusercontent.com/D6GQm-qnrhjZIGfYQqoh1bmPgx-a97DWQrD5LsAqDQRedCR81P6RQ3b3uRbCuKkxQ_Qj6Aug-ehul86VSbuNtJbmp7RytgBWVMus8dH5j00xQrbryxRZ1jE8DHNh60826vbKHBIaz685bnYG1GuvOUHmWQ=s2048)

 

   

![img](https://lh6.googleusercontent.com/kc7vZEe25XJhoED6JD9sgr9RwyKZo5-lciPeybtgtP6vXbGih6TcPt2ZG_YGEnJuoTRz90jXzLTZ1sDPTGb0l0Pm5u5ziGed553S4VLE1oZe8BJiDxS2iDuQC-PTwzcBnTQ42o4EgFlUhge0M6VZwGvmsQ=s2048)

![img](https://lh6.googleusercontent.com/WmbcvaX9faQDVYiXM3f4JWKdrh2kjTUbDIAgYCmkn90YK6LZ9nUcRthKry6-B0bVR_z98mo1GT3gv1IzDrEGgkHncktzuTybjyw8HjvxqrQMockS2KW_HDJSyCfiObsmdzN9v0p6lhYE1OVQP2So6Dyg4g=s2048)

![img](https://lh3.googleusercontent.com/YWA8YesWN5te_gesyJ7dnkY-4TH0AyZkOs2Q9TQJAeUpsjdhVxJxxkR9IKlHdh0oiKUHhe4Qzh6Vc77I-9v-i8vGFXxdncO1hCERMpdcPzRa6c4nvqCcbIVseFulmdB5Uuj2bFJPHqcInljQ_lKiYbempw=s2048)



![img](https://lh5.googleusercontent.com/VeX1-fc9L8kmutmSs2hu_i0Zi8ZWiI73cootKGqvnnHJb9DQYh1O3hvGdm8pr2nXKp2YEM87rBcCGDwQ_gEFMhyHvmXHlrpssgyhzuPvf1A5zExM7jctLszZD7XuBQi8zZNr33B6XlWdl6OhQhp6Jt-QFg=s2048)



**Tipos de permisos:**

**Control Total:** Todas las operaciones y cambio de permisos.

**Cambiar:** permite crear, modificar y borrar carpetas y archivos,.

**Lectura:** sólo permite la lectura y ejecución de archivos.

![img](https://lh4.googleusercontent.com/ozZtZs9FucA1-LKHJzpYumcV9hV5uONaV_L6V2VeWsbhSSPRbzkYKljhrAcmJu7GOjy3N9jy3Y3IfgD0Vs_gcwS6-cZ2Led__yn8cYcLOZ3q54FRutMtzdXc0Ycq9_X6i0_is3ZiTvGPsS2TYprxPOQiaw=s2048)



**Establecer permisos de recursos compartidos**

**1º Compartir con usuarios específicos** 

Seleccionar el recurso y hacer clic con el botón secundario **‘Compartir con ….’ y usuarios específicos.**

![img](https://lh3.googleusercontent.com/yHEOZvKq0OHmYPd6mqFD9IHs2omCoUtnwBbcQlPPdtTd_sbiFN7CQ1vtLAuSoR5-DaA8i5G8jSiZQI3xbrfKkkwf1p4fHjo2uFTE9lnTJ9hjzFjPzd_XwNcv-u4mcdE8rBR_X-eJoqZJxnAaQz9JkOhFKg=s2048)

**2º Compartir mediante el uso de Compartido avanzado**

![image-20231003120446770](/aso/assets/img/windows_server/image-20231003120446770.png)

#### 4.5.2 Permisos NTFS

**Los Permisos NTFS** permiten controlar qué usuarios y grupos puede tener acceso a archivos y carpetas en un volumen NTFS. 

Podemos asignar los siguientes permisos:

![img](https://lh5.googleusercontent.com/gnErA5oK7nF06-K_Ot_OHrVXd9LH06GOj3Pmz4uUsBXyfEhmKzzjxfQP3Eu-rxF1y03wtInRKo1nuckYoleZSkFBln7z7q66Hdx9mj5YOoYxbxdEVb3CfTEuCDMiRiyFjvtY0yaoWO4bGIR_GYIjEAX2Pw=s2048)

- **Control total.** Otorga todos los permisos posibles, incluido el control total sobre los permisos NTFS y los permisos de compartir.
- **Modificar.** Permite leer, escribir, modificar y eliminar archivos y subcarpetas, así como ejecutar archivos.
- **Lectura y ejecución.** Permite ver el contenido de un archivo o carpeta y ejecutar archivos ejecutables, pero no permite modificarlos.
- **Mostrar el contenido de la carpeta.** Permite ver el contenido de una carpeta, pero no permite acceder a los archivos dentro de ella ni ejecutarlos.
- **Lectura.** Permite únicamente la lectura de archivos y carpetas, sin posibilidad de modificar o eliminar.
- **Escritura.** Permite crear nuevos archivos y carpetas, así como modificar o eliminar los existentes, pero no permite ver el contenido de la carpeta. 

![img](https://lh5.googleusercontent.com/FgYdt6u_xg4-yvztI5-9wsvSh4f0b0nTHT0kNO5Hyq_AWme1GRcl35MKzkmfb5HrOatTDxJu43CUSmRo111T93QCL1_pwSBKsF5A5HCPwi4HNGVXgq09hpBd8QE44S6-40FMQv8IET-2-TF6Ec_kKuvY3A=s2048)



**Permisos NTFS avanzados**

![image-20231003175922893](/aso/assets/img/windows_server/image-20231003175922893.png)

![img](https://lh6.googleusercontent.com/73HZcMWYHi1EXY8lN6Gqgi-uqHx6Khz3MdTB3lyR2L1zEpj4cQrH60HOG2XP6uemMbcXnYQPc3dnwJGTum8MinVNNSa1gwJUtT0j6uk8-UghLmh_5phwFlMeYKy2MIN2lLfenyspRe_9F-UBn_GkvJy8rQ=s2048)

![img](https://lh4.googleusercontent.com/W7KeYEvB286Ieo9H95XflYrWAsW57LNbflTKMw_Zk17XhdSajblambkEpTapUt3a8BCag2JGDxYDpvlbjm4lvxDyE_UQ70JUMtShes2R1SIR60yH0rKqLVY5IMpdmaF8wDI5NxJxOIcGIKkw6j5bbiDP1Q=s2048)



**Herencia de permisos**

Al crear un archivo o una carpeta en un volumen NTFS, ese objeto hereda automáticamente los permisos de su carpeta padre, y a la inversa. 

En ocasiones, puede interesarnos eliminar esa herencia de permisos. Podemos eliminarla de tres formas:

- Eliminar la herencia a nivel de la carpeta de nivel superior. Los objetos contenidos en ella dejan de heredar los permisos.
- Eliminar la herencia a nivel de subcarpeta o archivo contenido dentro del recurso principal.
- Permitir o denegar explícitamente un permiso de manera diferente a como está definido en el recurso contenedor. 

Para *eliminar la herencia* seguimos los siguientes pasos:

1 - Se selecciona el recurso con el botón derecho y se pulsa **Propiedades**

2 - A través de la pestaña **Seguridad** accedemos a **Opciones avanzadas**

3 - En el cuadro que aparece, en la pestaña **Permisos**, se pulsa el botón **Deshabilitar herencia**. 

4 - Al pulsar en **Deshabilitar herencia** hay dos opciones:

- Convertir los permisos heredados en permisos explícitos: mantiene los permisos de todos los archivos y subcarpetas, pero no están vinculados a los de nivel superior.
- Quitar todos los permisos: elimina todos los permisos heredados.

Como norma general se marcará la primera opción, convertir los permisos en permisos explícitos.





### 4.6 Perfiles

Podemos definir un perfil como aquellos aspectos de configuración del equipo y del entorno de trabajo propios del usuario y que además son exportables a otras máquinas de manera transparente al mismo. mediante los perfiles conseguimos que el usuario independientemente del equipo en el que inicie la sesión disponga de un entorno de trabajo similar.

Existen tres tipos de perfiles:

- **Perfiles locales** : se almacenan en el equipo
- **Perfiles móviles**: se almacenan en el servidor
- **Perfiles obligatorios**: son perfiles móviles de solo lectura. Sólo el administrador puede modificarlos.

Hay que tener en cuenta de que cuando un usuario con perfil móvil inicia la sesión, la información del servidor se copia al cliente. Cuando cierra la sesión se realiza la operación inversa. Un alto número de usuarios con perfil móvil puede **sobrecargar la red** demasiado. 



