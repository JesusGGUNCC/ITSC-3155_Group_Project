from . import dishes, customers, accounts


def load_routes(app):

    app.include_router(dishes.router)
    app.include_router(customers.router)
    app.include_router(accounts.router)