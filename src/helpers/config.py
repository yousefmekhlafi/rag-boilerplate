from pydantic_settings import BaseSettings, SettingsConfigDict

# This configuration class will be responsible for loading the .env file as well as configurations for the entire backend's logic
class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str

    CHUNKING_PROVIDER: str

    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE: int


    class Config:
        env_file = ".env"

def get_settings():
    return Settings() 


