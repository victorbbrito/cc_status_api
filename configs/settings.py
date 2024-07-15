from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL:str = Field(default='postgresql+asyncpg://postgres:postgres@localhost:5432/cc_status')
    
settings = Settings()

# database url to connection