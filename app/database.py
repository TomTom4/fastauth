from sqlmodel import Field, Session, SQLModel, create_engine, select
import models
from configurations import Settings

settings = Settings()


connect_args = {"check_same_thread": False}
engine = create_engine(settings.database_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
