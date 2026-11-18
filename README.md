**Kubernetes TodoApp Productivity**

A cloud-native full-stack productivity application built with FastAPI, React, PostgreSQL, Docker, Kubernetes, and Helm. The project demonstrates modern software engineering practices including containerization, orchestration, infrastructure automation, CI/CD, database management, and scalable cloud deployment.

**🚀 Features**
Task Management
Create tasks
Update task details
Mark tasks as completed
Delete tasks
Persistent data storage using PostgreSQL
RESTful API architecture

**Productivity Features**
Real-time task tracking
Task status management
Responsive user interface
Persistent storage across application restarts
Scalable backend services

**Backend**
FastAPI REST API
SQLAlchemy ORM
Alembic database migrations
PostgreSQL integration
Environment-based configuration
Dockerized deployment

**Frontend**
React + Vite
Modern component-based architecture
Axios API communication
Responsive design
Containerized deployment

**Kubernetes**
Namespace isolation
Deployments
Services
Secrets management
Horizontal Pod Autoscaling (HPA)
Ingress configuration
TLS certificates
Self-signed certificate issuer

**Helm**
Helm chart packaging
Templated Kubernetes manifests
Configurable deployments
Environment-specific values
Simplified application rollout

**DevOps**
Docker image builds
Docker Hub integration
GitHub Actions CI pipeline
Automated testing and build validation
Infrastructure as Code (IaC)

**🏗 System Architecture**
Plain Text
┌───────────────┐
│ React UI │
│ Frontend │
└───────┬───────┘
│
▼
┌───────────────┐
│ Ingress │
└───────┬───────┘
│
▼
┌───────────────┐
│ FastAPI │
│ Backend │
└───────┬───────┘
│
▼
┌───────────────┐
│ PostgreSQL DB │
└───────────────┘

**🛠 Technology Stack**
*Frontend*
React
Vite
JavaScript
Axios

*Backend*
FastAPI
Python
SQLAlchemy
Alembic
Uvicorn

*Database*
PostgreSQL

*Containerization*
Docker
Docker Compose

*Orchestration*
Kubernetes
Helm

*CI/CD*
GitHub Actions

**📂 Project Structure**
.
├── frontend/
│ ├── src/
│ ├── public/
│ └── Dockerfile
│
├── TodoApp/
│ ├── routers/
│ ├── alembic/
│ ├── models/
│ ├── database/
│ └── Dockerfile
│
├── k8s/
│ ├── todoapp/
│ │ ├── templates/
│ │ ├── values.yaml
│ │ └── Chart.yaml
│ │
│ └── kind-ingress.yaml
│
├── .github/workflows/
│
|___ . README.md


**🐳 Docker Deployment**

Build backend image:

docker build -t todoapp-backend ./TodoApp

Build frontend image:

docker build -t todoapp-frontend ./frontend

Run containers:

docker compose up -d

**☸️ Kubernetes Deployment**

Create namespace:

kubectl create namespace todoapp

Deploy using Helm:

helm install todoapp ./k8s/todoapp -n todoapp

Verify deployment:

kubectl get all -n todoapp

Upgrade deployment:

helm upgrade todoapp ./k8s/todoapp -n todoapp

Uninstall:

helm uninstall todoapp -n todoapp

**🔒 Security**

The project implements:

Kubernetes Secrets for sensitive credentials
Environment variable configuration
TLS-ready ingress configuration
Certificate management through Kubernetes
Namespace isolation
Containerized service separation

Sensitive files such as database credentials are excluded from source control using .gitignore.

**📈 Scalability**

The application supports horizontal scaling through Kubernetes:

kubectl get hpa -n todoapp

Features include:

Horizontal Pod Autoscaling
Stateless backend deployment
Service discovery
Container orchestration
Rolling updates
✅ CI/CD Pipeline

GitHub Actions provides:

Source validation
Automated builds
Docker image creation
Container registry publishing
Continuous integration workflows

Pipeline stages:

Code Push
↓
GitHub Actions
↓
Build
↓
Test
↓
Docker Image Creation
↓
Container Registry
 
🔄 Database Migrations

Create migration:

alembic revision --autogenerate -m "New Migration"

Apply migration:

alembic upgrade head

Rollback migration:

alembic downgrade -1


**🎯 Learning Outcomes**

This project demonstrates practical experience with:

Full-stack web development
REST API design
Database modelling
PostgreSQL administration
Docker containerization
Kubernetes orchestration
Helm packaging
DevOps workflows
CI/CD automation
Cloud-native architecture
Infrastructure as Code (IaC)

**👩‍💻 Author**

Shravani Ranshevare

BSc Computer Science Student
 University of Hertfordshire

GitHub: https://github.com/ShravaniRanshevare

**Future Enhancements**
User authentication and authorization
JWT security integration
Task categories and priorities
Due dates and reminders
Analytics dashboard
Prometheus monitoring
Grafana dashboards
Production cloud deployment (AKS/EKS/GKE)
Automated Kubernetes deployment via GitHub Actions

⭐ If you found this project interesting, consider starring the repository.
