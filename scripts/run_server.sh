#!/bin/bash

# Activate virtual environment if exists
if [ -d "venv" ]; then
  source venv/bin/activate
fi

# Export environment variables
export PYTHONPATH=.
export UVICORN_CMD="backend.api.server:app"

# Run with uvicorn (default)
echo "[SyntharaOS] Starting API server..."
uvicorn $UVICORN_CMD --host 0.0.0.0 --port 8000 --reload