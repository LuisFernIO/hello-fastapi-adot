#!/bin/bash

echo "Starting the FastAPI application with Uvicorn..."
opentelemetry-instrument uvicorn main:app --host 0.0.0.0 --port 8000 # INSTRUMENTATION