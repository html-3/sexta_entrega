from app.extensions import db
from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from .model import Horario
from app.pets.model import Pet
from app.clientes.model import Cliente

class VerHorario(MethodView):          #/horarios
    def get(self):                     #ver horarios
        horarios_todos=Horario.query.filter_by().all()
        return jsonify([horario.json() for horario in horario_todos]),200

class MarcarHorario(MethodView):       #/horarios/<int:id>/marcar
    decorators=[jwt_required]
    cliente=Cliente.query.get_or_404(id)
    pets=Pet.query.filter_by(id_dono=id)
    def get(self,id):                  #ver horarios marcados
        if get_jwt_identiry!=id:
            return {"erro":"Cliente incorreto."},400
        horarios_todos=Horario.query.filter_by(id_dono=id).all()
        return jsonify([horario.json() for horario in horario_todos]),200
    def post(self,id):                 #marcar horario
        if get_jwt_identiry!=id:
            return {"erro":"Cliente incorreto."},400
        dia_hora=str(dados.get("dia_hora"))
        banho=dados.get("banho")
        tosa=dados.get("tosa")
        nome_pet=str(dados.get("nome_pet"))
        id_dono=cliente.id

        if (dia_hora is None) or (banho is None) or (tosa is None)or (nome_pet is None):
            return {"erro":"Há algum input vazio."},400
                                               #dia DD-MM | hora HH:00
        dia_hora_split=dia_hora.split()
        horas_disponivel=("10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00")
        if not isinstance(dia_hora,str) or 
           len(dia_hora)>11 or 
           "/" in dia_hora or 
           horas_disponivel.count(dia_hora_split[1])!=1 or
           dia_hora==Pet.query.filter_by(dia_hora=dia_hora): 
            return {"erro":"Dia ou hora inválidos."},400

        if not isinstance(banho,bool) or not isinstance(tosa,bool) or (banho=False and tosa=False):
            return {"erro":"Servicos inválidos."},400

        horario=Horario(id_dono=id_dono,
                        nome_pet=nome_pet,
                        dia_hora=dia_hora,
                        banho=banho,
                        tosa=tosa)

        db.session.add(horario)
        db.session.commit()
    def patch(self,id):                #editar horario
        if get_jwt_identiry!=id:
            return {"erro":"Cliente incorreto."},400
        dia_hora=str(dados.get("dia_hora",horario.dia_hora))
        banho=dados.get("banho",horario.banho)
        tosa=dados.get("tosa",horario.tosa)
        nome_pet=str(dados.get("nome_pet",horario.nome_pet))
        id_dono=cliente.id

        if (dia_hora is None) or (banho is None) or (tosa is None)or (nome_pet is None):
            return {"erro":"Há algum input vazio."},400
                                               #dia DD-MM | hora HH:00
        dia_hora_split=dia_hora.split()
        horas_disponivel=("10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00")
        if not isinstance(dia_hora,str) or 
           len(dia_hora)>11 or 
           "/" in dia_hora or 
           horas_disponivel.count(dia_hora_split[1])!=1 or
           dia_hora==Pet.query.filter_by(dia_hora=dia_hora): 
            return {"erro":"Dia ou hora inválidos."},400

        if not isinstance(banho,bool) or not isinstance(tosa,bool) or (banho=False and tosa=False):
            return {"erro":"Servicos inválidos."},400

        horario=Horario(id_dono=id_dono,
                        nome_pet=nome_pet,
                        dia_hora=dia_hora,
                        banho=banho,
                        tosa=tosa)
                        
        db.session.commit()
    def delete(self,id):               #desmarcar horarios [todos]
         if get_jwt_identiry!=id:
            return {"erro":"Cliente incorreto."},400
        
        Horario.query.filter_by(id_dono=id).delete()
        db.session.commit()