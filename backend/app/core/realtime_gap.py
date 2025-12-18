from app.storage.evolution_store import upsert_gap

def create_gap_now(theme: str, question: str, province: str=None):
    key = f"realtime:{theme}:{province or 'CAN'}"
    upsert_gap(
        key=key,
        theme=theme,
        province=province or "CAN",
        region=None,
        example_question=question,
        priority=5  # 🔥 priorité MAX
    )
