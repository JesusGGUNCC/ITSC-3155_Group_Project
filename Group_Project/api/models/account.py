from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), index=True)
    password = Column(String(100), index=True)

    name = Column(String(100), index=True)
    address = Column(String(100), index=True)
    phone = Column(String(100), index=True)


    customer = relationship("Customer", back_populates="account")