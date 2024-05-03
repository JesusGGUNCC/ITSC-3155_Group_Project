from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .dishes import Dish
from .customers import Customer

class OrderBase(BaseModel):
    status: str
    description: Optional[str] = None
    total_price: float


class OrderCreate(OrderBase):
    custID: int
    dishID: int

class OrderUpdate(BaseModel):
    status: Optional[str] = None
    description: Optional[str] = None
    total_price: Optional[int] = None
    custID: Optional[int] = None
    dishID: Optional[int] = None

class Order(OrderBase):
    id: int
    customer: Customer = None
    dish: Dish = None

    class ConfigDict:
        from_attribute = True