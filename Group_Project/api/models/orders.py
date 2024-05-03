from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    status = Column(String(100), index=True, nullable=False)
    description = Column(String(100), index=True, nullable=False)
    total_price = Column(Float, index=True, nullable=False)


    custID = Column(Integer, ForeignKey("customers.id"), index=True)
    dishID = Column(Integer, ForeignKey("dishes.id"), index=True)

    cust = relationship("Customer", foreign_keys=[custID])
    dish = relationship("Dish", foreign_keys=[dishID])


