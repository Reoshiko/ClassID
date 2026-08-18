from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )
    DB_URL: str = "sqlite+aiosqlite:///./class.db"
    DB_ECHO: bool = False
    ALLOWED_HOSTS: list[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ]

    @field_validator("ALLOWED_HOSTS", mode="before")
    @classmethod
    def split_hosts(cls, value: str | list[str]) -> list[str]:
        if isinstance(value, str):
            return [host.strip() for host in value.split(",") if host.strip()]
        return value


settings = Settings()
