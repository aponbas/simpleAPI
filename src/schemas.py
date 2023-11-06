from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String

Base = declarative_base()


class User(Base):
    __tablename__ = "example.user"

    user_id: str = Column("user_id", String, primary_key=True)
    username: str = Column("username", String)
    password: str = Column("password", String)
