"""
from flask import Blueprint
from .controllers import (VerHorario)

horario_api=Blueprint("horario_api", __name__)

horario_api.add_url_rule(
    "/horarios",view_func=VerHorario.as_view("ver_horarios"),methods=["GET"])
"""