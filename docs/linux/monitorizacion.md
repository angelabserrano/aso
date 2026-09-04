---
draft: true
---

# UT9. Monitorización Centralizada y Alertas

!!! abstract "Resultado de aprendizaje"
    Esta unidad trabaja el **RA2** del RD 1629/2009: *Administra procesos del sistema describiéndolos y aplicando criterios de seguridad y eficiencia*, en su vertiente de **seguimiento y evaluación del rendimiento del sistema**.

    Las herramientas del propio sistema (`journalctl`, `top`, `sar`, Visor de eventos…) se ven en la **UT2**. Esta unidad las lleva un paso más allá: monitorizar **muchos equipos a la vez**, con histórico y **alertas automáticas**.

## Programación de Aula

### Planificación Temporal (3 sesiones / 6 horas)

| Sesión | Contenido |
| ------ | --------- |
| 1 | Arquitectura de una plataforma de monitorización. Prometheus y *exporters* |
| 2 | Grafana: fuentes de datos, cuadros de mando y PromQL |
| 3 | Alertas. Caso práctico integrador |

---

## 1. Por qué una plataforma de monitorización

Las herramientas vistas en la UT2 sirven para **un vistazo puntual a un equipo**. En una red con varios servidores necesitamos algo que:

- Recoja métricas de **todos los equipos** de forma continua.
- Guarde un **histórico** para ver la evolución y planificar capacidad.
- Muestre **cuadros de mando** comprensibles.
- **Avise automáticamente** (correo, chat…) cuando algo se sale de lo normal, sin que nadie esté mirando.

En esta unidad se usa **Prometheus** (recogida y almacenamiento de métricas) con **Grafana** (visualización y alertas), que es la combinación estándar hoy en administración de sistemas y entornos *cloud*.

## 2. Arquitectura

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

## 3. Instalar los exporters

```bash
# Linux — en cada host a monitorizar
sudo apt install prometheus-node-exporter
sudo systemctl enable --now prometheus-node-exporter
curl -s localhost:9100/metrics | head
```

En Windows se instala **`windows_exporter`** (paquete `.msi` del proyecto); queda escuchando en el puerto **9182**.

## 4. Instalar y configurar Prometheus

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

## 5. Instalar Grafana

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

## 6. PromQL básico

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

## 7. Alertas

Con **Grafana Unified Alerting** se define una alerta en tres pasos:

1. **Regla de alerta**: una consulta PromQL + una condición (p. ej. `espacio_libre < 10` durante `5m`).
2. **Punto de contacto**: cómo se avisa (correo electrónico, webhook…).
3. **Política de notificación**: qué alertas van a qué punto de contacto.

Buenas prácticas:

- Alertar sobre **síntomas** que afectan al servicio (disco casi lleno, servicio caído), no sobre cada pico puntual.
- Usar el parámetro de duración (`for`) para evitar falsas alarmas por picos momentáneos.
- Cada alerta debe ser **accionable**: si no vas a hacer nada al recibirla, no la crees.

!!! tip "Alternativa integrada"
    **Zabbix** es otra opción muy usada, sobre todo en entornos on-premise: un único producto que integra servidor, agente, interfaz web y alertas. Se ha elegido Prometheus + Grafana por su alineación con los entornos *cloud native* y por el modelo de configuración como código.

---

## 8. Actividades

!!! example "Tarea"

    **Actividad 1. Monitorización centralizada**

    - Monta un servidor con Prometheus y Grafana.
    - Añade como objetivos un host Linux (`node_exporter`) y un cliente Windows (`windows_exporter`).
    - Importa los cuadros de mando 1860 y 14694 y comprueba que muestran datos de ambos equipos.

!!! example "Tarea"

    **Actividad 2. Cuadro de mando propio**

    - Crea un panel nuevo con una consulta PromQL que muestre el **porcentaje de espacio libre en `/`** de todos los hosts Linux.
    - Añade otro panel con el **% de uso de CPU** por host y otro con la **carga media**.

!!! example "Tarea"

    **Actividad 3. Alerta**

    - Define una alerta que se dispare cuando el espacio libre en `/` baje del **15 %** durante más de 5 minutos y la envíe por correo.
    - Llena el disco con un fichero grande y verifica que la alerta salta y que luego se resuelve al liberar espacio.
