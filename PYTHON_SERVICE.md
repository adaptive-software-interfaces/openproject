# Adaptive UI service

The FastAPI service is isolated in `adaptive_ui_service/` so it does not conflict with OpenProject's Rails `app/` directory. The repository-root `main.py` is the service entry point required by the initial BFF task.

## Local setup

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn main:app --reload
```

The service listens on `http://127.0.0.1:8000`. Its health endpoint is available at `GET /health` and returns the service status and version.

Install the development dependencies and enable the pre-commit hooks with:

```bash
pip install -r requirements-dev.txt
pre-commit install
```

Configuration is loaded from `.env` and the process environment by `adaptive_ui_service/app/core/config.py`. Keep credentials in `.env`; it is ignored by Git.