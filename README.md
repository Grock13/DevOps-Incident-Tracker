project now uses PostgreSQL, a Docker bridge network, a named volume, and database-backed API endpoints.
docker ps
docker network inspect incident-net
docker volume ls
docker logs incident-api
how to start your application with Docker Compose.
docker compose up -d --build
docker compose ps
docker compose logs --tail 20
docker compose down


A hands-on DevOps portfolio project demonstrating how to build, containerize, secure, deploy, and troubleshoot a Python FastAPI application connected to PostgreSQL.

The application uses Docker Compose for multi-container orchestration, persistent Docker volumes for database storage, health checks for service monitoring, and Docker Compose secrets for database credentials.

The complete stack was deployed on AWS EC2 and accessed securely through an SSH tunnel. The project includes automated API tests, smoke tests, and simulated incident-response exercises.
