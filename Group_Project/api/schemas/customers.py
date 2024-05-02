from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class CustomerBase(BaseModel):
    name: str
    email: str
    phone: str
    address: str

class CustomerCreate(CustomerBase):
    pass

# Not optional because these things cannont be null
class CustomerUpdate(BaseModel):
    name: str
    email: str
    phone: str
    address: str

class Customer(CustomerBase):
    id: int
    class ConfigDict:
        from_attribute = True