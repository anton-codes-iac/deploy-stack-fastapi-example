# FastAPI + AWS Fargate & RDS (via deploy-stack) ☁️🚀

> A production-grade example of a modern, async FastAPI application deployed to AWS ECS Fargate with a managed PostgreSQL database, generated instantly using [cookiecutter-fastapi-deploy-stack](https://github.com/anton-codes-iac/cookiecutter-fastapi-deploy-stack).

[![Cookiecutter](https://img.shields.io/badge/cookiecutter-template-D4AA00.svg)](https://github.com/cookiecutter/cookiecutter)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com/)

## 🌟 The Magic

This repository does **not** rely on manual Terraform scripting or AWS console clicks. 

The AWS architecture, Docker configurations, and GitHub Actions CI/CD pipelines were automatically provisioned the moment the project was scaffolded using a post-generation hook.

By simply running:
```bash
cookiecutter gh:anton-codes-iac/cookiecutter-fastapi-deploy-stack
```
The template asked for the AWS region, port, and whether a database was needed, then silently executed `deploy-stack` to generate the `terraform/` and `.github/` directories natively.

## 🏗️ Architecture Features

* **Serverless Compute:** AWS ECS Fargate container running a highly optimized, unprivileged Uvicorn async server.
* **Managed Database:** Securely attached Amazon RDS PostgreSQL instance running inside a private subnet with auto-rotating credentials.
* **Traffic Routing:** Application Load Balancer (ALB) handling health checks and traffic distribution.
* **Zero-Secret CI/CD:** GitHub Actions configured with AWS IAM OIDC (no long-lived access keys).
* **DevSecOps Built-in:** Automated container and infrastructure vulnerability scanning via Trivy on every push.

## 🚀 Try It Yourself

Want to bootstrap and deploy your own production-ready FastAPI app to AWS in under 5 minutes?

1. Install Cookiecutter:
   ```bash
   pip install cookiecutter
   ```
2. Run the deployment template:
   ```bash
   cookiecutter gh:anton-codes-iac/cookiecutter-fastapi-deploy-stack
   ```
3. Navigate into your new project folder.
4. Run `npx --yes deploy-stack apply` to provision the real infrastructure in your AWS account.
5. Once applied, push your local API secrets to the newly created AWS Vault:
   ```bash
   npx --yes deploy-stack secrets push .env
   ```

## 🛑 Safe Teardown

To destroy the AWS infrastructure provisioned by this example (including the RDS database) and stop all billing, run:
```bash
npx --yes deploy-stack destroy
```

## 💰 AWS Costs & Disclaimer
**This tool provisions real AWS resources which will incur charges on your AWS bill.** An ECS Fargate cluster with an Application Load Balancer running 24/7 typically costs around ~$15 - $20/month minimum, depending on your region. A managed RDS database will add additional monthly costs.

*Disclaimer: The maintainers are not responsible for unexpected AWS charges. Always monitor your AWS Billing Dashboard.*
