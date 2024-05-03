from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Promotions(Base):
    __tablename__ = "promotions"
    
    id = Column(Integer,  primary_key=True, autoincrement=True)
    promo_code = Column(String(100), nullable=False)
    expiration_date = Column(String(100), nullable=True)
    category = Column(String(100), nullable=False)
    description = Column(String(100), nullable=False)