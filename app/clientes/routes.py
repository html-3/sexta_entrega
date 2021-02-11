from flask import Blueprint
from .controllers import (ClientesDetalhes) #,ClientesMenu,ClientesPets

clientes_api=Blueprint("clientes_api", __name__)

clientes_api.add_url_rule(
    "/clientes",view_func=ClientesDetalhes.as_view("clientes_detalhes"),methods=["GET","POST"])
"""
clientes_api.add_url_rule(
    "/clientes/<int:id>",view_func=ClientesMenu.as_view("clientes_menu"),methods=["GET","PATCH","DELETE"]
)
clientes_api.add_url_rule(
    "/clientes/<int:id>/pets",view_func=ClientesPets.as_view("clientes_pets"),methods=["GET","POST","PATCH","DELETE"]
)"""