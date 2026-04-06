from pydantic_settings import BaseSettings

<<<<<<< HEAD

class Settings(BaseSettings):

    PROJECT_NAME: str = "Service API"
    DATABASE_URL: str
=======
class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
>>>>>>> 84b76c2771508275288ddeba9bf9e93e98db1d3d

    class Config:
        env_file = ".env"

<<<<<<< HEAD

settings = Settings()
=======
settings = Settings()
>>>>>>> 84b76c2771508275288ddeba9bf9e93e98db1d3d
