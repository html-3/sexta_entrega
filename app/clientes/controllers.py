from flask import request, Blueprint, jsonify
from flask.views import MethodView
import bcrypt
from app.extensions import db
from app.clientes.model import Cliente



class ClientesDetalhes(MethodView):     #/clientes
    def get(self):                      #ver clientes
        clientes_todos=Cliente.query.all()
        return jsonify([cliente.json() for cliente in clientes_todos]),200
    def post(self):                     #criar cliente
        dados=request.json

        nome=dados.get("nome")
        endereco=dados.get("endereco")
        telefone=dados.get("telefone")
        email=str(dados.get("email"))
    
        senha=dados.get("senha")

        if (nome is None) or (endereco is None) or (telefone is None) or (email is None) or (senha is None):
            return {"erro":"Há algum input vazio."},400

        if not isinstance(nome,str) or len(nome)>20:
            return {"erro":"Nome inválido."},400
        if not isinstance(endereco,str) or len(endereco)>100:
            return {"erro":"Endereco inválido."},400
        if not isinstance(telefone,str) or len(telefone)>20:
            return {"erro":"Telefone inválido."},400
        if not isinstance(email,str) or len(email)>100:
            return {"erro":"Email inválido."},400
        if not isinstance(senha,str) or len(senha)>20:
            return {"erro":"Senha inválida."},400

        senha_hash=bcrypt.hashpw(senha.encode(),bcrypt.gensalt())

        cliente=Cliente(nome=nome,
                        endereco=endereco,
                        telefone=telefone,
                        email=email,
                        senha_hash=senha_hash)

        db.session.add(cliente)
        db.session.commit()

        return cliente.json(), 200
"""     
class ClientesMenu(MethodView):         #/clientes/<int:id>
    cliente=Cliente.query.get_or_404(id)
        
    def patch(self,id):                 #editar cliente  [INCOMPLETO]
        
    def delete(self,id):                #deletar cliente  [INCOMPLETO]

class ClientesPets(MethodView):         #/clientes/<int:id>/pets   [INCOMPLETO]

    def get(self,id):                   #ver pets [ENCONTRAR FUNCAO SORT PARA FUNCIONAR]
        pets_todos=Pet.query.all()
        return jsonify([pet.json() for pet in pets_todos]),200
    def post(self,id):                  #criar pet  [INCOMPLETO]
    
    def delete(self,id):                #deletar pet  [INCOMPLETO]
"""