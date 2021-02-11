from flask import Blueprint
from .controllers import (ClientesJoin,ClientesLogin) #,ClientesMenu,ClientesPets

clientes_api=Blueprint("clientes_api", __name__)

clientes_api.add_url_rule(
    "/join",view_func=ClientesJoin.as_view("clientes_join"),methods=["POST"])

clientes_api.add_url_rule(
    "/login",view_func=ClientesLogin.as_view("clientes_login"),methods=["POST"])


clientes_api.add_url_rule(
    "/cliente/<int:id>",view_func=ClientesMenu.as_view("clientes_menu"),methods=["GET","PATCH","DELETE"])

#clientes_api.add_url_rule(
#    "/cliente/<int:id>/pets",view_func=ClientesPets.as_view("clientes_pets"),methods=["GET","POST","PATCH","DELETE"])