from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .customers import Customer


class AccountBase(BaseModel):
    pass

class AccountCreate(AccountBase):
    username:str
    password: str


class AccountUpdate(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None

class Account(AccountBase):
    username: str
    accountInfo: Customer = None

    class ConfigDict:
        from_attributes = True


