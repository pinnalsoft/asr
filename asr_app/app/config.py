from functools import lru_cache
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    db_connection: str = Field("mysql", env="DB_CONNECTION")
    db_host: str = Field(..., env="DB_HOST")
    db_port: int = Field(..., env="DB_PORT")
    db_database: str = Field(..., env="DB_DATABASE")
    db_username: str = Field(..., env="DB_USERNAME")
    db_password: str = Field(..., env="DB_PASSWORD")

    jwt_secret: str = Field(..., env="JWT_SECRET")
    jwt_expires_in_hours: int = Field(12, env="JWT_EXPIRES_IN_HOURS")

    class Config:
        env_file = ".env"
        case_sensitive = False

    @property
    def sqlalchemy_database_url(self) -> str:
        return (
            f"{self.db_connection}+pymysql://{self.db_username}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_database}"
        )


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
