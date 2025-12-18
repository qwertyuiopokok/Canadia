# Keywords for tagging themes
KEYWORDS = {
	"logement": ["logement", "loyer", "habitation"],
	"santé": ["santé", "hôpital", "médecin"],
	"économie": ["économie", "inflation", "emploi"],
	"transport": ["transport", "tramway", "autoroute"]
}

# Tag content with themes and geography
def tag_content(content: dict) -> dict:
	text = (content["title"] + " " + content["content"]).lower()

	themes = [
		theme for theme, words in KEYWORDS.items()
		if any(w in text for w in words)
	]

	geography = {
		"level": "canada",
		"province": None,
		"region": None
	}

	if "québec" in text:
		geography["province"] = "QC"
		geography["level"] = "province"

	if "montréal" in text:
		geography["region"] = "Montréal"
		geography["level"] = "region"

	content["themes"] = themes
	content["geography"] = geography
	return content
"""
Theme and geography tagging utilities
"""
def tag_content(content: dict) -> dict:
	text = (content["title"] + " " + content["content"]).lower()

	themes = []
	if "logement" in text or "loyer" in text or "habitation" in text:
		themes.append("logement")
	if "canada" in text:
		themes.append("canada")

	geography = {
		"level": "canada",
		"province": None,
		"region": None
	}

	if "québec" in text:
		geography["level"] = "province"
		geography["province"] = "QC"

	content["themes"] = themes
	content["geography"] = geography
	return content
