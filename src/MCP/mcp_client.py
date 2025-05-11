"""
mcp_client.py

Acts as the MCP client that sends requests to the MCP server.
"""

import requests

SERVER_URL = "http://127.0.0.1:5000"

def request_context(source_type, payload):
    try:
        response = requests.post(f"{SERVER_URL}/context/{source_type}", json=payload)
        return response.json()
    except Exception as e:
        return {"error": str(e)}
