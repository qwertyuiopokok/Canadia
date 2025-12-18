def llm_suggest_sources(theme: str, province: str) -> list:
    """
    Appel LLM EXTERNE (ChatGPT ou autre)
    pour SUGGÉRER des sources, jamais pour des faits.
    """
    return [
        {
            "source_name": "SCHL",
            "source_url": "https://www.cmhc-schl.gc.ca",
            "method": "llm",
            "notes": "Suggestion LLM: Organisme fédéral officiel"
        }
    ]
