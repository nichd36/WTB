# Variables
UV_NAME ?= venv
PYTHON_VERSION ?= 3.14

init-env:
	@echo "Setting up Virtual Environment with uv (Python $(PYTHON_VERSION))"
	uv venv $(UV_NAME) --python $(PYTHON_VERSION)