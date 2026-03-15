# AWS Container Delivery Platform

Production-style container platform built on AWS using FastAPI, Docker, Terraform, Amazon EKS, Kubernetes, and GitHub Actions.

This project demonstrates an end-to-end container delivery workflow:

- build a Python API
- containerize it with Docker
- push the image to Amazon ECR
- provision AWS infrastructure with Terraform
- deploy the workload to Amazon EKS
- expose it publicly with a Kubernetes LoadBalancer Service
- enable Horizontal Pod Autoscaling
- automate deployment with GitHub Actions
- troubleshoot real infrastructure issues
- tear everything down after validation to control cost

## Why I Built This

I built this project to strengthen the exact areas commonly requested in cloud and DevOps job descriptions: Docker, Kubernetes, Terraform, CI/CD, and infrastructure troubleshooting.

Rather than stopping at a local container demo, I wanted a full AWS deployment lifecycle that included both successful delivery and real debugging.

## Project Overview

The application is a containerized FastAPI service deployed to Amazon EKS.

The workflow was:

1. Develop and test the API locally
2. Build and run the container locally with Docker
3. Push the image to Amazon ECR
4. Provision AWS infrastructure with Terraform
5. Create and validate the EKS cluster
6. Deploy the application to Kubernetes
7. Expose it publicly using a LoadBalancer Service
8. Add Horizontal Pod Autoscaling
9. Add GitHub Actions CI/CD for repeatable deployments
10. Validate the final platform and destroy the infrastructure

## Tech Stack

### Cloud
- AWS EKS
- AWS ECR
- AWS VPC
- AWS IAM
- Elastic Load Balancing

### Infrastructure as Code
- Terraform

### Containers and Orchestration
- Docker
- Kubernetes

### Application
- Python
- FastAPI
- Uvicorn

### CI/CD
- GitHub Actions

## Repository Structure

```text
aws-container-delivery-platform
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── tests
│       └── test_main.py
├── k8s
│   ├── namespace.yaml
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── hpa.yaml
│   ├── ingress.yaml
│   ├── configmap.yaml
│   └── secret.example.yaml
├── terraform
│   ├── main.tf
│   ├── providers.tf
│   ├── outputs.tf
│   ├── variables.tf
│   ├── versions.tf
│   └── terraform.tfvars.example
├── .github
│   └── workflows
│       └── deploy.yml
├── docs
│   └── screenshots
└── README.md
