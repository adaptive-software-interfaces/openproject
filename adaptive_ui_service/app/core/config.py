from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = Field(
        default="Adaptive UI BFF", validation_alias="ADAPTIVE_UI_APP_NAME"
    )
    app_version: str = Field(
        default="0.1.0", validation_alias="ADAPTIVE_UI_APP_VERSION"
    )
    environment: str = Field(
        default="development", validation_alias="ADAPTIVE_UI_ENVIRONMENT"
    )
    host: str = Field(default="127.0.0.1", validation_alias="ADAPTIVE_UI_HOST")
    port: int = Field(default=8000, validation_alias="ADAPTIVE_UI_PORT")
    openproject_base_url: str = Field(
        default="http://localhost:3000",
        validation_alias="ADAPTIVE_UI_OPENPROJECT_BASE_URL",
    )
    openproject_api_token: str | None = Field(
        default=None, validation_alias="ADAPTIVE_UI_OPENPROJECT_API_TOKEN"
    )
    llm_base_url: str | None = Field(
        default=None, validation_alias="ADAPTIVE_UI_LLM_BASE_URL"
    )
    llm_api_key: str | None = Field(
        default=None, validation_alias="ADAPTIVE_UI_LLM_API_KEY"
    )
    llm_model: str = Field(
        default="gemini-2.5-flash", validation_alias="ADAPTIVE_UI_LLM_MODEL"
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_ignore_empty=True,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
