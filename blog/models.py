from sqlalchemy import Column, INTEGER, String
from . database import Base

class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(INTEGER, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)