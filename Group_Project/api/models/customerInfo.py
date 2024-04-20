from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, autoincrement=True)
    name = Column(String(100), index=True, primary_key=True)
    email = Column(String(100), index=True, primary_key=True)
    phone = Column(String(15), index=True, primary_key=True)
    address = Column(String(100), index=True, primary_key=True)

    accounts = relationship("Account", back_populates="customers")