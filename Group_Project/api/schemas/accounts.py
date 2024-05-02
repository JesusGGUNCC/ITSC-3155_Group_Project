from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class AccountBase(BaseModel):
    username:str
    name: str
    phone: str
    address: str

class AccountCreate(AccountBase):
    pass
    password: str


class AccountUpdate(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None

class Account(AccountBase):
    id: int

    class ConfigDict:
        orm_mode = True


