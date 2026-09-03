# Contenedores y orquestación (ampliación)

!!! note "Contenido de ampliación"
    Este apéndice **no forma parte de la evaluación** del módulo ni se corresponde con un resultado de aprendizaje del RD 1629/2009. Los contenedores se trabajan en profundidad en el módulo *Implantación de Aplicaciones Web*. Aquí solo se repasan las ideas clave y se introduce el concepto de **orquestación**, por su relevancia en la administración de sistemas actual.

## 1. Repaso: contenedores y Docker

- **Imagen**: plantilla inmutable con una aplicación y todas sus dependencias. Se distribuye a través de un **registro** (Docker Hub, etc.).
- **Contenedor**: instancia en ejecución de una imagen. Para el sistema operativo es un **proceso aislado** mediante *namespaces* (aislamiento de PID, red, montajes…) y limitado con *cgroups* (CPU, memoria).
- **Dockerfile**: receta para construir una imagen (`docker build`).
- **docker compose**: describe varios contenedores y sus relaciones en un único fichero, para **un solo host**.

| Comando | Acción |
| ------- | ------ |
| `docker run` | Crear y arrancar un contenedor |
| `docker ps` | Listar contenedores en ejecución |
| `docker build -t img .` | Construir una imagen |
| `docker logs` / `docker exec` | Ver registros / entrar en el contenedor |
| `docker compose up -d` | Levantar una aplicación multicontenedor |

Desde el punto de vista de la administración de sistemas, un contenedor es una forma de **empaquetar y ejecutar un servicio** con sus dependencias, reproducible entre máquinas y sin "ensuciar" el sistema anfitrión.

## 2. Por qué hace falta orquestar

Docker resuelve "ejecutar contenedores en **un** servidor". En producción aparecen necesidades que un único host no cubre:

| Necesidad | Qué aporta un orquestador |
| --------- | ------------------------- |
| Alta disponibilidad | Reparte los contenedores entre varios nodos; si un nodo cae, los recrea en otro |
| Escalado | Ajusta el número de réplicas de un servicio (manual o automático) |
| Balanceo de carga | Distribuye el tráfico entre las réplicas |
| Autorreparación | Reinicia o reprograma los contenedores que fallan |
| Despliegues sin corte | Actualiza la imagen de forma progresiva (*rolling update*) y permite revertir |
| Configuración y secretos | Gestiona parámetros y credenciales fuera de la imagen |

A esto se le llama **orquestación de contenedores**. Las opciones más habituales son **Kubernetes (K8s)** —el estándar de facto—, **Docker Swarm** (más simple) y **Nomad**.

## 3. Kubernetes en 5 conceptos

| Concepto | Idea |
| -------- | ---- |
| **Clúster** | Conjunto de máquinas: un *control plane* que decide y varios *worker nodes* que ejecutan las cargas |
| **Pod** | Unidad mínima de despliegue: uno o varios contenedores que comparten red y almacenamiento |
| **Deployment** | Mantiene *N* réplicas de un Pod y gestiona actualizaciones y *rollback* |
| **Service** | Punto de acceso de red estable (IP y DNS fijos) a un conjunto de Pods que cambian |
| **Estado deseado** | Se describe en YAML lo que se quiere; Kubernetes **reconcilia** la realidad con esa descripción de forma continua |

El modelo **declarativo** de Kubernetes es el mismo que ya has visto con **Ansible**: describes el resultado, no los pasos.

## 4. Prueba rápida (opcional)

Con **Minikube** puedes levantar un clúster de un solo nodo en tu propio equipo:

```bash
minikube start --driver=docker
kubectl create deployment web --image=nginx --replicas=2
kubectl expose deployment web --type=NodePort --port=80
minikube service web --url
kubectl get pods -o wide
minikube delete
```

## 5. Para seguir aprendiendo

- Documentación oficial: <https://kubernetes.io/es/docs/home/>
- Tutorial interactivo *Kubernetes Basics*: <https://kubernetes.io/docs/tutorials/kubernetes-basics/>
- Cursos de especialización relacionados: *Administración en la nube* y *Ciberseguridad en entornos de las tecnologías de la información*.
