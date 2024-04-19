from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class MenuBase(BaseModel):
    category:str

class MenuCreate(MenuBase):
    pass

# Not optional because these things cannont be null
class MenuUpdate(BaseModel):
    category:str

class Menu(MenuBase):
    id: int

    class ConfigDict:
        from_attribute = True