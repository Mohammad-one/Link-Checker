from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Link(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True, index=True)
    source_url = Column(String, nullable=False)
    url = Column(String, nullable=False)
    type = Column(String, nullable=False)
