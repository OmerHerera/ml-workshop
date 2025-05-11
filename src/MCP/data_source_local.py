"""
data_source_local.py

Handles access to local files.
"""

def get_local_context(filename):
    try:
        with open(filename, "r") as f:
            return {"content": f.read()}
    except Exception as e:
        return {"error": str(e)}
