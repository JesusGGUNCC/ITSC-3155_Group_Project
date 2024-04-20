from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Dish(Base):
   __tablename__ = "dishes"


   id = Column(Integer, autoincrement=True, primary_key=True)
   dish_name = Column(String(100), unique=True, nullable=True)
   price = Column(DECIMAL, index=True, nullable=False, server_default='0.0')
   calories = Column(Integer, index=True, nullable=False, server_default='0.0')
   menu_category_id = Column(Integer, ForeignKey("menu.id"))




   menu = relationship("menu", back_populates="dishes")