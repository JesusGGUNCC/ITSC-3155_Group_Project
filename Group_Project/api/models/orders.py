from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    status = Column(String(100), index=True, nullable=False)
    desciprtion = Column(String(100), index=True, nullable=False)
    total_price = Column(Float, index=True, nullable=False)
    date = Column(DATETIME, index=True, nullable=False)

    order_details = relationship("Order_Details", back_populates="order")