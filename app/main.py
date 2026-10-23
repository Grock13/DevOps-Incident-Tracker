import os
import logging
from contextlib import asynccontextmanager 
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger("incident-api")

# Read database settings from environment variables
db_url = URL.create(
    "postgresql+psycopg",
    username=os.environ["POSTGRES_USER"],
    password=Path(
    os.environ["POSTGRES_PASSWORD_FILE"]
).read_text(encoding="utf-8").rstrip("\n"),
    host=os.getenv("DB_HOST", "incident-db"),
    port=int(os.getenv("DB_PORT", "5432")),
    database=os.environ["POSTGRES_DB"]
)

engine = create_engine(db_url, pool_pre_ping=True)


# Run once when the application starts
@asynccontextmanager
async def lifespan(app: FastAPI):
    with engine.begin() as connection:
        connection.execute(text("""
            CREATE TABLE IF NOT EXISTS incidents (
                id BIGSERIAL PRIMARY KEY,
                service TEXT NOT NULL,
                status TEXT NOT NULL,
                summary TEXT NOT NULL
            )
        """))

        # Add a sample incident only to an empty database
        connection.execute(text("""
            INSERT INTO incidents (service, status, summary)
            SELECT 'nginx', 'resolved',
                   'HTTP port 80 was blocked'
            WHERE NOT EXISTS (
                SELECT 1 FROM incidents
            )
        """))

    logger.info("Database initialized")
    yield
    engine.dispose()


app = FastAPI(
    title="DevOps Incident API",
    lifespan=lifespan
)


class Incident(BaseModel):
    service: str
    status: str
    summary: str


@app.get("/")
def home():
    return {"message": "Welcome to the DevOps Incident API"}


@app.get("/health")
def health():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "database": "connected"
        }

    except Exception:
        logger.exception("Database health check failed")
        raise HTTPException(
            status_code=503,
            detail="Database unavailable"
        )


@app.get("/incidents")
def get_incidents():
    with engine.connect() as connection:
        results = connection.execute(text("""
            SELECT id, service, status, summary
            FROM incidents
            ORDER BY id
        """))

        return [dict(row) for row in results.mappings()]


@app.post("/incidents", status_code=201)
def create_incident(incident: Incident):
    with engine.begin() as connection:
        result = connection.execute(
            text("""
                INSERT INTO incidents (service, status, summary)
                VALUES (:service, :status, :summary)
                RETURNING id, service, status, summary
            """),
            incident.model_dump()
        )

        record = dict(result.mappings().one())

    logger.info(
        "Incident created: id=%s service=%s status=%s",
        record["id"],
        record["service"],
        record["status"]
    )

    return record
