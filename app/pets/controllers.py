import bcrypt
from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from .model import Pet

class ClientesPets(MethodView):         #/clientes/<int:id>/pets   [INCOMPLETO]
    decorators=[jwt_required]
    cliente=Cliente.query.get_or_404(id)
    def get(self,id):                   #ver pets [acho que funciona]
        if get_jwt_identiry!=id:
            return {"erro":"Cliente incorreto."},400
        pets_todos=Pet.query.filter_by(id_dono=id).all()
        return jsonify([pet.json() for pet in pets_todos]),200
    def patch(self,id):                 #editar cliente [nao muda senha]
        if get_jwt_identiry!=id:
            return {"erro":"Cliente incorreto."},400
        dados=request.json

        nome=dados.get("nome", pet.nome)
        descricao=dados.get("descricao", pet.descricao)
        dia_hora=str(dados.get("dia_hora", pet.dia_hora))
        banho=dados.get("banho", pet.banho)
    
        if (nome is None) or (descricao is None) or (dia_hora is None) or (banho is None) or (tosa is None):
            return {"erro":"Há algum input vazio."},400

        if not isinstance(nome,str) or len(nome)>50:
            return {"erro":"Nome inválido."},400
        if not isinstance(descricao,str) or len(descricao)>300:
            return {"erro":"Descricao inválida."},400

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

        pet=Pet(nome=nome,
                descricao=descricao,
                dia_hora=dia_hora,
                banho=banho,
                tosa=tosa,
                id_dono=cliente.id)

        db.session.commit()
    def post(self,id):                  #criar pet 
        dados=request.json

        nome=dados.get("nome")
        descricao=dados.get("descricao")
        dia_hora=str(dados.get("dia_hora"))
        banho=dados.get("banho")
        tosa=dados.get("tosa")
    
        if (nome is None) or (descricao is None) or (dia_hora is None) or (banho is None) or (tosa is None):
            return {"erro":"Há algum input vazio."},400

        if not isinstance(nome,str) or len(nome)>50:
            return {"erro":"Nome inválido."},400
        if not isinstance(descricao,str) or len(descricao)>300:
            return {"erro":"Descricao inválida."},400

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

        pet=Pet(nome=nome,
                descricao=descricao,
                dia_hora=dia_hora,
                banho=banho,
                tosa=tosa,
                id_dono=cliente.id)

        db.session.add(pet)
        db.session.commit()
        return cliente.json(), 200
    def delete(self,id):                #deletar pet  [INCOMPLETO]
        if get_jwt_identiry!=id:
            return {"erro":"Cliente incorreto."},400
        
        Cliente.query.filter_by(id=id).delete()
        db.session.commit()