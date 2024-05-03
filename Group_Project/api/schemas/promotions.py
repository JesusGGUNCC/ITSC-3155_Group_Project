from datetime import datetime
from typing import Optional
from pydantic import BaseModel



class PromotionBase(BaseModel):
    promo_code: str
    description: Optional[str] = None


class PromotionCreate(PromotionBase):
    category: str
    expiration_date: Optional[datetime] = None


class PromotionUpdate(BaseModel):
    promo_code: Optional[str] = None
    description: Optional[str] = None


class Promotion(PromotionBase):
    id: int

    class ConfigDict:
        from_attributes = True