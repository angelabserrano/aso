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

2.1 Creación de grupos

