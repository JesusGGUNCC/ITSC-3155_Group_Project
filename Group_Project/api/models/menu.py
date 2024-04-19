from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Menu(Base):
   __tablename__ = "menu"


   id = Column(Integer, autoincrement=True)
   category = Column(String(100), unique=True, nullable=True)


   dishes = relationship("dishes", back_populates="menu")


git