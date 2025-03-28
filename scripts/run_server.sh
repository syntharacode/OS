#!/bin/bash

# Activate virtual environment if it exists
if [ -d "venv" ]; then
  source venv/bin/activate          # Enable local Python venv
fi

# Export PYTHONPATH so modules can be imported from project root
export PYTHONPATH=.

# Set the Uvicorn entrypoint for FastAPI server
export UVICORN_CMD="backend.api.server:app"

# Launch the FastAPI server using Uvicorn
echo "[SyntharaOS] Starting API server..."
uvicorn $UVICORN_CMD --host 0.0.0.0 --port 8000 --reload
