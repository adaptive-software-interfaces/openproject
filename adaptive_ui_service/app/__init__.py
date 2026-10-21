from fastapi import FastAPI

from adaptive_ui_service.app.core.config import get_settings
from adaptive_ui_service.app.routes.health import router as health_router


def create_app() -> FastAPI:
    settings = get_settings()
    application = FastAPI(title=settings.app_name, version=settings.app_version)
    application.include_router(health_router)
    return application
