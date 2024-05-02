from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Order_Details(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    customerID = Column(Integer, ForeignKey("customers.id"), index=True)
    dishID = Column(Integer, ForeignKey("dishes.id"), index=True)
    orderID = Column(Integer, ForeignKey("orders.id"), index=True)

    order_dish = relationship("Dish", back_populates="order_details")
    order_cust = relationship("Customer", back_populates="order_details")
    order = relationship("Order", back_populates="order_details")