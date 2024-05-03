from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .dishes import Dish

class RatingBase(BaseModel):
    score: float
    review: str

class RatingCreate(RatingBase):
    dishID: Optional[int] = None

class RatingUpdate(BaseModel):
    score: Optional[float] = None
    review: Optional[str] = None

class Rating(RatingBase):
    id: int
    dish: Dish = None

    class ConfigDict:
        from_attribute = None

