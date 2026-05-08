## Prerequisitos

En esta unidad se asume que ya conoces los conceptos básicos de contenedores trabajados en la asignatura **Implantación de Aplicaciones Web**:

- Qué es una **imagen** y un **contenedor**.
- Comandos básicos de Docker (`run`, `build`, `ps`, `stop`, `rm`).
- Qué es **Docker Hub** y cómo usar imágenes públicas.
- Ficheros `Dockerfile` y `docker-compose.yml`.

---

## 1. Introducción

### 1.1 Limitaciones de Docker en producción

Docker es ideal para ejecutar contenedores en un único servidor. Sin embargo, en entornos de producción reales surgen problemas que Docker por sí solo no resuelve:

| Problema | Descripción |
|----------|-------------|
| **Alta disponibilidad** | Si el servidor cae, todos los contenedores caen con él |
| **Escalado** | Escalar manualmente réplicas de un servicio es complejo |
| **Balanceo de carga** | No hay mecanismo automático para distribuir tráfico entre réplicas |
| **Recuperación automática** | Si un contenedor falla, no se reinicia solo en otro nodo |
| **Despliegues sin downtime** | Actualizar una imagen sin interrumpir el servicio es difícil |

### 1.2 ¿Qué es Kubernetes?

**Kubernetes** (también llamado **K8s**) es una plataforma de código abierto para la **orquestación de contenedores**. Fue desarrollado originalmente por Google y donado a la Cloud Native Computing Foundation (CNCF) en 2014.

Kubernetes automatiza el despliegue, el escalado y la gestión de aplicaciones en contenedores, distribuyéndolas entre un conjunto de máquinas llamado **clúster**.

!!! note "¿Por qué K8s?"
    El nombre abreviado K8s viene de sustituir las 8 letras entre la K y la s de "Kubernetes".

---

## 2. Arquitectura

Un clúster Kubernetes está formado por dos tipos de nodos:

```
┌─────────────────────────────────────────────────────────┐
│                     CLÚSTER KUBERNETES                  │
│                                                         │
│  ┌──────────────────────────────┐                       │
│  │       CONTROL PLANE          │                       │
│  │  ┌──────────┐ ┌───────────┐  │                       │
│  │  │API Server│ │  etcd     │  │                       │
│  │  └──────────┘ └───────────┘  │                       │
│  │  ┌──────────┐ ┌───────────┐  │                       │
│  │  │Scheduler │ │Controller │  │                       │
│  │  └──────────┘ └───────────┘  │                       │
│  └──────────────────────────────┘                       │
│                                                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │  WORKER     │  │  WORKER     │  │  WORKER     │     │
│  │  NODE 1     │  │  NODE 2     │  │  NODE 3     │     │
│  │  kubelet    │  │  kubelet    │  │  kubelet    │     │
│  │  kube-proxy │  │  kube-proxy │  │  kube-proxy │     │
│  │  [pods...]  │  │  [pods...]  │  │  [pods...]  │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
└─────────────────────────────────────────────────────────┘
```

### 2.1 Control Plane

El **Control Plane** (plano de control) gestiona el estado del clúster. Sus componentes principales son:

| Componente | Función |
|------------|---------|
| **API Server** | Punto de entrada de todas las operaciones. Expone la API REST de Kubernetes |
| **etcd** | Base de datos distribuida clave-valor que almacena el estado del clúster |
| **Scheduler** | Decide en qué nodo se ejecuta cada Pod según los recursos disponibles |
| **Controller Manager** | Bucle de control que asegura que el estado actual coincide con el deseado |

### 2.2 Worker Nodes

Los **Worker Nodes** son las máquinas que ejecutan las aplicaciones. Cada uno tiene:

| Componente | Función |
|------------|---------|
| **kubelet** | Agente que se comunica con el API Server y gestiona los Pods del nodo |
| **kube-proxy** | Gestiona las reglas de red para que los Pods se puedan comunicar |
| **Container Runtime** | Motor que ejecuta los contenedores (containerd, CRI-O...) |

---

## 3. Instalación del entorno: Minikube

**Minikube** crea un clúster Kubernetes de un solo nodo en tu máquina local, ideal para aprender y hacer pruebas.

### 3.1 Instalación de Minikube

```bash
# Descargar el binario
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64

# Instalar
sudo install minikube-linux-amd64 /usr/local/bin/minikube

# Verificar
minikube version
```

### 3.2 Instalación de kubectl

`kubectl` es la herramienta de línea de comandos para interactuar con el clúster.

```bash
# Descargar kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"

# Instalar
sudo install kubectl /usr/local/bin/kubectl

# Verificar
kubectl version --client
```

### 3.3 Iniciar el clúster

```bash
# Iniciar Minikube (usa Docker como driver)
minikube start --driver=docker

# Ver el estado
minikube status

# Parar el clúster
minikube stop

# Eliminar el clúster
minikube delete
```

---

## 4. Objetos de Kubernetes

Todo en Kubernetes se describe mediante **objetos**. Los más importantes son:

### 4.1 Pod

El **Pod** es la unidad mínima de despliegue en Kubernetes. Contiene uno o más contenedores que comparten red y almacenamiento.

```yaml
# pod-nginx.yaml
apiVersion: v1
kind: Pod
metadata:
  name: mi-pod
  labels:
    app: nginx
spec:
  containers:
    - name: nginx
      image: nginx:latest
      ports:
        - containerPort: 80
```

```bash
# Crear el Pod
kubectl apply -f pod-nginx.yaml

# Ver Pods en ejecución
kubectl get pods

# Ver detalles del Pod
kubectl describe pod mi-pod

# Ver logs del contenedor
kubectl logs mi-pod

# Acceder al contenedor
kubectl exec -it mi-pod -- /bin/bash

# Eliminar el Pod
kubectl delete pod mi-pod
```

!!! warning "Atención"
    Los Pods son efímeros — si fallan, no se reinician solos. Para gestionar la disponibilidad se usan **Deployments**.

### 4.2 Deployment

Un **Deployment** gestiona un conjunto de réplicas de un Pod, asegurando que siempre haya el número deseado en ejecución. Si un Pod falla, lo recrea automáticamente.

```yaml
# deployment-nginx.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx:1.25
          ports:
            - containerPort: 80
```

```bash
# Crear el Deployment
kubectl apply -f deployment-nginx.yaml

# Ver Deployments
kubectl get deployments

# Ver el estado del rollout
kubectl rollout status deployment/nginx-deployment

# Escalar a 5 réplicas
kubectl scale deployment nginx-deployment --replicas=5

# Actualizar la imagen (rolling update)
kubectl set image deployment/nginx-deployment nginx=nginx:1.26

# Deshacer el último cambio
kubectl rollout undo deployment/nginx-deployment

# Eliminar el Deployment
kubectl delete deployment nginx-deployment
```

### 4.3 Service

Un **Service** expone un conjunto de Pods como un servicio de red estable, con una IP y nombre DNS fijos. Los Pods pueden cambiar, pero el Service siempre apunta a los correctos mediante **selectores de etiquetas**.

Tipos de Service:

| Tipo | Descripción |
|------|-------------|
| **ClusterIP** | Accesible solo dentro del clúster (por defecto) |
| **NodePort** | Expone el servicio en un puerto de cada nodo (30000–32767) |
| **LoadBalancer** | Crea un balanceador de carga externo (en cloud providers) |

```yaml
# service-nginx.yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  type: NodePort
  selector:
    app: nginx
  ports:
    - port: 80
      targetPort: 80
      nodePort: 30080
```

```bash
# Crear el Service
kubectl apply -f service-nginx.yaml

# Ver Services
kubectl get services

# Obtener la URL en Minikube
minikube service nginx-service --url
```

### 4.4 Namespace

Los **Namespaces** permiten dividir el clúster en entornos virtuales aislados (producción, desarrollo, testing...).

```bash
# Ver namespaces
kubectl get namespaces

# Crear un namespace
kubectl create namespace desarrollo

# Desplegar en un namespace concreto
kubectl apply -f deployment-nginx.yaml -n desarrollo

# Ver Pods de un namespace
kubectl get pods -n desarrollo

# Ver Pods de todos los namespaces
kubectl get pods --all-namespaces
```

---

## 5. ConfigMaps y Secrets

### 5.1 ConfigMap

Un **ConfigMap** almacena configuración no sensible (variables de entorno, ficheros de configuración) desacoplada de la imagen del contenedor.

```yaml
# configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  APP_ENV: "produccion"
  APP_PORT: "8080"
  LOG_LEVEL: "info"
```

Usar el ConfigMap en un Deployment:

```yaml
spec:
  containers:
    - name: mi-app
      image: mi-app:1.0
      envFrom:
        - configMapRef:
            name: app-config
```

### 5.2 Secret

Los **Secrets** almacenan información sensible (contraseñas, tokens, claves) codificada en base64.

```bash
# Crear un Secret desde la línea de comandos
kubectl create secret generic db-credenciales \
  --from-literal=usuario=admin \
  --from-literal=password=S3cur3Pass!
```

```yaml
# Usar el Secret en un Deployment
spec:
  containers:
    - name: mi-app
      image: mi-app:1.0
      env:
        - name: DB_USER
          valueFrom:
            secretKeyRef:
              name: db-credenciales
              key: usuario
        - name: DB_PASS
          valueFrom:
            secretKeyRef:
              name: db-credenciales
              key: password
```

!!! warning "Atención"
    Los Secrets solo están codificados en base64, no cifrados. Para producción real se deben usar soluciones adicionales como **Sealed Secrets** o **HashiCorp Vault**.

---

## 6. Almacenamiento persistente

Los contenedores son efímeros — al eliminarse, sus datos desaparecen. Para datos persistentes se usan **Volumes**.

### 6.1 PersistentVolume y PersistentVolumeClaim

| Objeto | Descripción |
|--------|-------------|
| **PersistentVolume (PV)** | Recurso de almacenamiento físico aprovisionado en el clúster |
| **PersistentVolumeClaim (PVC)** | Solicitud de almacenamiento hecha por un Pod |

```yaml
# persistent-volume.yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-datos
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: /mnt/datos
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-datos
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```

Montar el PVC en un Pod:

```yaml
spec:
  containers:
    - name: mi-app
      image: mi-app:1.0
      volumeMounts:
        - mountPath: /datos
          name: almacenamiento
  volumes:
    - name: almacenamiento
      persistentVolumeClaim:
        claimName: pvc-datos
```

---

## 7. Referencia rápida de kubectl

| Comando | Descripción |
|---------|-------------|
| `kubectl get pods` | Lista los Pods |
| `kubectl get pods -o wide` | Lista Pods con IP y nodo |
| `kubectl get all` | Lista todos los recursos |
| `kubectl describe pod <nombre>` | Detalles de un Pod |
| `kubectl logs <pod>` | Logs de un Pod |
| `kubectl logs -f <pod>` | Logs en tiempo real |
| `kubectl exec -it <pod> -- bash` | Acceso interactivo al contenedor |
| `kubectl apply -f <fichero.yaml>` | Crear/actualizar recursos desde YAML |
| `kubectl delete -f <fichero.yaml>` | Eliminar recursos definidos en YAML |
| `kubectl delete pod <nombre>` | Eliminar un Pod |
| `kubectl scale deployment <nombre> --replicas=N` | Escalar un Deployment |
| `kubectl rollout status deployment/<nombre>` | Estado del despliegue |
| `kubectl rollout undo deployment/<nombre>` | Revertir un despliegue |
| `kubectl port-forward pod/<nombre> 8080:80` | Redirigir puerto local al Pod |
| `kubectl top pods` | Uso de CPU y memoria por Pod |

---

## 8. Actividades

!!! example "Tarea"

    **Práctica 1. Instalación y primer despliegue**

    1. Instala Minikube y kubectl en tu máquina virtual.
    2. Inicia el clúster con `minikube start`.
    3. Verifica que el clúster funciona con `kubectl get nodes`.
    4. Despliega un Pod con la imagen `nginx:latest` usando un manifiesto YAML.
    5. Accede a los logs del Pod y conéctate a él con `kubectl exec`.
    6. Elimina el Pod y verifica que desaparece.

!!! example "Tarea"

    **Práctica 2. Deployment y escalado**

    1. Crea un Deployment con 2 réplicas de `nginx:1.25`.
    2. Verifica que se crean 2 Pods con `kubectl get pods`.
    3. Escala el Deployment a 4 réplicas y comprueba el resultado.
    4. Actualiza la imagen a `nginx:1.26` y observa el rolling update con `kubectl rollout status`.
    5. Deshaz la actualización con `kubectl rollout undo` y verifica que vuelve a `nginx:1.25`.
    6. Expón el Deployment con un Service de tipo NodePort y accede desde el navegador usando `minikube service`.

!!! example "Tarea"

    **Práctica 3. ConfigMaps, Secrets y Namespaces**

    1. Crea un Namespace llamado `produccion`.
    2. Crea un ConfigMap con las variables `APP_ENV=produccion` y `LOG_LEVEL=info`.
    3. Crea un Secret con un usuario y contraseña de base de datos.
    4. Despliega un Pod en el Namespace `produccion` que use el ConfigMap y el Secret como variables de entorno.
    5. Verifica dentro del contenedor con `kubectl exec` que las variables están disponibles.

!!! tip "Reto"

    **Práctica 4 (Avanzado). Aplicación con base de datos persistente**

    Despliega una aplicación WordPress completa en Kubernetes:

    1. Crea un Namespace `wordpress`.
    2. Crea un Secret con las credenciales de MySQL.
    3. Despliega MySQL con un PersistentVolumeClaim de 2Gi y un Service ClusterIP.
    4. Despliega WordPress con un Service NodePort, usando el Secret para conectar a MySQL.
    5. Accede a WordPress desde el navegador y completa la instalación.
    6. Elimina el Pod de MySQL, deja que Kubernetes lo recree y verifica que los datos persisten.
