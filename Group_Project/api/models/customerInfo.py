from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), index=True, nullable=True)
    email = Column(String(100), primary_key=True, index=True, nullable=True)
    phone = Column(String(15), index=True, nullable=True)
    address = Column(String(100), index=True, nullable=True)

    accountID = Column(Integer, ForeignKey("accounts.id"), index=True, nullable=True)


    account = relationship("Account", back_populates="customer")
    order_details = relationship("Order_Details", back_populates="order_cust")







