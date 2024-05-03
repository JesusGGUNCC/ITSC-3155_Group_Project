from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Rating(Base):
    __tablename__ = "rating"

    id = Column(Integer, index=True, primary_key=True, autoincrement=True)

    dishID = Column(Integer, ForeignKey("dishes.id"), index=True)
    score = Column(Float, index=True)
    review = Column(String(100))

    dish = relationship("Dish", foreign_keys=[dishID])
