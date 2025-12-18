from app.pro.registry.sectors import SECTORS
from app.pro.registry.jobs import JOBS

def build_context(payload: dict) -> dict:
    job = JOBS[payload["job"]]
    sector = SECTORS[job["sector"]]
    return {
        "sector": sector["label"],
        "job": job["label"],
        "capabilities": sector["capabilities"],
        "focus": job["focus"],
        "company_size": payload.get("size"),
        "project_type": payload.get("project_type"),
        "constraints": payload.get("constraints"),
        "goals": payload.get("goals")
    }
