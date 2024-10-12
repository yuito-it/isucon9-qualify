from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from ..database import Base


class Config(Base):
    __tablename__ = "Congifs"
    name = Column(String, primary_key=True, index=True)
    value = Column(String)
