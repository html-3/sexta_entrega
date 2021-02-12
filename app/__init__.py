from flask import Flask
from .config import Config
from .extensions import db,migrate,mail,jwt

from app.clientes.routes import clientes_api
from app.pets.routes import pets_api
from app.horarios.routes import horario_api

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app,db)
    mail.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(clientes_api)
    app.register_blueprint(pets_api)
    app.register_blueprint(horario_api)


    return app