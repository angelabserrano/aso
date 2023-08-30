---
typora-copy-images-to: ../assets/img/powershell
typora-root-url: ../../
layout: post
title: Administracion del servicio de directorio en Windows con PowerShell
categories: scripts
conToc: true
permalink: powershell
---

## 1.Gestión de usuarios de Active Directory con PowerShell 

### 1.1 Creación de cuentas de usuario 

El comando [New-ADUser](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ee617253(v=technet.10)?redirectedfrom=MSDN) crea un usuario en el directorio activo.

Ejemplo:

```powershell
New-ADUser -Name "Maria Perez" -Path "CN=Users,DC=EMPRESA,DC=LOCAL" -SamAccountName "mariap" -UserPrincipalName "mariap@EMPRESA.LOCAL" -AccountPassword (ConvertTo-SecureString "aso2023." -AsPlainText -Force) -GivenName "Maria" -Surname "Perez" -ChangePasswordAtLogon $true -Enabled $true
```

### 1.2 Eliminación de usuarios

El comando [Remove-ADUser](https://docs.microsoft.com/en-us/powershell/module/addsadministration/remove-aduser?view=win10-ps) elimina un usuario del directorio activo.

Ejemplo:

```powershell
Remove-ADUser -Identity "mariap"
```

```powershell
Remove-ADUser -Identity "CN=Maria Perez,CN=Users,DC=Empresa,DC=Local" 
```



2. Gestión de grupos de Active Directory con PowerShell

