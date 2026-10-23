# AWS EC2 — Dockerized Incident API Deployment

## Project Overview

Deployed a containerized Python FastAPI application and PostgreSQL database on AWS EC2 using Docker Compose.

## Infrastructure

- Cloud provider: AWS
- Compute: Amazon EC2
- Operating system: Amazon Linux 2023
- Container runtime: Docker
- Container orchestration: Docker Compose
- Application: Python FastAPI
- Database: PostgreSQL 17
- Storage: Docker named volume backed by EC2 storage
- Networking: Docker bridge network and restricted AWS Security Group

## Deployment Process

1. Provisioned and secured an EC2 instance.
2. Installed Docker Engine and Docker Compose.
3. Transferred application source files using SCP.
4. Created Docker networking and persistent storage.
5. Generated environment-specific database credentials.
6. Built and deployed the application stack.
7. Verified application and database health.
8. Accessed the application through an SSH tunnel.

## Security Measures

- Restricted SSH to an approved source IP.
- Kept PostgreSQL inaccessible from the public internet.
- Used Docker Compose secrets for database credentials.
- Ran the API as a non-root user.
- Applied a read-only application filesystem.
- Configured resource limits and health checks.

## Troubleshooting and Recovery

Tested database failure recovery, application logs, and container recreation.

## Validation

Verified that the application responds to health checks and retains database records across container recreation.

## Lessons Learned

Deploying an application involves more than copying source code. It requires configuring infrastructure, networking, secrets, persistent storage, monitoring, and recovery procedures.
