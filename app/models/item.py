from sqlalchemy import Column, Integer, String, Boolean
from bd import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100),nullable=False)
    existe = Column(Boolean)