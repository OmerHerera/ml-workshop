# MCP Protocol Demo

This demo shows how to implement a simplified version of the Model Context Protocol (MCP) architecture in Python.

## 🧠 Architecture Overview

```
        ┌────────────┐
        │ MCP Host   │  <-- e.g., IDE or AI Tool
        └────┬───────┘
             │
      ╔══════▼══════╗
      ║ MCP Client  ║  <-- Communicates with MCP Server
      ╚══════┬══════╝
             │
       ┌─────▼─────┐
       │ MCP Server│  <-- Exposes capabilities via HTTP API
       └─────┬─────┘
             │
 ┌───────────▼─────────────┐
 │ Local Data Sources      │  e.g., files, SQLite
 └───────────┬─────────────┘
             │
 ┌───────────▼─────────────┐
 │ Remote Services (APIs)  │  e.g., public REST API
 └─────────────────────────┘
```

## Components

- `host.py`: Simulates an IDE requesting context.
- `mcp_client.py`: Sends structured requests to the MCP server.
- `mcp_server.py`: Receives requests, routes them to appropriate handlers.
- `data_source_local.py`: Reads from local files.
- `data_source_remote.py`: Queries a public API (JSONPlaceholder).

## How to Run

In separate terminals or background processes:

✅ Step 1: Create a Virtual Environment (recommended for macOS Homebrew)

```python
python3 -m venv venv
source venv/bin/activate
```

Then install the requirements:

```python
pip install -r requirements.txt
```

✅ Step 2: Run the MCP Server
In one terminal window:

```bash
python mcp_server.py
```

In another terminal:

```bash
python host.py
```

## Dependencies

- `Flask`
- `requests`
