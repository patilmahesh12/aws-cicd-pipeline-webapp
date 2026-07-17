# 🚀 AWS CI/CD Automated Web Application

This project demonstrates a production-ready **CI/CD (Continuous Integration/Continuous Deployment) pipeline**. Whenever code is pushed to this repository, it is automatically deployed to an AWS EC2 instance, demonstrating real-world DevOps automation practices.

## 🏗️ Architecture Overview

*   **Version Control:** GitHub
*   **Automation:** GitHub Actions (CI/CD Pipeline)
*   **Infrastructure:** AWS EC2 (Amazon Linux 2023)
*   **Web Server:** Nginx
*   **Deployment Scripting:** Python (Paramiko library for SSH)

## ⚙️ How the Pipeline Works

1.  **Trigger:** A `git push` to the `main` branch triggers the GitHub Actions workflow.
2.  **Environment Setup:** The workflow installs necessary dependencies (`paramiko`) in the runner.
3.  **Secure Deployment:** The workflow uses GitHub Secrets to authenticate with your AWS EC2 instance.
4.  **Automated Update:** A Python script logs into the EC2 instance, pulls the latest code from GitHub, and restarts Nginx to reflect changes instantly.

## 🚀 Getting Started

To deploy this project yourself, you will need:
*   An AWS EC2 instance running Nginx.
*   Your AWS `.pem` private key (stored in GitHub Secrets as `PRIVATE_KEY`).
*   Your EC2 Public Host IP (stored in GitHub Secrets as `EC2_HOST`).

## 👤 About Me
Hi! I am Mahesh, a Cloud Engineer passionate about infrastructure as code, automation, and building scalable cloud solutions. This project showcases my ability to bridge the gap between development and operations.

---
*Built with passion for Cloud Computing and DevOps.*