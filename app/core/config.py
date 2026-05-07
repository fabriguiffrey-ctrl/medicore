from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # Config general
    PROJECT_NAME: str = "Service API"

    # Datos de la DB
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    # Construcción dinámica de la URL
    @property
    def DATABASE_URL(self):
        return (
            f"postgresql://{self.DB_USER}:"
            f"{self.DB_PASSWORD}@"
            f"{self.DB_HOST}:"
            f"{self.DB_PORT}/"
            f"{self.DB_NAME}"
        )

    class Config:
        env_file = ".env"


settings = Settings()

