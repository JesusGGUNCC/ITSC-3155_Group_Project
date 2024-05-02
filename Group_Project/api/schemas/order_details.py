from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .oders import Order
from .customers import Customer
from .dishes import Dish



class CustomerBase(BaseModel):
    pass

class CustomerCreate(CustomerBase):
    orderID: Optional[int] = None
    custID: Optional[int] = None
    dishID: Optional[int] = None


class CustomerUpdate(BaseModel):
    orderID: Optional[int] = None
    custID: Optional[int] = None
    dishID: Optional[int] = None

class Customer(CustomerBase):
    id: int
    order: Order = None
    cust: Customer = None
    dish: Dish = None

    class ConfigDict:
        from_attribute = True