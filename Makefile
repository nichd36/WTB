# Variables
UV_NAME ?= venv
PYTHON_VERSION ?= 3.14

init-env:
	@echo "Setting up Virtual Environment with uv (Python $(PYTHON_VERSION))"
	uv venv $(UV_NAME) --python $(PYTHON_VERSION)
	@echo "Installing dependencies"
	uv sync

start:
	uv run uvicorn src.server:app --reload --host 0.0.0.0 --port 8000