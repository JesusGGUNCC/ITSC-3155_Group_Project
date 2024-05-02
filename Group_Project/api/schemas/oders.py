from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class OrderBase(BaseModel):
    status: str
    description: Optional[str] = None
    total_price: float


class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    status: Optional[str] = None
    description: Optional[str] = None
    total_price: Optional[str] = None

class Order(OrderBase):
    id: int
    date: Optional[datetime] = None

    class ConfigDict:
        from_attribute = True