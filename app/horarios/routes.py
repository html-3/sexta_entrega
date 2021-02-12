from flask import Blueprint
from .controllers import (VerHorario,MarcarHorario)

horario_api=Blueprint("horario_api", __name__)

horario_api.add_url_rule(
    "/horarios",view_func=VerHorario.as_view("ver_horarios"),methods=["GET"])

horario_api.add_url_rule(
    "/horarios/<int:id>/marcar",view_func=MarcarHorario.as_view("marcar_horarios"),methods=["GET","POST","PATCH","DELETE"])
