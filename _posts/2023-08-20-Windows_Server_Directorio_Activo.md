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

- **Dominio (Domain)** : Colección de objetos: usuarios, grupos, equipos, etc. Se representa por un nombre de dominio DNS. Ejemplo: empresa.local

- **Controlador de dominio (Domain Controller):** Es el servidor con el directorio activo instalado, que contiene la base de datos de objetos del directorio para un determinado dominio. 

- **Árbol de dominios (Tree) :** Los árboles están compuestos por uno o varios dominios. Estos dominios están dentro del mismo espacio de nombres.

  ![image-20230910113519819](/aso/assets/img/windows_server/image-20230910113519819.png)

- **Bosque (Forest) :** Colección de árboles. Los dominios dentro de un bosque establecen relaciones de confianza, y esto les permite compartir recursos. Los dominios dentro del bosque no comparten el mismo espacio de nombres.

  ![image-20230910115708152](/aso/assets/img/windows_server/image-20230910115708152.png)

- **Unidad organizativa** : Es un contenedor para organizar los objetos en un dominio, a la que se pueden asignar valores de configuración de directivas de grupo.

- **Catálogo Global (Global Catalog):** incluye una copia parcial de solo lectura que contiene información de los atributos más utilizados de los objetos del bosque.

  ![image-20230910115844695](/aso/assets/img/windows_server/image-20230910115844695.png)

- **DNS :** El objetivo principal es traducir un nombre de dominio a una IP

​	[www.microsoft.com](http://www.microsoft.com) => 2.21.180.244

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

![image-20230910121347212](/aso/assets/img/windows_server/image-20230910121347212.png)

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

![img](https://lh5.googleusercontent.com/Y-uBy35sDydQuu3RaGicxKMh7_t92npEunPy-h5FGcviszT52pfgJRakRBZBW2WIWLmWpalh7WK9yCSAGXjfcnbajOrThaMgB_lZ0FyYyR5kcPNShLvrrgeySEAOZ578ZKwptPKlMprifZAaJwzX5K0i=s2048)

![img](https://lh4.googleusercontent.com/B_Bew_qhCmNfTdaSTAQYMqyFXdgvjIj_zqybRNCnyu21MvPAJOu-4jVoMCuuUORDNamCo8ytBXSMZzzBDIRZeEj6h3IZhpZ6yRUP6gnrJdyCxRTWVFhhv9U4JkFX4cA7UhjnoJewLJ6zQZe3YnWBzUyn=s2048)

![image-20230910135549160](/aso/assets/img/windows_server/image-20230910135549160.png)



![image-20230910135626044](/aso/assets/img/windows_server/image-20230910135626044.png)

![image-20230910135654515](/aso/assets/img/windows_server/image-20230910135654515.png)



![image-20230910135709834](/aso/assets/img/windows_server/image-20230910135709834.png)

![image-20230910135739606](/aso/assets/img/windows_server/image-20230910135739606.png)

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

  

## 3. Gestión del directorio activo a través de la interfaz gráfica

### 3.1 Cuentas de usuario y equipo

- Una **cuenta de usuario** es un objeto que posibilita el acceso a los recursos del dominio. No siempre representan a personas concretas, sino que también pueden ser utilizadas como mecanismos de acceso para determinados servicios o aplicaciones de la máquina local o, incluso, de un equipo remoto. 

>  -info- Cada cuenta de usuario dispone de un identificador de seguridad (**SID****,** **Security IDentifier**) que es único en el dominio.

- Una **cuenta de equipo** sirve para autenticar a los diferentes equipos que se conectan al dominio, permitiendo o denegando su acceso a los diferentes recursos del dominio. Aunque una cuenta de equipo se puede crear de forma manual (como veremos más adelante), también se puede crear en el momento en el que el equipo se une al dominio.
