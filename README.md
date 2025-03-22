**Project Overview**

This project implements a fully automated DevOps pipeline for a file upload web application, integrating Terraform, Docker, and Jenkins running locally to streamline infrastructure provisioning, containerization, and CI/CD automation. The application allows users to upload files via a web interface, which are then securely stored in an Amazon S3 bucket.  

**Key Technologies & Tools**
- Terraform – Infrastructure as Code.
- Docker – Containerization.
- Jenkins – CI/CD automation.
- Amazon S3 – Cloud storage.
- Python (Flask) – Backend framework.
- HTML – Frontend  
 
**Project Workflow**    
### 1.Infrastructure Provisioning with Terraform
- Terraform is used to create an Amazon S3 bucket with predefined security policies.
- The S3 bucket serves as cloud storage for uploaded user files.
### 2.Web Application Development (Python + HTML)
- A Flask-based backend processes file uploads and interacts with AWS S3 using the boto3 SDK.
- The HTML frontend provides a simple interface for users to upload files.
### 3.Containerization with Docker
- The application is packaged in a Docker container, ensuring a consistent runtime environment.
- The Dockerfile defines dependencies and configurations needed to run the application.
### 4.	CI/CD Automation with Jenkins
- Jenkins pipeline automates the build and deployment process.
- The pipeline fetches the code from the local machine, builds a Docker image, and runs the containerized application.
- Every code update in the local machine triggers Jenkins to rebuild and redeploy the application.

**CI/CD Pipeline Workflow**
### 1.	Jenkins detects code changes in the local machine.
### 2.	Build the Docker image of the web application.
### 3.	Run the containerized application locally.
### 4.	Deploy to S3, ensuring uploaded files are stored securely.


This project runs entirely on a local machine, with Terraform, Docker, and Jenkins automating the deployment process.
