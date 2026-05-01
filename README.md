# DevShelf — GitOps Internal Developer Platform

> Production-grade GitOps IDP on AWS. Push code. Kubernetes deploys itself.

[

![CI](https://github.com/EdwinJdevops/devshelf/actions/workflows/ci.yaml/badge.svg)

](https://github.com/EdwinJdevops/devshelf/actions/workflows/ci.yaml)

---

## What It Does

Developer pushes code → GitHub Actions builds Docker image → pushes to AWS ECR → ArgoCD detects change → Kubernetes deploys automatically. Zero manual steps.

## Stack

| Layer | Tool |
|-------|------|
| Cloud | AWS EC2 (eu-north-1) |
| Kubernetes | K3s |
| GitOps Engine | ArgoCD |
| CI/CD | GitHub Actions |
| Container Registry | AWS ECR |
| Auth | IAM Instance Profile |
| IaC | Terraform (in progress) |
| Observability | Prometheus + Grafana (in progress) |
| Application | Python Flask |

## Phases

| Phase | Description | Status |
|-------|-------------|--------|
| 1 | AWS Foundation + K3s cluster | ✅ Done |
| 2 | ArgoCD GitOps engine | ✅ Done |
| 3 | GitHub Actions CI/CD + ECR | ✅ Done |
| 4 | Observability — Prometheus + Grafana | 🔨 In Progress |
| 5 | Terraform IaC | Pending |
| 6 | Self-Healing + FinOps | Pending |

## Author

**Edwin Jonathan** — Cloud & DevOps Engineer
Lagos, Nigeria → Building globally
[LinkedIn](https://www.linkedin.com/in/edwin-jonathan-1094093b0) • [X](https://x.com/TheCloudDeveng)
