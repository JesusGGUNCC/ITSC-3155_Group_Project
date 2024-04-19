from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .menu import Menu


class DishBase(BaseModel):
    dish_name: str
    price: float
    calories: int
    menu_category_id: int

class DishCreate(DishBase):
    pass

# Not optional because these things cannont be null
class DishUpdate(BaseModel):
    dish_name: str
    price: float
    calories: int
    menu_category_id: int


class Dish(DishBase):
    id: int
    Menu: Menu = None

    class ConfigDict:
        from_attribute = True