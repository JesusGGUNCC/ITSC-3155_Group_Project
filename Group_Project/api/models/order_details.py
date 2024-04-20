from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class OrderDetail(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    cust_name = Column(String(100), ForeignKey("customers.name"))
    cust_email = Column(String(100), ForeignKey("customers.email"))
    cust_phone = Column(String(15), ForeignKey("customers.phone"))
    cust_address = Column(String(100), ForeignKey("customers.address"))

    dish_id = Column(Integer, ForeignKey("dishes.id"))


    name = relationship("Customer", back_populates="order_details")
    email = relationship("Customer", back_populates="order_details")
    phone = relationship("Customer", back_populates="order_details")
    address = relationship("Customer", back_populates="order_details")
    dish = relationship("Dish", back_populates="order_details")
