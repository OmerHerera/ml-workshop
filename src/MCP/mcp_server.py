"""
mcp_server.py

Implements the MCP Server that exposes access to local and remote data sources.
"""

from flask import Flask, request, jsonify
from data_source_local import get_local_context
from data_source_remote import get_remote_context

app = Flask(__name__)

@app.route("/context/local", methods=["POST"])
def context_local():
    data = request.get_json()
    result = get_local_context(data.get("filename"))
    return jsonify(result)

@app.route("/context/remote", methods=["POST"])
def context_remote():
    data = request.get_json()
    result = get_remote_context(data.get("endpoint"))
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
