from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .accounts import Account



class CustomerBase(BaseModel):
    name: str
    email: str
    phone: str
    address: str

class CustomerCreate(CustomerBase):
    accountID: Optional[int] = None


class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None

class Customer(CustomerBase):
    id: int
    account: Account = None
    class ConfigDict:
        from_attribute = True