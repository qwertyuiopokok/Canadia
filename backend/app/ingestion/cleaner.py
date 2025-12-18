def clean_text(text):
    """Basic text cleaner: strips and replaces multiple spaces."""
    if not isinstance(text, str):
        return text
    return ' '.join(text.strip().split())
