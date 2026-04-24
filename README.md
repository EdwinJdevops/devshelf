# DevShelf — GitOps Internal Developer Platform

> A self-service platform that provisions production-grade AWS 
> environments automatically via GitOps. Built on AWS, Terraform, 
> ArgoCD, and GitHub Actions.

## The Problem It Solves
Developer needs an environment → opens a ticket → waits 3 days.  
With DevShelf → pushes to Git → environment live in minutes.

## Stack
| Layer | Tool |
|-------|------|
| Infrastructure as Code | Terraform |
| GitOps Engine | ArgoCD |
| CI/CD | GitHub Actions |
| Container Orchestration | AWS ECS |
| Observability | Prometheus + Grafana |
| Cloud | AWS (VPC, EC2, ECS, S3, IAM, Lambda) |
| Cost Management | Python + AWS Cost Explorer |
| Secrets | AWS Secrets Manager |

## Build Status
- [x] Remote Terraform state (S3 + DynamoDB)
- [x] VPC with public/private subnets
- [ ] ArgoCD GitOps engine
- [ ] CI/CD pipeline
- [ ] Observability stack
- [ ] FinOps automation

## Phases
| Phase | Description | Status |
|-------|-------------|--------|
| 1 | AWS Foundation — VPC, IAM, S3 backend | ✅ Done |
| 2 | GitOps Core — ArgoCD | 🔨 In Progress |
| 3 | CI/CD Pipeline — GitHub Actions | Pending |
| 4 | Observability — Prometheus + Grafana | Pending |
| 5 | FinOps Intelligence — Cost Automation | Pending |
| 6 | Self-Healing Infrastructure | Pending |

## Author
**Edwin Jonathan** — Cloud & DevOps Engineer  
Lagos, Nigeria → Building globally  
[LinkedIn](https://www.linkedin.com/in/edwin-jonathan-1094093b0)
