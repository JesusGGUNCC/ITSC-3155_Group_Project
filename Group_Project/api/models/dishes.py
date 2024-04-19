from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Dish(Base):
   __tablename__ = "dishes"


   id = Column(Integer, autoincrement=True)
   dish_name = Column(String(100), unique=True, nullable=True)
   price = Column(DECIMAL, index=True, nullable=False, server_default='0.0')
   calories = Column(Integer, index=True, nullable=False, server_default='0.0')
   menu_category = Column(String(100), ForeignKey("menu.category"))




   menu = relationship("menu", back_populates="dishes")