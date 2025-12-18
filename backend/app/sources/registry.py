from enum import Enum

class SourceType(str, Enum):
    GOVERNMENT = "government"
    MEDIA = "media"
    ORGANISM = "organism"
    ACADEMIC = "academic"

SOURCES = [
    {
        "id": "canada-gov",
        "name": "Gouvernement du Canada",
        "type": SourceType.GOVERNMENT,
        "priority": 1,
        "trust": 1.0,
        "rss": [
            "https://www.canada.ca/en/news/web-feeds/rss.html"
        ]
    },
    {
        "id": "radio-canada",
        "name": "Radio-Canada",
        "type": SourceType.MEDIA,
        "priority": 2,
        "trust": 0.9,
        "rss": [
            "https://ici.radio-canada.ca/rss/4159"
        ]

    }
]

# Ajout d'une source supplémentaire après la définition de SOURCES
SOURCES.append({
    "id": "radio-canada-actualites",
    "name": "Radio-Canada - Actualités",
    "type": SourceType.MEDIA,
    "priority": 2,
    "trust": 0.9,
    "rss": [
        "https://ici.radio-canada.ca/rss/4159"
    ]
})
