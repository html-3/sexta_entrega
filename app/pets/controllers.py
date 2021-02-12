import bcrypt
from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from .model import Pet
from app.clientes.model import Cliente

class ClientesPets(MethodView):         #/pets
    decorators=[jwt_required]
    cliente=Cliente.query.get_or_404(id)
    def get(self,id):                   #ver pets
        if get_jwt_identiry!=id:
            return {"erro":"Cliente incorreto."},400
        pets_todos=Pet.query.filter_by(id_dono=id).all()
        return jsonify([pet.json() for pet in pets_todos]),200
    def patch(self,id):                 #editar pets
        if get_jwt_identiry!=id:
            return {"erro":"Cliente incorreto."},400
        dados=request.json

        nome=dados.get("nome", pet.nome)
        descricao=dados.get("descricao", pet.descricao)
    
        if (nome is None) or (descricao is None):
            return {"erro":"Há algum input vazio."},400

        if not isinstance(nome,str) or len(nome)>50:
            return {"erro":"Nome inválido."},400
        if not isinstance(descricao,str) or len(descricao)>300:
            return {"erro":"Descricao inválida."},400

        pet=Pet(nome=nome,
                descricao=descricao,
                id_dono=cliente.id)

        db.session.commit()
    def post(self,id):                  #criar pet 
        dados=request.json

        nome=dados.get("nome")
        descricao=dados.get("descricao")
    
        if (nome is None) or (descricao is None):
            return {"erro":"Há algum input vazio."},400

        if not isinstance(nome,str) or len(nome)>50:
            return {"erro":"Nome inválido."},400
        if not isinstance(descricao,str) or len(descricao)>300:
            return {"erro":"Descricao inválida."},400

        pet=Pet(nome=nome,
                descricao=descricao,
                id_dono=cliente.id)

        db.session.add(pet)
        db.session.commit()
        return cliente.json(), 200
    def delete(self,id):                #deletar pet  [deleta todos os pets]
        if get_jwt_identiry!=id:
            return {"erro":"Cliente incorreto."},400
        
        Pets.query.filter_by(id_dono=id).all().delete()
        db.session.commit()