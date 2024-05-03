from . import dishes, customers, accounts, menu, orders, ratings



def load_routes(app):

    app.include_router(dishes.router)
    app.include_router(menu.router)
    app.include_router(customers.router)
    app.include_router(accounts.router)
    app.include_router(orders.router)
    app.include_router(ratings.router)
