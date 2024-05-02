from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .menu import Menu


class DishBase(BaseModel):
    dish_name: str
    price: float
    calories: int


class DishCreate(DishBase):
    menu_category_id: int

# Not optional because these things cannont be null
class DishUpdate(BaseModel):
    dish_name: Optional[str] = None
    price: Optional[float] = None
    calories: Optional[int] = None
    menu_category_id: Optional[int] = None


class Dish(DishBase):
    id: int
    menu: Menu = None

    class ConfigDict:
        from_attribute = True