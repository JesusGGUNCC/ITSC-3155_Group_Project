from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .customers import Customer
from .orders import Order


class OrderDetailBase(BaseModel):
    total: int


class OrderDetailCreate(OrderDetailBase):
    dish_id: int
    customer: Customer = None


class OrderDetailUpdate(BaseModel):
    dish_id: Optional[int] = None
    customer: Customer = None
    total: Optional[int] = None


class OrderDetail(OrderDetailBase):
    id: int
    dish_id: int
    customer: Customer = None
    order: Order = None

    class ConfigDict:
        from_attributes = True