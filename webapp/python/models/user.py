from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from ..database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(String)
    name = Column(String, primary_key=True, index=True)
    email = Column(String, index=True)
    hash_password = Column(String)
    display_name = Column(String, index=True)
