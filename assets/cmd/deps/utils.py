import re

def validate_url(url):
    """Validate the provided URL."""
    regex = r'^(https?:\/\/)?(www\.)?(youtube\.com|youtu\.?be)\/.+$'
    return re.match(regex, url) is not None

def format_output(title, link):
    """Format output for displaying video title and link."""
    return f"{title}: {link}"
