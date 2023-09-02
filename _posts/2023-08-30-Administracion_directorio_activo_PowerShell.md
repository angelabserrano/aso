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

El cmdlet [New-ADUser](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ee617253(v=technet.10)?redirectedfrom=MSDN) crea un usuario en el directorio activo.

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

El cmdlet [Remove-ADUser](https://docs.microsoft.com/en-us/powershell/module/addsadministration/remove-aduser?view=win10-ps) elimina un usuario del directorio activo.

Ejemplo:

```powershell
Remove-ADUser -Identity "mariag"
```

```powershell
Remove-ADUser -Identity "CN=Maria Garcia,CN=Users,DC=Empresa,DC=Local" 
```

### 1.3 Deshabilitar una cuenta de usuario

El cmdlet [Disable-ADAccount](https://docs.microsoft.com/en-us/powershell/module/addsadministration/disable-adaccount?view=win10-ps) deshabilita una cuenta de usuario del directorio activo

Ejemplo:

```powershell
Disable-ADAccount -Identity "mariag" 
```

```powershell
Disable-ADAccount -Identity "CN=Maria Garcia,CN=Users,DC=Empresa,DC=Local" 
```

### 1.4 Modificación de cuentas de usuario

Podemos modificar alguna propiedad de la cuenta de usuario a través del cmdlet **Set-ADUser**

```powershell
Set-ADUser -Identity "mariag" -EmailAddress "mariag@empresa.local"
```

### 1.5 Consultar usuarios

El cmdlet **Get-ADUser** nos pemite consulltar las cuentas de usuario.

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

El comando [New-ADGroup](https://docs.microsoft.com/en-us/powershell/module/addsadministration/new-adgroup?view=win10-ps) crea un nuevo grupo en el dominio especificado

Ejemplo:

```powershell
New-ADGroup -Name "Profesores" -GroupCategory Security -GroupScope Global -Path "CN=Users,DC=EMPRESA,DC=LOCAL"
```

### 2.2 Añadir usuarios a un grupo del dominio

El comando [Add-ADGroupMember](https://docs.microsoft.com/en-us/powershell/module/addsadministration/add-adgroupmember?view=win10-ps) añade usuarios al grupo especificado

Ejemplo:

```powershell
Add-ADGroupMember -Identity "Profesores" -Members mariag,pepe
```

### 2.3 Quitar usuarios de un grupo del dominio

El comando [Remove-ADGroupMember](https://docs.microsoft.com/en-us/powershell/module/addsadministration/remove-adgroupmember?view=win10-ps) quita usuarios del grupo especificado

Ejemplo:

```powershell
Remove-ADGroupMember -Identity "Profesores" -Members mariag
```



## 3. Gestión de unidades organizativas de Active Directory con PowerShell

### 3.1 Creación de unidades organizativas

El comando [New-ADOrganizationalUnit](https://docs.microsoft.com/en-us/powershell/module/addsadministration/new-adorganizationalunit?view=win10-ps) crea una unidad organizativa.

Ejemplo:

```powershell
New-ADOrganizationalUnit -Name "Empresa" -Path "DC=EMPRESA,DC=LOCAL" -Description "Unidad Empresa"
```

```powershell
New-ADOrganizationalUnit -Name "Finanzas" -Path "OU=EMPRESA,DC=EMPRESA,DC=LOCAL" -Description "Unidad de finanzas"
```

### 3.2 Eliminación de unidades organizativas

El comando Remove_ADOrganizationalUnit elimina una unidad organizativa.

```powershell
Remove-ADOrganizationalUnit -Identity  "OU=INFORMATICA,DC=IESELCAMINAS,DC=LOCAL" -Recursive -Confirm:$False
```

**Explicación detallada:**

- `Remove-ADOrganizationalUnit`: Este es el cmdlet (comando de PowerShell) utilizado para eliminar una Unidad Organizativa de Active Directory.

- `-Identity "OU=INFORMATICA,DC=IESELCAMINAS,DC=LOCAL"`: Esta parte especifica la identidad de la OU que deseas eliminar. En este caso, es "OU=INFORMATICA,DC=IESELCAMINAS,DC=LOCAL".
- `-Recursive`: Este interruptor indica que deseas eliminar la OU y todos sus objetos secundarios (sub-OUs, usuarios, grupos, etc.) de forma recursiva.
- `-Confirm:$False`: Esto se utiliza para desactivar la solicitud de confirmación. Cuando se establece en `$False`, significa que no se te pedirá confirmación antes de que se elimine la OU. Ten precaución al usar esta opción, ya que puede provocar eliminaciones accidentales.
