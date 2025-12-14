# Intelligent E-Commerce Ad Creative Generator 🚀

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Azure](https://img.shields.io/badge/Azure-AKS-0078D4)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED)
![CI/CD](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success)

## 📌 Project Overview
This project is an end-to-end **MLOps Pipeline** designed to automate the creation of e-commerce advertisement copy. It uses a Generative AI model (fine-tuned LLM) to produce marketing text based on product descriptions.

The system is built with a "Production-First" mindset, featuring automated data ingestion, model versioning, containerized deployment on **Azure Kubernetes Service (AKS)**, and real-time observability.

---

## 🏗️ System Architecture

The pipeline consists of the following key stages:

1.  **Data Ingestion & Orchestration:** **Apache Airflow** schedules the fetching of product data and triggers model retraining workflows.
2.  **Model Training & Tracking:** **MLflow** tracks experiments, logs metrics, and manages model versions (Model Registry).
3.  **CI/CD Pipeline:** **GitHub Actions** automatically:
    * Lints and tests the code.
    * Builds and pushes Docker images to Docker Hub.
    * Deploys the latest image to the Azure Kubernetes Service (AKS).
4.  **Deployment:** The API is served via **FastAPI** on a Kubernetes cluster with **Horizontal Pod Autoscaling (HPA)** enabled.
5.  **Monitoring:** **Prometheus** scrapes metrics from the pods, and **Grafana** visualizes traffic, latency, and error rates with active alerting.

---

## 🚀 Key Features

* **Generative AI Model:** Fine-tuned Transformer model for high-quality ad copy generation.
* **Fully Automated CI/CD:** Zero-touch deployment from GitHub commit to live Production.
* **Scalable Infrastructure:** Deployed on Azure AKS with a Load Balancer and HPA to handle traffic spikes.
* **Observability:** Custom Grafana dashboards monitoring Request Rate, Latency, and System Health.
* **Containerization:** Optimized Docker images ensuring consistency across environments.

---

## 🛠️ Installation & Setup

### Prerequisites
* Azure CLI
* Kubectl
* Docker
* Python 3.9+

# Build the image
docker build -t ad-creative-api src/api/

# Run the container
docker run -p 8000:8000 ad-creative-api

Visit http://localhost:8000/docs to test the API locally.

# Apply deployments and services
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

# Enable Autoscaling
kubectl apply -f k8s/hpa.yaml

📊 Monitoring & Observability
The system uses the Prometheus Operator stack for full-stack monitoring.

Accessing Dashboards
Grafana: Exposed on port 3000 (via port-forwarding).

Prometheus: Scrapes metrics from the /metrics endpoint on the API.

Key Metrics Tracked
Throughput: Requests per second (RPS).

Latency: Average response time per inference.

Error Rate: Percentage of 5xx errors.

Saturation: CPU and Memory usage of pods.



# Completed 14th Dec, 2025 6:48 PM GMT
# HASEEB SULTAN 22i-0874