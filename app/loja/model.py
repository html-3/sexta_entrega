from app.extensions import db

#modelo Loja OK, SEM NEXO

class Loja(db.Model):
    __tablename__="produtos"
    id=db.Column(db.Integer,primary_key=True)

    nome=db.Column(db.String(50),nullable=False)
    valor=db.Column(db.Float,nullable=False)
    descricao=db.Column(db.String(300),nullable=False)
    estoque=db.Column(db.Integer,nullable=False)

    #carrinho=db.Relationship("loja",secondary=carrinhos,backref="cliente")

    def json(self):
        return{
            "nome": self.nome,
            "valor": self.valor,
            "descricao": self.descricao,
            "estoque": self.estoque}
