from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PGRES_DSN: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
