from datetime import datetime
from typing import Optional
from pydantic import BaseModel



class PaymentBase(BaseModel):
    payment_type: str
    transaction_status: str
    payment_information: str

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(BaseModel):
    payment_type: str
    transaction_status: str
    payment_information: str

class Payment(PaymentBase):
    id: int

    class ConfigDict:
        from_attribute = True