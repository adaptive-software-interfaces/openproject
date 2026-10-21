from adaptive_ui_service.app.routes.health import health_check


def test_health_check() -> None:
    response = health_check()

    assert response["status"] == "ok"
