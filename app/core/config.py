from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI deploy-stack example"
    
    # deploy-stack automatically injects these into ECS memory from AWS Secrets Manager
    DB_HOST: Optional[str] = None
    DB_USER: Optional[str] = None
    DB_PASSWORD: Optional[str] = None
    DB_NAME: Optional[str] = None
    DB_PORT: int = 5432
    
    @property
    def database_url(self) -> Optional[str]:
        if all([self.DB_HOST, self.DB_USER, self.DB_PASSWORD, self.DB_NAME]):
            return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        # Fallback for local development if no .env is provided
        return "sqlite:///./local.db"
    # Tells Pydantic to read from a local .env file during development
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

settings = Settings()