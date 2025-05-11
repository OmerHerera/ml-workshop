"""
data_source_remote.py

Handles access to a public API (e.g., JSONPlaceholder).
"""

import requests

API_BASE = "https://jsonplaceholder.typicode.com"

def get_remote_context(endpoint):
    try:
        response = requests.get(f"{API_BASE}/{endpoint}")
        return response.json()
    except Exception as e:
        return {"error": str(e)}
