# Intelligent E-Commerce Ad Creative Generator

![Python](https://img.shields.io/badge/Python-3.9-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Azure](https://img.shields.io/badge/Azure_AKS-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=for-the-badge&logo=mlflow&logoColor=white)
![Status](https://img.shields.io/badge/Status-Production_Ready-success?style=for-the-badge)

An end-to-end **MLOps pipeline** that automates e-commerce ad copy generation using a fine-tuned Generative AI model — built with a production-first mindset featuring automated data ingestion, model versioning, containerized deployment on **Azure Kubernetes Service**, and real-time observability.

---

## 🏗️ System Architecture

![Architecture Diagram](https://github.com/user-attachments/assets/de6e969a-6d9b-4a13-b458-93d91a288147)

---

## ⚙️ Pipeline Stages

```
Product Data Source
      │
      ▼
Apache Airflow
(Scheduled ingestion & retraining triggers)
      │
      ▼
Model Training
(Fine-tuned Transformer — ad copy generation)
      │
      ▼
MLflow
(Experiment tracking, metric logging, Model Registry)
      │
      ▼
GitHub Actions CI/CD
(Lint → Test → Docker Build → Push → Deploy)
      │
      ▼
Azure AKS Deployment
(FastAPI + Load Balancer + HPA)
      │
      ▼
Prometheus + Grafana
(Real-time metrics, dashboards, alerting)
```

---

## 🚀 Key Features

**Generative AI Model**
Fine-tuned Transformer model producing high-quality, product-specific ad copy from raw product descriptions.

**Fully Automated CI/CD**
Zero-touch deployment — a GitHub commit triggers linting, testing, Docker image build and push, and live deployment to AKS automatically via GitHub Actions.

**Scalable Kubernetes Infrastructure**
Deployed on Azure AKS with a Load Balancer and Horizontal Pod Autoscaling (HPA) to handle traffic spikes without manual intervention.

**Full-Stack Observability**
Custom Grafana dashboards tracking throughput, latency, error rates, and pod resource saturation — with active Prometheus alerting.

**Optimized Containerization**
Docker images built for consistency across local, staging, and production environments.

---

## 📊 Monitored Metrics

| Metric | Description |
|:---|:---|
| **Throughput** | Requests per second (RPS) |
| **Latency** | Average inference response time |
| **Error Rate** | Percentage of 5xx responses |
| **Saturation** | Pod CPU and memory utilization |

---

## 🛠️ Tech Stack

| Layer | Tools |
|-------|-------|
| **Orchestration** | Apache Airflow |
| **Model Tracking** | MLflow (experiments, registry) |
| **API** | FastAPI |
| **Containerization** | Docker |
| **Infrastructure** | Azure AKS, Kubernetes, HPA |
| **CI/CD** | GitHub Actions |
| **Monitoring** | Prometheus, Grafana |

---

## ⚙️ Setup & Deployment

### Prerequisites
- Python 3.9+
- Docker
- Azure CLI
- kubectl

### Run Locally

```bash
git clone https://github.com/your-username/ad-creative-generator.git
cd ad-creative-generator
pip install -r requirements.txt

# Build and run Docker container
docker build -t ad-creative-api src/api/
docker run -p 8000:8000 ad-creative-api
```

Visit `http://localhost:8000/docs` to test the API.

### Deploy to Kubernetes

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/hpa.yaml
```

### Access Monitoring Dashboards

```bash
# Grafana (port 3000)
kubectl port-forward svc/grafana 3000:3000

# Prometheus metrics endpoint
GET /metrics
```

---

## 📂 Repository Structure

```
ad-creative-generator/
├── src/
│   └── api/
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── hpa.yaml
├── dags/
├── mlflow/
├── monitoring/
├── .github/
│   └── workflows/
└── README.md
```
