from flask import Blueprint
from .controllers import (VerLoja,AdicionarCarrinho)

loja_api=Blueprint("horario_api", __name__)

loja_api.add_url_rule(
    "/loja",view_func=VerLoja.as_view("ver_loja"),methods=["GET","PATCH"])