from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    warehouse_api_host: str = '0.0.0.0'
    warehouse_api_port: int = 8080

    warehouse_db_name: str = 'warehouse_database'
    warehouse_db_user: str = 'app'
    warehouse_db_password: str = '123qwe'
    warehouse_db_host: str = 'postgres_db'
    warehouse_db_port: int = 5432

settings = Settings()
