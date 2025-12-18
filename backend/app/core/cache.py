import time

_cache = {}
_CACHE_TTL = 300  # 5 minutes

def get_cache(key):
    item = _cache.get(key)
    if not item:
        return None
    if item["expires"] < time.time():
        _cache.pop(key, None)
        return None
    return item["value"]

def set_cache(key, value):
    _cache[key] = {
        "value": value,
        "expires": time.time() + _CACHE_TTL
    }
