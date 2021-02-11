from app.extensions import db

#modelo Cliente OK

class Cliente(db.Model):
    __tablename__="clientes"
    id=db.Column(db.Integer,primary_key=True)

    nome=db.Column(db.String(50),nullable=False)
    endereco=db.Column(db.String(100),nullable=False)
    telefone=db.Column(db.String(20),nullable=False)
    email=db.Column(db.String(100),nullable=False,unique=True)

    senha_hash=db.Column(db.String(200),nullable=False)

    #pets=db.relationship("Pet")

    #endereco_pet=db.Relationship("Pet",backref="cliente")
    #telefone_pet=db.Relationship("Pet",backref="cliente")
    #email_pet=db.Relationship("Pet",backref="cliente")
    #carrinho=db.Relationship("loja",secondary=carrinhos,backref="cliente")

    def json(self):
        return{
            "nome": self.nome,
            "endereco": self.endereco,
            "telefone": self.telefone,
            "email": self.email}