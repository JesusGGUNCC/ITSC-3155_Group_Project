from sqlalchemy import Column, Integer, String, Text, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    payment_type = Column(String(100), nullable=False)
    transaction_status = Column(String(100), nullable=False)
    payment_information = Column(Text, nullable=True)