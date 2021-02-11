from app.extensions import db

#modelo Pet OK

class Pet(db.Model):
    __tablename__="pets"
    id=db.Column(db.Integer,primary_key=True)

    nome=db.Column(db.String(50),nullable=False)
    descricao=db.Column(db.String(300),nullable=False)
    dia_hora=db.Column(db.String(11),nullable=False,unique=True)
    banho=db.Column(db.Boolean,nullable=False)
    tosa=db.Column(db.Boolean,nullable=False)
    
    id_dono=db.Column(db.Integer,nullable=False)

    def json(self):
        return{
            "nome": self.nome,
            "descricao": self.descricao,
            "dia_hora": self.dia_hora,
            "banho": self.banho,
            "tosa": self.tosa,
            "id_dono": self.id_dono}



