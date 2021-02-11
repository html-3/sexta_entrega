from flask import Flask
from .config import Config
from .extensions import db,migrate,mail

from app.clientes.routes import clientes_api

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app,db)
    mail.init_app(app)

    app.register_blueprint(clientes_api)

    return app