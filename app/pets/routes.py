from flask import Blueprint
from .controllers import (ClientesPets)

pets_api=Blueprint("clientes_api", __name__)

pets_api.add_url_rule(
    "/<int:id>/pets",view_func=ClientesPets.as_view("clientes_pets"),methods=["GET","PATCH","POST","DELETE"])

