from app.extensions import db
from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from .model import Loja

class VerLoja(MethodView):             #/loja
    def get(self):                     #ver loja
        loja_todos=Loja.query.filter_by().all()
        return jsonify([loja.json() for loja in loja_todos]),200
    def patch(self):                   #editar loja
        nome=str(dados.get("nome",loja.nome))
        valor=dados.get("valor",loja.valor)
        descricao=dados.get("descricao",loja.descricao)
        estoque=str(dados.get("estoque",loja.estoque))
        id_dono=cliente.id

        if (nome is None) or (valor is None) or (descricao is None)or (estoque is None):
            return {"erro":"Há algum input vazio."},400

        if not isinstance(nome,str) or len(nome)>50:
            return {"erro":"Nome inválido."},400
        if not isinstance(valor,float):
            return {"erro":"Valor inválido."},400
        if not isinstance(descricao,str) or len(descricao)>300:
            return {"erro":"Descricao inválida."},400
        if not isinstance(estoque,int):
            return {"erro":"Estoque inválido."},400

        horario=Horario(nome=nome,
                        valor=valor,
                        descricao=descricao,
                        estoque=estoquea)
                        
        db.session.commit()