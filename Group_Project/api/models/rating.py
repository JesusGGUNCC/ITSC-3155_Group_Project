from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Rating(Base):
    __tablename__ = "rating"

    id = Column(Integer, index=True, primary_key=True, autoincrement=True)

    score = Column(DECIMAL(2,2))
    review = Column(String(100))

    dish_id = Column(Integer, ForeignKey("dishes.id"))

    dID = relationship("Dish", back_populates="rating")
