"""
host.py

Simulates a tool (e.g., IDE or AI agent) that sends context requests to the MCP client.
"""

from mcp_client import request_context

# Example: Request file content
print("[Host] Requesting local file context...")
response = request_context("local", {"filename": "example.txt"})
print("[Host] Response:", response)

# Example: Request remote API data
print("\n[Host] Requesting remote API context...")
response = request_context("remote", {"endpoint": "posts/1"})
print("[Host] Response:", response)
