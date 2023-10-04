---
typora-copy-images-to: ../assets/img/powershell
typora-root-url: ../../
layout: post
title: Administracion del servicio de directorio en Windows con PowerShell
categories: scripts
conToc: true
permalink: powershell-directorio-activo
---

## 1 Gestión de usuarios de Active Directory con PowerShell 

### 1.1 Creación de cuentas de usuario 

El cmdlet [**New-ADUser**](https://learn.microsoft.com/es-es/powershell/module/activedirectory/new-aduser?view=windowsserver2022-ps) crea un usuario en el directorio activo.

**Ejemplo:**

```powershell
New-ADUser -Name "Maria Garcia" -Path "CN=Users,DC=Empresa,DC=Local" -SamAccountName "mariag" -UserPrincipalName "mariag@empresa.local" -AccountPassword (ConvertTo-SecureString "aso2023." -AsPlainText -Force) -GivenName "Maria" -Surname "Garcia" -ChangePasswordAtLogon $true -Enabled $true
```

**Explicación detallada:**

- `New-ADUser`: Este cmdlet se utiliza para crear un nuevo usuario en Active Directory.

- `-Name "Maria Garcia"`: Especifica el nombre de visualización del usuario.

- `-Path "CN=Users,DC=EMPRESA,DC=LOCAL"`: Especifica la ubicación (unidad organizativa) donde se creará el nuevo usuario.

- `-SamAccountName "mariag"`: Especifica el nombre de usuario (sAMAccountName) para el usuario. Asegúrate de que sea único dentro de la ruta especificada.

- `-UserPrincipalName "mariag@EMPRESA.LOCAL"`: Especifica el Nombre Principal de Usuario (UPN) para el usuario. El UPN también debe ser único.

- `-AccountPassword (ConvertTo-SecureString "aso2023." -AsPlainText -Force)`: Establece la contraseña inicial para el usuario. En este ejemplo, la contraseña es "aso2023."

- `-GivenName "Maria"`: Especifica el primer nombre del usuario.

- `-Surname "Garcia"`: Especifica el apellido del usuario.

- `-ChangePasswordAtLogon $true`: Obliga al usuario a cambiar su contraseña en el próximo inicio de sesión. Esta es una buena práctica de seguridad para la configuración inicial de la contraseña.

- `-Enabled $true`: Habilita la cuenta de usuario. Si deseas crear la cuenta pero dejarla deshabilitada inicialmente, puedes establecer esto en `$false`.

### 1.2 Eliminación de usuarios

El cmdlet [**Remove-ADUser**](https://learn.microsoft.com/es-es/powershell/module/activedirectory/remove-aduser?view=windowsserver2022-ps) elimina un usuario del directorio activo.

Ejemplo:

```powershell
Remove-ADUser -Identity "mariag"
```

```powershell
Remove-ADUser -Identity "CN=Maria Garcia,CN=Users,DC=Empresa,DC=Local" 
```

### 1.3 Deshabilitar una cuenta de usuario

El cmdlet [Disable-ADAccount](https://learn.microsoft.com/es-es/powershell/module/activedirectory/disable-adaccount?view=windowsserver2022-ps) deshabilita una cuenta de usuario del directorio activo

Ejemplo:

```powershell
Disable-ADAccount -Identity "mariag" 
```

```powershell
Disable-ADAccount -Identity "CN=Maria Garcia,CN=Users,DC=Empresa,DC=Local" 
```

### 1.4 Modificación de cuentas de usuario

Podemos modificar alguna propiedad de la cuenta de usuario a través del cmdlet **[Set-ADUser](https://learn.microsoft.com/es-es/powershell/module/activedirectory/set-aduser?view=windowsserver2022-ps)**

```powershell
Set-ADUser -Identity "mariag" -EmailAddress "mariag@empresa.local"
```

### 1.5 Consultar usuarios

El cmdlet [**Get-ADUser**](https://learn.microsoft.com/es-es/powershell/module/activedirectory/get-aduser?view=windowsserver2022-ps) nos pemite consulltar las cuentas de usuario.

Para visualizar ejemplos de cómo utilizar el comando: 

```powershell
Get-Help Get-ADUser - Examples
```

Aquí tienes algunos ejemplos de cómo puedes utilizarlo:

1. **Obtener información de un usuario específico por su nombre de usuario**:

   ```powershell
   Get-ADUser -Identity mariag
   ```

   Este comando obtiene información sobre el usuario con el nombre de usuario "mariag".

2. **Obtener una lista de todos los usuarios en un dominio específico**:

   ```powershell
   Get-ADUser -Filter * -SearchBase "OU=Usuarios,DC=empresa,DC=local"
   ```

   Este comando recupera una lista de todos los usuarios dentro de la Unidad Organizativa (OU) "Usuarios" en el dominio "MiDominio.com".

3. **Obtener usuarios con un atributo específico**:

   ```powershell
   Get-ADUser -Filter {EmailAddress -like "*@miempresa.com"}
   ```
   
   Este comando busca y muestra todos los usuarios cuya dirección de correo electrónico contiene "@miempresa.com".
   
4. **Obtener usuarios que pertenecen a un grupo específico**:

   ```powershell
   Get-ADGroupMember -Identity "GroupName" | Where-Object { $_.objectClass -eq 'user' }
   ```
   
   Este comando obtiene una lista de usuarios que son miembros del grupo especificado ("GroupName").
   
5. **Obtener una lista de todos los usuarios activos**:

   ```powershell
   Get-ADUser -Filter {Enabled -eq $true}
   ```
   

Este comando recupera una lista de todos los usuarios que están habilitados en Active Directory, es decir, cuentas de usuario activas.



## 2. Gestión de grupos 

### 2.1 Creación de grupos

El comando [New-ADGroup](https://learn.microsoft.com/es-es/powershell/module/activedirectory/new-adgroup?view=windowsserver2022-ps) crea un nuevo grupo en el dominio especificado

Ejemplo:

```powershell
New-ADGroup -Name "Profesores" -GroupCategory Security -GroupScope Global -Path "CN=Users,DC=EMPRESA,DC=LOCAL"
```

### 2.2 Eliminación de grupos 

El cmdlet **[Remove-ADGroup](https://learn.microsoft.com/es-es/powershell/module/activedirectory/remove-adgroup?view=windowsserver2022-ps)** elimina un grupo del dominio.

```powershell
Remove-ADGroup -Identity "CN=Profesores,CN=Users,DC=EMPRESA,DC=LOCAL" -Confirm:$false
```

### 2.3 Modificación de grupos

El cmdlet **[Set-ADGroup](https://learn.microsoft.com/es-es/powershell/module/activedirectory/set-adgroup?view=windowsserver2022-ps)** modifica las propiedades de un grupo del dominio.

```powershell
Set-ADGroup -Identity Profesores -GroupScope Universal
```

### 2.4 Consultar grupos

El cmdlet **[Get-ADGroup](https://learn.microsoft.com/es-es/powershell/module/activedirectory/get-adgroup?view=windowsserver2022-ps)** muesetra todas las propiedades de un grupo del dominio.

```powershell
Get-ADGroup -Identity Profesores
```

### 2.5 Añadir usuarios a un grupo del dominio

El cmdlet **[Add-ADGroupMember](https://learn.microsoft.com/es-es/powershell/module/activedirectory/add-adgroupmember?view=windowsserver2022-ps)** añade usuarios al grupo especificado

Ejemplo:

```powershell
Add-ADGroupMember -Identity "Profesores" -Members mariag,pepe
```

### 2.6 Quitar usuarios de un grupo del dominio

El cmdlet **[Remove-ADGroupMember](https://learn.microsoft.com/es-es/powershell/module/activedirectory/remove-adgroupmember?view=windowsserver2022-ps)** quita usuarios del grupo especificado

Ejemplo:

```powershell
Remove-ADGroupMember -Identity "Profesores" -Members mariag
```

3.7 Consultar miembros de un grupo

El cmdlet Get-ADGroupMember nos permite consultar  

## 3. Gestión de unidades organizativas de Active Directory con PowerShell

### 3.1 Creación de unidades organizativas

El cmdlet [**New-ADOrganizationalUnit**](https://learn.microsoft.com/es-es/powershell/module/activedirectory/new-adorganizationalunit?view=windowsserver2022-ps) crea una unidad organizativa.

Ejemplo:

```powershell
New-ADOrganizationalUnit -Name "Empresa" -Path "DC=EMPRESA,DC=LOCAL" -Description "Unidad Empresa"
```

```powershell
New-ADOrganizationalUnit -Name "Finanzas" -Path "OU=EMPRESA,DC=EMPRESA,DC=LOCAL" -Description "Unidad de finanzas"
```

### 3.2 Eliminación de unidades organizativas

El cmdlet **[Remove_ADOrganizationalUnit](https://learn.microsoft.com/es-es/powershell/module/activedirectory/remove-adorganizationalunit?view=windowsserver2022-ps)** elimina una unidad organizativa.

```powershell
Remove-ADOrganizationalUnit -Identity  "OU=INFORMATICA,DC=IESELCAMINAS,DC=LOCAL" -Recursive -Confirm:$False
```

**Explicación detallada:**

- `Remove-ADOrganizationalUnit`: Este es el cmdlet (comando de PowerShell) utilizado para eliminar una Unidad Organizativa de Active Directory.

- `-Identity "OU=INFORMATICA,DC=IESELCAMINAS,DC=LOCAL"`: Esta parte especifica la identidad de la OU que deseas eliminar. En este caso, es "OU=INFORMATICA,DC=IESELCAMINAS,DC=LOCAL".
- `-Recursive`: Este interruptor indica que deseas eliminar la OU y todos sus objetos secundarios (sub-OUs, usuarios, grupos, etc.) de forma recursiva.
- `-Confirm:$False`: Esto se utiliza para desactivar la solicitud de confirmación. Cuando se establece en `$False`, significa que no se te pedirá confirmación antes de que se elimine la OU. Ten precaución al usar esta opción, ya que puede provocar eliminaciones accidentales.

## 4. Recursos compartidos

Los cmdlets para trabajar con recursos compartidos se encuentran dentro del módulo **SmbShare**

A los recursos compartidos se les puede asociar los distintos ***tipos de permisos***:

- **Control Total (FullAccess)** : Todas las operaciones y cambio de permisos.
- **Cambiar (ChangeAccess)**: Permite crear, modificar y borrar carpetas y archivos.
- **Lectura (ReadAccess)**: Sólo permite la lectura y ejecución de archivos.

### 4.1 Mostrar información de  recurso compartido

El cmdlet **Get-SmbShare (gsmbs)** devuelve los recursos compartidos del sistema.

```powershell
Get-SmbShare
```

Para mostrar los datos de un recurso compartido especificado:

```powershell
# Muestra información del recurso compartido datos
Get-SmbShare -Name datos
# Muestra información del recurso compartido datos en formato lista (Format-List, alias fl)
Get-SmbShare -Name datos | fl
```

### 4.2 Crear recurso compartido

El cmdlet **New-SmbShare (nsmbs)** crea un recurso compartido. 

```powershell
# creación de un recurso compartido sin especificar
New-SmbShare -Path C:\datos -Name datos
#Creación del recurso compartido datos, de forma que al usuario profesor le damos todos los permisos y al usuario alumno, solo lectura
New-SmbShare -Path C:\datos -Name datos -FullAccess profesor -ReadAccess alumno
```

### 4.3 Eliminar recurso compartido

El cmdlet **Remove-SmbShare (rsmbs)** elimina un recurso compartido. La propiedad -Force evita el mensaje de confirmación de eliminación.

```powershell
Remove-SmbShare -Name datos -Force
```

### 4.4 Administrar permisos de un recurso compartido

Los cmdlets `Grant-SmbShareAccess` y `Revoke-SmbShareAccess` son cmdlets de PowerShell que se utilizan para administrar los permisos de acceso a carpetas compartidas (shares) en un entorno de red SMB (Server Message Block). 

El cmdlet **Grant-SmbShareAccess(grsmba)** permite otorgar permisos de acceso a una carpeta compartida. 

El cmdlet **Revoke-SmbShareAccess** se utiliza para revocar o quitar los permisos de acceso a una carpeta compartida. 

**Ejemplo 1**: Añadir el permiso de **control total** al usuario **profesor** sobre el recurso **datos**.

```powershell
Grant-SmbShareAccess -Name datos -AccountName profesor -AccessRight Full -Force 
```

**Ejemplo 2** : Quitar los permisos que tiene el usuario **alumno** sobre el recurso **datos**.

```powershell
Revoke-SmbShareAccess -Name datos -AccountName alumno -Force
```



## 5. Permisos NTFS

Los permisos NTFS (permisos básicos) se componen de cinco niveles de autorización:

- **Control total**: un usuario que tenga este nivel de permisos puede modificar, añadir, desplazar o suprimir carpetas y archivos. También puede cambiar el permiso de acceso.

- **Modificación**: el usuario puede visualizar y modificar los archivos, así como sus propiedades. También puede añadir y suprimir archivos.

- **Lectura y ejecución**: el usuario puede visualizar el contenido de los archivos y lanzar archivos ejecutables y scripts.

- **Lectura**: el usuario puede visualizar el contenido de los archivos.

- **Escritura**: el usuario puede escribir en un archivo y añadir nuevos archivos en la carpeta.

  

Los permisos **NTFS** se pueden heredar (provienen de la carpeta padre) o pueden ser explícitos (configurados individualmente). De esta manera en cada **ACE** (**Access Control Entry**) configurada en el **ACL** (**Access Control List**) se puede definir si el permiso debe ser de tipo "Permitir" o "Denegar".

La gestión de los permisos NTFS con PowerShell puede hacerse con dos cmdlets:

- **Get-Acl**: permite recuperar los permisos configurados en un recurso (carpetas y archivos).
- **Set-Acl**: permite modificar los permisos de un recurso.

- El cmdlet **Get-Acl** permite obtener los permisos declarados en un recurso, como una carpeta, un archivo o una clave de registro. El cmdlet se puede usar simplemente con el parámetro -Path:

| **Parámetro**  | **Descripción**                        |
| -------------- | -------------------------------------- |
| -Path <String> | Indica el camino de acceso al recurso. |

```powershell
Get-Acl -Path .\prueba | Format-List
```

En lugar de Format-List, podemos utilizar el alias fl 

```powershell
Get-Acl -Path .\prueba | fl
```

**Ejemplo 1**: Obtener los permisos del fichero prueba.txt y visualizar en formato tabla.

```powershell
(Get-Acl .\prueba.txt).Access | Format-Table
```

![img](https://lh6.googleusercontent.com/X03gwnAOD-F5ymfnPWapnkxg3CWi2v0m_kbLr9e1neAGFlXBffQ3XeB5S-2PpmDwsvoDkJW1f85tZfKHj1wB-BcXXpFdW7GzOP2vFcdbhwi1pAOCl38DeRj9nJ5WXUbSinTTp8eSUveDO-h-xz_3r_SyiA=s2048)



**Ejemplo 2:** Obtener los permisos del directorio permisos y visualizar en formato tabla

```powershell
(Get-Acl .\permisos).Access | Format-Table
```

![img](https://lh6.googleusercontent.com/VaX-76oBZmEZ1v49hM1t0duOZQm4Gl7R69ScTSnO47YS4HXjkEahs1kZsiB16nLPwm3_mNVnfFSNC9arQISo9hW0dls7IpiKPr0Qo9XrxGcIo1JzaHHRZwasuK7p6o_9G5h0ouy5lhci4DKaTgj7GVOkFg=s2048)

Como puede observarse, es la misma información que podemos recopilar en la GUI:

![img](https://lh6.googleusercontent.com/TwMdsDVlawBvVsSsZJlT3WzpxzVJCyCDti58DGgDlHZgGMXB3PnzodXvLJrJ5e69-yuiIFYDOrq2150cqwCg2_W_rVZkPxHLadroPQPHSQ7zNCjNnXnzY3vWtdb3NbPDjzq7g6mRFouP8meVLdRW_Dk3_w=s2048)

- El cmdlet **Set-Acl** permite definir los permisos en un recurso. Para usar este cmdlet y poder definir estos permisos, hay que utilizar los descriptores de seguridad usando Get-Acl, y aplicarlos después en el recurso deseado.

  | **Parámetro**       | **Descripción**                                              |
  | ------------------- | ------------------------------------------------------------ |
  | -AclObject <Object> | Especifica los descriptores de seguridad que se van a aplicar |
  | -Path <String>      | Indica el camino de acceso al recurso.                       |



**Ejemplo 1: Aplicar permisos NTFS en la carpeta prueba**

```powershell
$ruta = "C:\prueba\"

 New-Item -Path $ruta -ItemType Directory

 $acl= Get-Acl -Path $ruta 

#Crear regla de acceso

<# System.Security.AccessControl.FileSystemAccessRule: Representa una abstracción de una entrada de control de acceso (ACE) que define una regla de acceso para un archivo o directorio #>

$permisoadd = @('Todos', 'FullControl', 'ContainerInherit, ObjectInherit', 'None', 'Allow')

$ace= New-Object -TypeName System.Security.AccessControl.FileSystemAccessRule -ArgumentList $permisoadd

$acl.SetAccessRule($ace)

#Añadir permisos a la carpeta

$acl | Set-Acl -Path $ruta
```

### Herencia

- La **herencia** (**Inheritance**) es a qué tipo de objetos secundarios se aplica la ACE 

  - **ContainerInherit** = Los objetos contenedores secundarios se heredan de la ACE
  - **None** = Los objetos secundarios no se heredan de la ACE.
  - **ObjectInherit** = Los objetos hoja secundarios se heredan de la ACE.

  

### Propagación

- La **propagación** (**propagation)** controla a qué generación de objetos secundarios está restringida la ACE. 

  - **Ninguno** = ACE se aplica a todos. 
  - **InheritOnly** = ACE se aplica solo a hijos y nietos, no a la carpeta de destino. 
  - **NoPropagateInherit** = Carpeta de destino y carpeta de destino hijos, no nietos



**Ejemplo1:** Asignar permisos de control total a todos los usuarios

```powershell
$acl = Get-Acl .\permisos

$acl.Access | Format-Table

$permisoadd = @('Todos','FullControl','ContainerInherit,ObjectInherit','None','Allow')

$ace= New-Object -TypeName System.Security.AccessControl.FileSystemAccessRule -ArgumentList $permisoadd

$acl.setAccessRule($ace)

$acl.Access | Format-Table

$acl | Set-Acl .\permisos
```

