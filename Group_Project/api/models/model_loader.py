from . import account, customerInfo, dishes, menu, rating, orders, order_details

from ..dependencies.database import engine


def index():

    customerInfo.Base.metadata.create_all(engine)
    account.Base.metadata.create_all(engine)
    dishes.Base.metadata.create_all(engine)
    menu.Base.metadata.create_all(engine)
    rating.Base.metadata.create_all(engine)
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)