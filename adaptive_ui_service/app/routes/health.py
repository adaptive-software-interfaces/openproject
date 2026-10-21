from fastapi import APIRouter

from adaptive_ui_service.app.core.config import get_settings


router = APIRouter(tags=["health"])


@router.get("/health")
def health_check() -> dict[str, str]:
    settings = get_settings()
    return {"status": "ok", "version": settings.app_version}