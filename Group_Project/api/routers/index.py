<<<<<<< HEAD
from . import dishes, customers, accounts, menu, orders, promotions
=======
from . import dishes, customers, accounts, menu, orders, order_details
>>>>>>> 428cbce5e64e5da05909c9aa37606521da09f9cf



def load_routes(app):

    app.include_router(dishes.router)
    app.include_router(menu.router)
    app.include_router(customers.router)
    app.include_router(accounts.router)
    app.include_router(orders.router)
<<<<<<< HEAD
    app.include_router(promotions.router)
=======
    app.include_router(order_details.router)
>>>>>>> 428cbce5e64e5da05909c9aa37606521da09f9cf
