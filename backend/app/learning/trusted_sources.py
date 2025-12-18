"""
Liste blanche officielle des sources fiables.
"""
TRUSTED_SOURCES = {
    "government": {
        "trust": 1.0,
        "domains": [
            "canada.ca",
            "quebec.ca",
            "ontario.ca",
            "gc.ca"
        ]
    },
    "public_agency": {
        "trust": 0.9,
        "domains": [
            "cmhc-schl.gc.ca",
            "statcan.gc.ca",
            "inspq.qc.ca"
        ]
    }
}

from urllib.parse import urlparse

def is_source_trusted(url: str) -> bool:
    domain = urlparse(url).netloc
    for group in TRUSTED_SOURCES.values():
        for d in group["domains"]:
            if domain.endswith(d):
                return True
    return False
