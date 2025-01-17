import os
from pydantic import SecretStr, Secret, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(__file__), ".envs/.env")
    )
    TELEGRAM_API_KEY: SecretStr = SecretStr("secret")
    LOG_LEVEL: str = "INFO"

    POSTGRES_DSN: Secret[PostgresDsn] = Secret(
        PostgresDsn("postgresql://postgres:password@localhost:5432/postgres")
    )
