from app.storage.evolution import log_question, upsert_gap

# Après avoir déterminé coverage et used_web
log_question(question, coverage, used_web, province=province, region=region)

if coverage in ("none", "partial"):
    key = f"{domain}:{province or 'CAN'}:{region or 'ALL'}"
    upsert_gap(
        key=key,
        theme=domain,
        province=province or "CAN",
        region=region,
        example_question=question,
        priority=10 if coverage == "none" else 30
    )
