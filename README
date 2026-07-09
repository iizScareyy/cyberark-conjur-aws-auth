# 🔐 Cloud-Native Secrets Management with CyberArk Conjur, Terraform, AWS & Python

![Terraform](https://img.shields.io/badge/Terraform-1.x-623CE4?logo=terraform)
![AWS](https://img.shields.io/badge/AWS-EC2-FF9900?logo=amazonaws)
![CyberArk](https://img.shields.io/badge/CyberArk-Conjur-blue)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python)
![Docker](https://img.shields.io/badge/Docker-D2496ED?logo=docker)
![License](https://img.shields.io/badge/License-MIT-green)

An end-to-end cloud security project that provisions AWS infrastructure using Terraform, deploys CyberArk Conjur OSS on Amazon EC2 using Docker, and demonstrates secure runtime secret retrieval through a Python application without hardcoded credentials.

---

# 📖 Overview

Modern applications often require access to sensitive information such as database passwords, API keys, and service credentials. These secrets are commonly stored inside source code, configuration files, or environment variables, increasing the risk of accidental exposure and making credential rotation difficult.

This project demonstrates a centralized secrets management solution using **CyberArk Conjur OSS**.

The infrastructure is provisioned using **Terraform**, while a Python application deployed on **Amazon EC2** authenticates to Conjur using a dedicated **Host Identity** and retrieves secrets securely at runtime through the **Conjur REST API**.

The project follows security best practices by implementing:

- Runtime secret retrieval
- Least-Privilege authorization
- Infrastructure as Code
- Centralized secrets management
- Secret rotation without application code changes

---

# ✨ Features

- Modular Terraform infrastructure
- AWS VPC, IAM, EC2 and Security Groups
- AWS Systems Manager (SSM) connectivity
- Dockerized CyberArk Conjur OSS
- Python REST API integration
- Host Identity authentication
- Least-Privilege authorization policies
- Runtime secret retrieval
- Centralized secret rotation
- Infrastructure as Code

---

# 🏗️ Architecture

# 🏗️ Architecture

<p align="center">
  <img src="docs/architecture.png" alt="Cloud-Native Secrets Management Architecture" width="100%">
</p>

<p align="center">
Terraform provisions the AWS infrastructure, while the Python application running on Amazon EC2 authenticates to CyberArk Conjur using a dedicated Host Identity and securely retrieves runtime secrets through the Conjur REST API.
</p>

---

# 🔄 Authentication Flow

```mermaid
sequenceDiagram

    participant App as Python Application
    participant Conjur as CyberArk Conjur

    App->>Conjur: Authenticate (Host Identity + API Key)
    Conjur-->>App: Access Token

    App->>Conjur: Request Database Username
    Conjur-->>App: Username

    App->>Conjur: Request Database Password
    Conjur-->>App: Password

    App->>App: Consume Retrieved Credentials
```

---

# ⚙️ Architecture Overview

The project consists of the following components:

| Component | Purpose |
|-----------|---------|
| Terraform | Provisions AWS infrastructure |
| Amazon EC2 | Hosts the Python application and CyberArk Conjur |
| AWS IAM | Provides secure instance permissions |
| AWS Systems Manager | Secure administration without SSH |
| Docker | Runs the Conjur platform |
| CyberArk Conjur OSS | Centralized secrets management |
| Python Client | Authenticates and retrieves secrets through the REST API |

---

# 📂 Repository Structure

```
cyberark-conjur-aws-auth/

├── app/
│   ├── config.py
│   ├── conjur_client.py
│   ├── main.py
│   ├── requirements.txt
│   └── .env.example
│
├── terraform/
│   ├── modules/
│   ├── providers.tf
│   ├── versions.tf
│   ├── variables.tf
│   ├── outputs.tf
│   ├── main.tf
│   └── terraform.tfvars.example
│
├── conjur/
│   ├── conjur-quickstart/
│   └── policies/
│
├── README.md
├── LICENSE
└── .gitignore
```

---

# 🛠️ Technology Stack

### Cloud

- Amazon EC2
- Amazon VPC
- AWS IAM
- AWS Systems Manager (SSM)

### Infrastructure

- Terraform
- Docker
- Docker Compose

### Secrets Management

- CyberArk Conjur OSS
- Conjur Policies
- REST API Authentication

### Development

- Python
- Requests

---

# 🚀 Getting Started

## Prerequisites

- AWS Account
- Terraform
- Docker Desktop
- Python 3.x
- Git
- AWS CLI

---

## 1. Clone the repository

```bash
git clone https://github.com/iizScareyy/cyberark-conjur-aws-auth.git

cd cyberark-conjur-aws-auth
```

---

## 2. Configure Terraform

Copy the example variables file.

```bash
cp terraform/terraform.tfvars.example terraform/terraform.tfvars
```

Update the required values inside `terraform.tfvars`.

---

## 3. Provision AWS Infrastructure

```bash
cd terraform

terraform init

terraform apply
```

Terraform provisions:

- VPC
- Public Subnet
- Internet Gateway
- Route Table
- Security Group
- IAM Role
- IAM Instance Profile
- Amazon EC2 Instance

---

## 4. Deploy CyberArk Conjur

```bash
cd ../conjur/conjur-quickstart

docker-compose up -d
```

Initialize Conjur and load the required policies.

---

## 5. Configure the Python Application

Copy

```
app/.env.example
```

to

```
app/.env
```

Update:

- Conjur URL
- Conjur Account
- Host Identity
- Host API Key

---

## 6. Install Dependencies

```bash
cd app

pip install -r requirements.txt
```

---

## 7. Run the Application

```bash
python main.py
```

Example output

```
==========================================

Authentication successful

Database Username : postgres

Database Password : ********

==========================================
```

---

# 🔁 Secret Rotation Demonstration

Secrets can be rotated centrally without modifying application code.

Update the stored password:

```bash
docker-compose exec client \
conjur variable set \
-i aws/database/password \
-v NewSecurePassword123
```

Run the application again.

The application automatically retrieves the updated credential from Conjur.

No code changes.

No redeployment.

No configuration updates.

---

# 🔒 Security Highlights

- No hardcoded credentials
- Dedicated application Host Identity
- Least-Privilege authorization
- Runtime secret retrieval
- Centralized secrets management
- Infrastructure provisioned with Terraform
- Secure EC2 administration through AWS Systems Manager
- Secret rotation without modifying application code

---

# 💡 Design Decisions

## Why Terraform?

Terraform provides repeatable, version-controlled infrastructure provisioning and enables the environment to be recreated with a single command.

---

## Why CyberArk Conjur?

CyberArk Conjur provides centralized secrets management, policy-based authorization, and runtime secret retrieval for applications.

---

## Why a Dedicated Host Identity?

The application authenticates using a dedicated Conjur Host Identity instead of administrative credentials.

This ensures the application can retrieve only the secrets explicitly permitted by policy, following the Principle of Least Privilege.

---

## Why REST API Integration?

The application communicates directly with the Conjur REST API rather than invoking the Conjur CLI, closely reflecting how production services integrate with enterprise secrets management platforms.

---

# 🧩 Challenges Solved

During development the following implementation challenges were encountered and resolved:

- Configured IAM Roles and Instance Profiles for EC2.
- Diagnosed AWS Systems Manager registration failures caused by restrictive Security Group egress rules.
- Installed and configured Docker Compose on Amazon Linux 2023.
- Implemented Conjur Host Identity authentication.
- Created least-privilege authorization policies for application access.
- Demonstrated centralized secret rotation without modifying application code.

---

# 🚧 Future Improvements

- Deploy Conjur on Amazon EKS
- Implement CI/CD deployment pipeline
- Integrate enterprise workload identity authentication
- Automate TLS certificate management
- Add monitoring and audit dashboards
- Replace demo Host API Key bootstrap with production-grade workload authentication

---

# 📚 Learning Outcomes

This project demonstrates practical experience with:

- Infrastructure as Code
- Cloud Infrastructure Provisioning
- AWS IAM
- AWS Systems Manager
- Docker
- CyberArk Conjur OSS
- REST API Integration
- Python
- Secrets Management
- Least-Privilege Security Design
- Runtime Authentication
- Infrastructure Automation

---

# 🙏 Acknowledgements

The Docker-based Conjur environment is based on the official CyberArk Conjur OSS Quickstart.

The AWS infrastructure, Terraform modules, Conjur policies, Python client, authentication flow, EC2 deployment, and end-to-end secrets management workflow were designed and implemented as part of this project.

---

# 📄 License

This project is licensed under the MIT License.