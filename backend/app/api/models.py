
from pydantic import BaseModel
from typing import List, Optional, Dict

class ContentResponse(BaseModel):
    fingerprint: str
    title: str
    content: str
    source: Dict
    themes: List[str]
    geography: Dict
    last_updated: Optional[str]
    status: str
