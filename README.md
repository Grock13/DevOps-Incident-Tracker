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
