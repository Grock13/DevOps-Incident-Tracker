import logging

from fastapi import FastAPI
from pydantic import BaseModel

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger("incident-api")

app = FastAPI(title="DevOps Incident API")

incidents = [
    {
        "id": 1,
        "service": "nginx",
        "status": "resolved",
        "summary": "HTTP port 80 was blocked"
    }
]

class Incident(BaseModel):
    service: str
    status: str
    summary: str

@app.get("/")
def home():
    return {"message": "Welcome to the DevOps Incident API"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/incidents")
def get_incidents():
    return incidents

@app.post("/incidents", status_code=201)
def create_incident(incident: Incident):
    record = {
        "id": len(incidents) + 1,
        **incident.model_dump()
    }

    incidents.append(record)

    logger.info(
        "Incident created: service=%s status=%s",
        incident.service,
        incident.status
    )

    return record
