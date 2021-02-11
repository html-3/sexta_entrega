from app.extensions import db,mail
from app.horario.model import Horario
from app.pets.model import Pet

class VerHorario(MethodView):
    def get(self):
        horarios_todos=Horario.query.filter_by().all()
        return jsonify([horario.json() for horario in horario_todos]),200
    
    