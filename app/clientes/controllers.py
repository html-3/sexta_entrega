import bcrypt
from flask import request, jsonify #render_template
from flask.views import MethodView
#from flask_mail import Message
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.extensions import db #mail
from .model import Cliente

class ClientesJoin(MethodView):         #/join
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

        #msg = Message(sender="henriquemarques@poli.ufrj.br",
        #    recipients=[email],
        #    subject="Conta Petshop criada!",
        #    html=render_template("email1.html")
        #    nome=nome,
        #    endereco=endereco,
        #    telefone=telefone,
        #    email=email,)
        
        #mail.send(msg)
        db.session.add(cliente)
        db.session.commit()

        return cliente.json(), 200

class ClientesLogin(MethodView):        #/login
    def post(self):                     #logar cliente
        dados=request.json

        senha=dados.get("senha")
        email=dados.get("email")

        cliente=Cliente.query.filter_by(email=email).first()

        if not cliente:
            return {"erro":"Email inválido."},400
        if not bcrypt.checkpw(senha.encode(),cliente.senha_hash):
            return {"erro":"Senha inválida."},400

        token=jwt.create_access_token(identity=cliente.id)

        return {"token":token,
                "email":email},200
    
class ClientesMenu(MethodView):         #/cliente/<int:id>
    decorators=[jwt_required]
    cliente=Cliente.query.get_or_404(id)
    def get(self,id):                   #ver cliente
        if get_jwt_identiry!=id:
            return {"erro":"Cliente incorreto."},400

        return cliente.json(),200    
    def patch(self,id):                 #editar cliente [nao muda senha]
        if get_jwt_identiry!=id:
            return {"erro":"Cliente incorreto."},400
        dados=request.json

        nome=dados.get("nome", cliente.nome)
        endereco=dados.get("endereco", cliente.endereco)
        telefone=dados.get("telefone", cliente.telefone)
        email=str(dados.get("email", cliente.email))
        
        senha_hash=cliente.senha_hash
        #senha=dados.get("senha")       #nao se pode mudar a senha nesse menu, causaria uma brecha na seguranca.

        if (nome is None) or (endereco is None) or (telefone is None) or (email is None):
            return {"erro":"Há algum input vazio."},400

        if not isinstance(nome,str) or len(nome)>20:
            return {"erro":"Nome inválido."},400
        if not isinstance(endereco,str) or len(endereco)>100:
            return {"erro":"Endereco inválido."},400
        if not isinstance(telefone,str) or len(telefone)>20:
            return {"erro":"Telefone inválido."},400
        if not isinstance(email,str) or len(email)>100:
            return {"erro":"Email inválido."},400

        cliente=Cliente(nome=nome,
                        endereco=endereco,
                        telefone=telefone,
                        email=email,
                        senha_hash=senha_hash)

        #msg = Message(sender="henriquemarques@poli.ufrj.br",
        #    recipients=[email],
        #    subject="Conta Petshop editada!",
        #    html=render_template("email2.html")
        #    nome=nome,
        #    endereco=endereco,
        #    telefone=telefone,
        #    email=email,)
        
        #mail.send(msg)
        db.session.commit()
    def delete(self,id):                #deletar cliente
        if get_jwt_identiry!=id:
            return {"erro":"Cliente incorreto."},400
        
        Cliente.query.filter_by(id=id).delete()
        db.session.commit()
    