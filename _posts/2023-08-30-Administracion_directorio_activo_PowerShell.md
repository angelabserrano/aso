---
typora-copy-images-to: ../assets/img/powershell
typora-root-url: ../../
layout: post
title: Administracion del servicio de directorio en Windows con PowerShell
categories: scripts
conToc: true
permalink: powershell-directorio-activo
---

## 1.Gestión de usuarios de Active Directory con PowerShell 

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



## 2. Gestión de grupos de Active Directory con PowerShell

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

2.7 Consultar miembros de un grupo

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

- **Control Total**: Todas las operaciones y cambio de permisos.
- **Cambiar**: Permite crear, modificar y borrar carpetas y archivos.
- **Lectura**: Sólo permite la lectura y ejecución de archivos.

### 4.1 Mostrar información de  recursos compartidos

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

