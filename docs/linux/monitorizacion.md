# UT9. Monitorización y Análisis del Rendimiento del Sistema

!!! abstract "Resultado de aprendizaje"
    Esta unidad trabaja el **RA2** del RD 1629/2009: *Administra procesos del sistema describiéndolos y aplicando criterios de seguridad y eficiencia*, en su vertiente de **seguimiento y evaluación del rendimiento del sistema**.

## Programación de Aula

### Planificación Temporal (5 sesiones / 10 horas)

| Sesión | Contenido |
| ------ | --------- |
| 1 | Introducción a la monitorización. Registros del sistema en Linux (journald, rsyslog, logrotate) |
| 2 | Registros en Windows (Visor de eventos, `Get-WinEvent`). Centralización de logs |
| 3 | Métricas del sistema con herramientas nativas (Linux y Windows) |
| 4 | Monitorización centralizada: Prometheus, *exporters* y Grafana |
| 5 | PromQL, cuadros de mando y alertas. Caso práctico integrador |

---

## 1. Introducción

**Monitorizar** un sistema es recoger de forma continua información sobre su estado y su rendimiento para poder:

- Detectar **incidencias** antes (o en cuanto) ocurren: servicios caídos, discos llenos, saturación.
- **Diagnosticar** problemas de rendimiento (¿CPU?, ¿memoria?, ¿disco?, ¿red?).
- Planificar la **capacidad**: prever cuándo habrá que ampliar recursos.
- Aportar **evidencias** para el análisis de seguridad y las auditorías.

### 1.1 Tres tipos de datos

| Tipo | Qué es | Ejemplo | Herramientas |
| ---- | ------ | ------- | ------------ |
| **Métricas** | Valores numéricos medidos en el tiempo | % de CPU, MB libres, peticiones/s | `top`, `sar`, Prometheus |
| **Registros (logs)** | Mensajes de texto con marca de tiempo | "servicio X arrancado", "fallo de autenticación" | `journalctl`, Visor de eventos, rsyslog |
| **Trazas** | Recorrido de una petición entre componentes | petición HTTP → app → BD | (fuera del alcance de esta unidad) |

### 1.2 Señales clave (*golden signals*)

Para cualquier servicio conviene vigilar cuatro señales: **latencia** (cuánto tarda), **tráfico** (cuánta demanda recibe), **errores** (proporción de fallos) y **saturación** (cómo de lleno está el recurso más limitado).

### 1.3 Monitorización reactiva y proactiva

- **Reactiva**: se mira el sistema cuando ya hay un problema (comandos puntuales).
- **Proactiva**: se recogen métricas y logs de forma permanente y se definen **alertas** que avisan al administrador automáticamente.

---

## 2. Registros del sistema en Linux

### 2.1 journald

En los sistemas con *systemd*, el servicio **`systemd-journald`** recoge de forma centralizada los mensajes del núcleo, los servicios y las aplicaciones. Se consulta con **`journalctl`**:

```bash
journalctl -u ssh                 # mensajes del servicio ssh
journalctl -u ssh --since "1 hour ago"
journalctl -p err                 # prioridad error o superior (0 emerg … 7 debug)
journalctl -b                     # solo el arranque actual
journalctl -k                     # solo mensajes del núcleo (kernel)
journalctl -f                     # seguir en tiempo real (como tail -f)
journalctl --since "2025-09-01" --until "2025-09-02 12:00"
journalctl --disk-usage           # espacio ocupado por el journal
```

Para que el registro **persista entre reinicios**:

```bash
sudo mkdir -p /var/log/journal
sudo systemctl restart systemd-journald
```

Limitar el tamaño en `/etc/systemd/journald.conf`:

```ini
[Journal]
Storage=persistent
SystemMaxUse=500M
MaxRetentionSec=1month
```

### 2.2 rsyslog y /var/log

Muchos servicios siguen escribiendo en ficheros de texto dentro de **`/var/log`** (`auth.log`, `syslog`, `kern.log`…) a través de **rsyslog**. Ficheros y "facilities/priorities" se configuran en `/etc/rsyslog.conf` y `/etc/rsyslog.d/`.

### 2.3 Rotación de logs (logrotate)

**logrotate** evita que los ficheros de registro crezcan sin control: los rota, comprime y elimina los antiguos. Configuración en `/etc/logrotate.conf` y `/etc/logrotate.d/`.

```
/var/log/mi-app/*.log {
    weekly
    rotate 8
    compress
    missingok
    notifempty
}
```

### 2.4 Centralización remota

En una red con varios servidores interesa **enviar todos los logs a un servidor central**. Con rsyslog:

```bash
# En el equipo que envía  (/etc/rsyslog.d/90-remote.conf)
*.*  @@192.168.1.10:514      # @@ = TCP ;  @ = UDP

# En el servidor central  (/etc/rsyslog.d/10-server.conf)
module(load="imtcp")
input(type="imtcp" port="514")
```

---

## 3. Registros del sistema en Windows

El **Visor de eventos** (`eventvwr.msc`) organiza los registros en canales; los principales son **Aplicación**, **Sistema** y **Seguridad**.

Desde PowerShell:

```powershell
# Últimos 20 eventos del registro del sistema
Get-WinEvent -LogName System -MaxEvents 20

# Inicios de sesión fallidos (Id 4625) de las últimas 24 h
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625; StartTime=(Get-Date).AddHours(-24)}

# Errores y advertencias de un servicio concreto
Get-WinEvent -FilterHashtable @{LogName='System'; Level=1,2,3} |
    Where-Object ProviderName -eq 'Service Control Manager'
```

Con `wevtutil` (línea de comandos clásica):

```cmd
wevtutil qe System /c:5 /rd:true /f:text
```

Para centralizar, Windows dispone de **Reenvío de eventos (WEF/WEC)**: los equipos *origen* envían eventos a un *colector* mediante WinRM (`winrm quickconfig`, `wecutil`).

---

## 4. Métricas con herramientas nativas

### 4.1 Linux

| Recurso | Comandos |
| ------- | -------- |
| Carga y CPU | `uptime`, `top`, `htop`, `mpstat 1`, `vmstat 1` |
| Memoria | `free -h`, `vmstat`, `cat /proc/meminfo` |
| Disco (espacio) | `df -h`, `du -sh *` |
| Disco (E/S) | `iostat -xz 1`, `iotop` |
| Red | `ss -tulpn`, `ip -s link`, `iftop`, `nload` |
| Por proceso | `ps aux --sort=-%cpu`, `pidstat 1` |

**Histórico con `sar`** (paquete `sysstat`): recoge métricas cada pocos minutos y permite consultarlas después.

```bash
sudo apt install sysstat
sudo sed -i 's/ENABLED="false"/ENABLED="true"/' /etc/default/sysstat
sudo systemctl enable --now sysstat

sar -u 1 5        # CPU: 5 muestras cada segundo
sar -r            # memoria a lo largo del día
sar -d            # actividad de disco
sar -n DEV        # tráfico de red por interfaz
```

### 4.2 Windows

- **Administrador de tareas** y **Monitor de recursos** (`resmon`): vista rápida e interactiva.
- **Monitor de rendimiento** (`perfmon`): contadores detallados y **conjuntos de recopiladores de datos** para registro histórico.

```powershell
Get-Counter '\Processor(_Total)\% Processor Time'
Get-Counter '\Memory\Available MBytes'
Get-Counter '\LogicalDisk(C:)\% Free Space'

typeperf "\Processor(_Total)\% Processor Time" -sc 5
```

---

## 5. Monitorización centralizada con Prometheus y Grafana

Las herramientas anteriores sirven para **un vistazo puntual**. Para vigilar **muchos equipos de forma continua**, con histórico y alertas, se usa una plataforma de monitorización. En esta unidad utilizamos **Prometheus** (recogida y almacenamiento de métricas) y **Grafana** (visualización y alertas).

### 5.1 Arquitectura

```
                    ┌───────────────┐        ┌───────────┐
  node_exporter ◄───┤   PROMETHEUS  ├───────►│  GRAFANA  │
 (host Linux)  9100 │  (pull + TSDB)│  9090  │   3000    │
                    │               │        │ paneles + │
windows_exporter◄───┤  prometheus.yml        │  alertas  │
 (host Windows)9182 └───────────────┘        └───────────┘
```

- **Modelo *pull***: Prometheus **consulta periódicamente** ("scrape") a cada objetivo por HTTP y guarda las métricas en su base de datos de series temporales (TSDB).
- **Exporters**: pequeños agentes que exponen las métricas de un sistema en `/metrics`. `node_exporter` para Linux, `windows_exporter` para Windows.
- **PromQL**: lenguaje de consulta de Prometheus.
- **Grafana**: cuadros de mando y **alertas** sobre los datos de Prometheus.

### 5.2 Instalar los exporters

```bash
# Linux — en cada host a monitorizar
sudo apt install prometheus-node-exporter
sudo systemctl enable --now prometheus-node-exporter
curl -s localhost:9100/metrics | head
```

En Windows se instala **`windows_exporter`** (paquete `.msi` del proyecto); queda escuchando en el puerto **9182**.

### 5.3 Instalar y configurar Prometheus

```bash
sudo apt install prometheus
```

Editar `/etc/prometheus/prometheus.yml` y añadir los objetivos:

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  - job_name: 'linux'
    static_configs:
      - targets: ['192.168.1.11:9100', '192.168.1.12:9100']

  - job_name: 'windows'
    static_configs:
      - targets: ['192.168.1.50:9182']
```

```bash
sudo systemctl restart prometheus
```

En `http://IP_SERVIDOR:9090` → **Status → Targets** deben aparecer todos los objetivos en estado **UP**.

### 5.4 Instalar Grafana

```bash
sudo apt install -y apt-transport-https software-properties-common
wget -q -O - https://apt.grafana.com/gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/grafana.gpg
echo "deb [signed-by=/etc/apt/keyrings/grafana.gpg] https://apt.grafana.com stable main" | \
  sudo tee /etc/apt/sources.list.d/grafana.list
sudo apt update && sudo apt install -y grafana
sudo systemctl enable --now grafana-server
```

1. Abrir `http://IP_SERVIDOR:3000` (usuario/contraseña iniciales `admin` / `admin`).
2. **Connections → Data sources → Add data source → Prometheus**, URL `http://localhost:9090`.
3. **Dashboards → Import** e introducir el ID de un panel ya hecho:
   - **1860** — *Node Exporter Full* (Linux)
   - **14694** — *Windows Exporter Dashboard*

### 5.5 PromQL básico

```promql
# % de uso de CPU por host
100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

# % de memoria disponible
node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes * 100

# % de espacio libre en la raíz
node_filesystem_avail_bytes{mountpoint="/"} / node_filesystem_size_bytes{mountpoint="/"} * 100

# Carga media de 1 minuto
node_load1
```

Ideas clave de PromQL: se **selecciona** una métrica y se filtra por *labels* (`{instance="..."}`); `rate()` calcula la variación por segundo de un contador; `avg by (instance)` **agrega** varias series.

---

## 6. Alertas

Con **Grafana Unified Alerting** se define una alerta en tres pasos:

1. **Regla de alerta**: una consulta PromQL + una condición (p. ej. `espacio_libre < 10` durante `5m`).
2. **Punto de contacto**: cómo se avisa (correo electrónico, webhook…).
3. **Política de notificación**: qué alertas van a qué punto de contacto.

Buenas prácticas:

- Alertar sobre **síntomas** que afectan al servicio (disco casi lleno, servicio caído), no sobre cada pico puntual.
- Usar el parámetro de duración (`for`) para evitar falsas alarmas por picos momentáneos.
- Cada alerta debe ser **accionable**: si no vas a hacer nada al recibirla, no la crees.

---

## 7. Resumen de comandos

| Ámbito | Comando | Uso |
| ------ | ------- | --- |
| Logs Linux | `journalctl -u <svc> -f` | Seguir el registro de un servicio |
| Logs Linux | `journalctl -p err -b` | Errores del arranque actual |
| Logs Linux | `logrotate -d /etc/logrotate.conf` | Probar la rotación sin aplicarla |
| Logs Windows | `Get-WinEvent -LogName System -MaxEvents 20` | Últimos eventos del sistema |
| CPU/carga | `uptime`, `top`, `mpstat 1` | Uso de CPU y carga |
| Memoria | `free -h`, `vmstat 1` | Uso de memoria |
| Disco | `df -h`, `iostat -xz 1` | Espacio y E/S de disco |
| Red | `ss -tulpn` | Puertos y conexiones |
| Histórico | `sar -u`, `sar -r` | Métricas registradas por sysstat |
| Windows | `Get-Counter '\Processor(_Total)\% Processor Time'` | Contador de rendimiento |
| Prometheus | `curl localhost:9100/metrics` | Ver las métricas de un exporter |

---

## 8. Actividades

!!! example "Tarea"

    **Actividad 1. Registros del sistema**

    - En un Ubuntu Server, activa el *journal* persistente y limita su tamaño a 300 MB.
    - Obtén con `journalctl` todos los mensajes de prioridad *warning* o superior del último arranque.
    - Provoca tres inicios de sesión SSH fallidos desde otro equipo y localiza los eventos correspondientes en `journalctl -u ssh` y en `/var/log/auth.log`.
    - En un Windows, localiza esos mismos intentos fallidos en el registro de **Seguridad** (Id 4625) con `Get-WinEvent`.

!!! example "Tarea"

    **Actividad 2. Métricas con herramientas nativas**

    - Instala `sysstat` y habilita la recogida.
    - Genera carga de CPU (`yes > /dev/null &`) y de disco (`dd if=/dev/zero of=prueba bs=1M count=2000`).
    - Con `sar`, `vmstat` e `iostat`, identifica qué recurso se satura en cada caso y documenta los valores observados.

!!! example "Tarea"

    **Actividad 3. Monitorización centralizada**

    - Monta un servidor con Prometheus y Grafana.
    - Añade como objetivos un host Linux (`node_exporter`) y un cliente Windows (`windows_exporter`).
    - Importa los cuadros de mando 1860 y 14694 y comprueba que muestran datos de ambos equipos.

!!! example "Tarea"

    **Actividad 4. Cuadro de mando y alerta propios**

    - Crea un panel nuevo con una consulta PromQL que muestre el **porcentaje de espacio libre en `/`** de todos los hosts Linux.
    - Define una alerta que se dispare cuando ese valor baje del **15 %** durante más de 5 minutos y la envíe por correo.
    - Llena el disco con un fichero grande y verifica que la alerta salta y luego se resuelve al liberar espacio.
