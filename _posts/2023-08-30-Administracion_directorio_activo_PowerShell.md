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

El comando [New-ADUser](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ee617253(v=technet.10)?redirectedfrom=MSDN) crea un usuario en el directorio activo.

Ejemplo:

```powershell
New-ADUser -Name "Maria Garcia" -Path "CN=Users,DC=EMPRESA,DC=LOCAL" -SamAccountName "mariag" -UserPrincipalName "mariap@EMPRESA.LOCAL" -AccountPassword (ConvertTo-SecureString "aso2023." -AsPlainText -Force) -GivenName "Maria" -Surname "Garcia" -ChangePasswordAtLogon $true -Enabled $true
```

### 1.2 Eliminación de usuarios

El comando [Remove-ADUser](https://docs.microsoft.com/en-us/powershell/module/addsadministration/remove-aduser?view=win10-ps) elimina un usuario del directorio activo.

Ejemplo:

```powershell
Remove-ADUser -Identity "mariag"
```

```powershell
Remove-ADUser -Identity "CN=Maria Garcia,CN=Users,DC=Empresa,DC=Local" 
```



### 1.3 Deshabilitar una cuenta de usuario

El comando [Disable-ADAccount](https://docs.microsoft.com/en-us/powershell/module/addsadministration/disable-adaccount?view=win10-ps) deshabilita una cuenta de usuario del directorio activo

Ejemplo:

```powershell
Disable-ADAccount -Identity "mariag" 
```

```powershell
Disable-ADAccount -Identity "CN=Maria Garcia,CN=Users,DC=Empresa,DC=Local" 
```



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



### 3. Gestión de unidades organizativas de Active Directory con PowerShell

### 3.1 Creación de unidades organizativas

El comando [New-ADOrganizationalUnit](https://docs.microsoft.com/en-us/powershell/module/addsadministration/new-adorganizationalunit?view=win10-ps) crea una unidad organizativa

Ejemplo:

```powershell
New-ADOrganizationalUnit -Name "Empresa" -Path "DC=EMPRESA,DC=LOCAL" -Description "Unidad Empresa"
```

```powershell
New-ADOrganizationalUnit -Name "Finanzas" -Path "OU=EMPRESA,DC=EMPRESA,DC=LOCAL" -Description "Unidad de finanzas"
```

3.2 Eliminación de unidades organizativas

Remove-ADObject -Identity "OU=EMPRESADC=office,DC=local" -Recursive -Confirm:$False
