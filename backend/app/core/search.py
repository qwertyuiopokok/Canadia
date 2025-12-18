def search_content(contents: list, analysis: dict) -> list:
    results = []
    for c in contents:
        theme_match = any(t in c.get("themes", []) for t in analysis.get("themes", [])) if analysis.get("themes") else True
        geo_match = True
        if "geo" in c and analysis.get("geo"):
            geo_match = c["geo"].lower() == analysis["geo"].lower()
        if theme_match and geo_match:
            results.append(c)
    return results
