from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SUPABASE_URL: str = ""
    SUPABASE_KEY: str = ""
    DATABASE_URL: str = "sqlite:///./test.db" # Default placeholder

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
