from . import dishes, customers


def load_routes(app):

    app.include_router(dishes.router)
    app.include_router(customers.router)
