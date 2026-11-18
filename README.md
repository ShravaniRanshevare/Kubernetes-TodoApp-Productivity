# 🚀 Kubernetes TodoApp Productivity

A cloud-native full-stack productivity application built using **React**, **FastAPI**, **PostgreSQL**, **Docker**, **Kubernetes**, and **Helm**.

The project demonstrates modern software engineering practices including full-stack development, containerisation, database persistence, Kubernetes orchestration, Helm chart deployment, CI/CD automation, scalability, and cloud-native application delivery.

---

## 📖 Overview

Kubernetes TodoApp Productivity is a task management application that allows users to create, manage, update, and track tasks through a responsive web interface.

### Built With

- **React + Vite** for the frontend
- **FastAPI** for the backend API
- **PostgreSQL** for persistent storage
- **Docker** for containerisation
- **Kubernetes** for orchestration
- **Helm** for deployment management
- **GitHub Actions** for CI/CD

---

## ✨ Features

### ✅ Task Management

- Create tasks
- View tasks
- Update tasks
- Delete tasks
- Mark tasks as completed
- Persistent PostgreSQL storage

### 🎨 Frontend Features

- React-based UI
- Responsive design
- API integration using Axios
- Fast Vite development environment

### 🔗 Backend Features

- FastAPI REST API
- SQLAlchemy ORM
- PostgreSQL integration
- Alembic database migrations
- Environment-based configuration
- Dockerised deployment

### ☸️ Kubernetes Features

- Deployments
- Services
- Secrets
- Namespace isolation
- Ingress configuration
- TLS certificate support
- Horizontal Pod Autoscaler (HPA)
- Rolling updates

### 📦 Helm Features

- Helm chart packaging
- Templated Kubernetes manifests
- Configurable deployments
- Upgrade and rollback support
- Reusable deployment configuration

### 🔄 CI/CD Features

- GitHub Actions workflows
- Automated builds
- Docker image creation
- Docker Hub integration
- Continuous Integration pipeline

---

## 🏗️ Architecture

```text
┌─────────────────────┐
│    React Frontend   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Kubernetes Ingress  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   FastAPI Backend   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    PostgreSQL DB    │
└─────────────────────┘
```

---

## 🛠️ Technology Stack

### Frontend

- React
- Vite
- JavaScript
- Axios

### Backend

- Python
- FastAPI
- SQLAlchemy
- Alembic
- Uvicorn

### Database

- PostgreSQL

### Containerisation

- Docker
- Docker Compose

### Orchestration

- Kubernetes
- Helm

### DevOps

- GitHub Actions
- Docker Hub

---

## 📂 Project Structure

```text
.
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── Dockerfile
│
├── TodoApp/
│   ├── alembic/
│   ├── routers/
│   ├── models/
│   ├── database/
│   ├── requirements.txt
│   └── Dockerfile
│
├── k8s/
│   ├── kind-ingress.yaml
│   └── todoapp/
│       ├── Chart.yaml
│       ├── values.yaml
│       └── templates/
│
├── .github/
│   └── workflows/
│
└── README.md
```

---

## 🐳 Docker Deployment

### Build Backend

```bash
docker build -t todoapp-backend ./TodoApp
```

### Build Frontend

```bash
docker build -t todoapp-frontend ./frontend
```

### Run Using Docker Compose

```bash
docker compose up -d
```

---

## ☸️ Kubernetes Deployment

### Create Namespace

```bash
kubectl create namespace todoapp
```

### Deploy Using Helm

```bash
helm install todoapp ./k8s/todoapp -n todoapp
```

### Verify Deployment

```bash
kubectl get all -n todoapp
```

### Upgrade Deployment

```bash
helm upgrade todoapp ./k8s/todoapp -n todoapp
```

### Remove Deployment

```bash
helm uninstall todoapp -n todoapp
```

---

## 🔒 Security

- Kubernetes Secrets for database credentials
- Environment variable configuration
- Namespace isolation
- TLS-ready ingress configuration
- Certificate management
- Separation of infrastructure and application configuration

Sensitive files are excluded from source control using `.gitignore`.

---

## 📈 Scalability

The application supports Kubernetes scaling features including:

- Horizontal Pod Autoscaling (HPA)
- Rolling updates
- Service discovery
- High availability deployment patterns
- Container orchestration

Check autoscaling:

```bash
kubectl get hpa -n todoapp
```

---

## 🔄 Database Migrations

### Create Migration

```bash
alembic revision --autogenerate -m "migration_name"
```

### Apply Migration

```bash
alembic upgrade head
```

### Rollback Migration

```bash
alembic downgrade -1
```

---

## 🚦 CI/CD Pipeline

```text
Developer Push
       │
       ▼
 GitHub Actions
       │
       ▼
 Automated Validation
       │
       ▼
 Docker Image Build
       │
       ▼
 Docker Hub Push
```

### Pipeline Features

- Automated validation
- Source code checks
- Docker image creation
- Docker Hub publishing
- Continuous Integration workflow

---

## 🎓 Learning Outcomes

This project demonstrates practical experience in:

- Full-Stack Development
- REST API Design
- PostgreSQL Database Management
- Docker Containerisation
- Kubernetes Orchestration
- Helm Chart Development
- GitHub Actions CI/CD
- Infrastructure as Code (IaC)
- DevOps Engineering
- Cloud-Native Application Development

---

## 🚀 Future Enhancements

- User authentication
- JWT security
- Task priorities
- Task categories
- Due dates and reminders
- Email notifications
- Prometheus monitoring
- Grafana dashboards
- Cloud deployment (AKS, EKS or GKE)
- Automated Kubernetes deployment pipeline

---

## 👩‍💻 Author

**Shravani Ranshevare**

BSc Computer Science Student  
University of Hertfordshire

GitHub: https://github.com/ShravaniRanshevare

---

⭐ If you found this project useful, consider starring the repository.
