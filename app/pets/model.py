from app.extensions import db

#modelo Pet OK

class Pet(db.Model):
    __tablename__="pets"
    id=db.Column(db.Integer,primary_key=True)

    nome=db.Column(db.String(50),nullable=False)
    descricao=db.Column(db.String(300),nullable=False)

    #id_dono=db.Column(db.Integer,ForeignKey("Cliente.id"))
    #horarios=db.relationship("Horario")

    def json(self):
        return{
            "nome": self.nome,
            "descricao": self.descricao,
            "id_dono": self.id_dono}



