
from fastapi import APIRouter, Query
from typing import Optional
from app.storage.content_store import all_contents, get_by_fingerprint
from app.storage.feedback_store import get_feedback_score_by_fingerprint
from app.api.models import ContentResponse

router = APIRouter(
    prefix="/content",
    tags=["content"]
)

@router.get("/alerts", response_model=list[ContentResponse])
def get_alerts_content():
    contents = all_contents()
    return [
        c for c in contents
        if c.get("content_type") == "alert"
    ]

@router.get("/latest", response_model=list[ContentResponse])
def latest_content():
    contents = all_contents()
    items = sorted(
        [c for c in contents if c.get("status") == "new" or c.get("status") == "updated"],
        key=lambda x: x.get("last_updated", ""),
        reverse=True
    )[:10]
    return items
from fastapi import APIRouter, Query
from typing import Optional
from app.storage.content_store import all_contents, get_by_fingerprint
from app.api.models import ContentResponse

router = APIRouter(
    prefix="/content",
    tags=["content"]
)

@router.get("/", response_model=list[ContentResponse])
def list_content(
    theme: Optional[str] = Query(None),
    province: Optional[str] = Query(None),
    region: Optional[str] = Query(None),
    status: Optional[str] = Query(None)
):
    contents = all_contents()
    results = []

    for c in contents:
        if theme and theme not in c.get("themes", []):
            continue

        geo = c.get("geography", {})
        if province and geo.get("province") != province:
            continue

        if region and geo.get("region") != region:
            continue

        if status and c.get("status") != status:
            continue

        results.append(c)

    return results

@router.get("/{fingerprint}", response_model=ContentResponse)
def get_content(fingerprint: str):
    item = get_by_fingerprint(fingerprint)
    if not item:
        return {"error": "Not found"}
    return item

from typing import Optional

@router.get("/personalized")
def personalized_content(
    province: Optional[str] = None
):
    contents = all_contents()
    results = []

    for c in contents:
        geo = c.get("geography", {})
        if province and geo.get("province") != province:
            continue

        score = get_feedback_score_by_fingerprint(c["fingerprint"])
        c["feedback_score"] = score
        results.append(c)

    results.sort(
        key=lambda x: (
            x["feedback_score"],
            x["last_updated"]
        ),
        reverse=True
    )

    return results
