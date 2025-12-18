
from fastapi import APIRouter, Query, Request
from pydantic import BaseModel, Field
from typing import Optional, List, Literal, Any
from uuid import UUID
from datetime import date
from backend.app.main import FilterPayload, FilterCondition, Operator, Pagination, Sort


router = APIRouter()

# Stockage centralisé en mémoire (à remplacer par une vraie base si besoin)
SIGNALS_STORE = []


# Sous-modèles pour enrichir Signal
class Source(BaseModel):
    nom: str
    url: Optional[str] = None
    type: Optional[Literal["gouvernement", "media", "organisme", "citoyen"]] = None

class Geographie(BaseModel):
    niveau: Literal["canada", "province", "region"]
    description: Optional[str] = None

class Signal(BaseModel):
    content_id: UUID = Field(..., description="ID unique du contenu")
    valeur: float = Field(..., description="Valeur associée au signal")
    date_signal: date = Field(..., description="Date du signal")
    contexte: Optional[str] = Field(None, description="Contexte ou sujet du signal")
    audience: Optional[str] = Field(None, description="À qui s'adresse ce signal ?")
    geographie: Optional[Geographie] = Field(None, description="Où ça s'applique ?")
    source: Optional[Source] = Field(None, description="Source du signal")



@router.post("/signals", response_model=Signal)
def create_signal(signal: Signal):
    """Crée un nouveau signal enrichi, le stocke et retourne le payload pour validation."""
    SIGNALS_STORE.append(signal)
    return signal


# Endpoint pour exposer tous les signaux centralisés

# Helper: apply a single filter condition
def match_condition(signal: Any, cond: FilterCondition) -> bool:
    value = getattr(signal, cond.field, None)
    if cond.operator == Operator.eq:
        return value == cond.value
    elif cond.operator == Operator.ne:
        return value != cond.value
    elif cond.operator == Operator.lt:
        return value < cond.value
    elif cond.operator == Operator.lte:
        return value <= cond.value
    elif cond.operator == Operator.gt:
        return value > cond.value
    elif cond.operator == Operator.gte:
        return value >= cond.value
    elif cond.operator == Operator.contains:
        return cond.value in value if value is not None else False
    elif cond.operator == Operator.in_:
        return value in cond.value if value is not None else False
    return True

# Helper: apply all filters
def filter_signals(signals: List[Signal], filters: List[FilterCondition]) -> List[Signal]:
    result = signals
    for cond in filters:
        result = [s for s in result if match_condition(s, cond)]
    return result

# Helper: sort signals
def sort_signals(signals: List[Signal], sort: Optional[List[Sort]]) -> List[Signal]:
    if not sort:
        return signals
    for s in reversed(sort):
        signals = sorted(signals, key=lambda x: getattr(x, s.field, None), reverse=(s.order=="desc"))
    return signals

# Helper: paginate
def paginate_signals(signals: List[Signal], pagination: Optional[Pagination]) -> List[Signal]:
    if not pagination:
        return signals
    start = (pagination.page - 1) * pagination.page_size
    end = start + pagination.page_size
    return signals[start:end]

@router.get("/signals", response_model=List[Signal])
def get_signals(
    request: Request,
    filters: Optional[str] = Query(None, description="JSON list of filter conditions (field, operator, value)"),
    sort: Optional[str] = Query(None, description="JSON list of sort objects (field, order)"),
    page: int = Query(1, ge=1, description="Page number for pagination"),
    page_size: int = Query(20, ge=1, le=100, description="Page size for pagination")
):
    """
    Recherche, filtre, trie et pagine les signaux centralisés en mémoire.
    - filters: JSON list of {field, operator, value}
    - sort: JSON list of {field, order}
    - page, page_size: pagination
    """
    import json
    signals = SIGNALS_STORE
    # Parse filters
    filter_objs = []
    if filters:
        try:
            filter_list = json.loads(filters)
            for f in filter_list:
                filter_objs.append(FilterCondition(**f))
        except Exception as e:
            return []
    # Parse sort
    sort_objs = []
    if sort:
        try:
            sort_list = json.loads(sort)
            for s in sort_list:
                sort_objs.append(Sort(**s))
        except Exception as e:
            pass
    # Pagination
    pagination = Pagination(page=page, page_size=page_size)
    # Filtering
    filtered = filter_signals(signals, filter_objs) if filter_objs else signals
    # Sorting
    sorted_signals = sort_signals(filtered, sort_objs) if sort_objs else filtered
    # Pagination
    paginated = paginate_signals(sorted_signals, pagination)
    return paginated
