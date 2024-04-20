from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Promotions(Base):
    __tablename__ = "promotions"
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    promo_code = Column(String(100), nullable=False)
    expiration_date = Column(String(100), nullable=False)