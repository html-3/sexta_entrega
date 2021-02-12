from app.extensions import db

#modelo Horar OK

class Horario(db.Model):
    __tablename__="horario"
    id_horario=db.Column(db.Integer,primary_key=True)
    
    #id_dono=db.Column(db.String(50),ForeignKey("Pet.id_dono"))
    #nome_pet=db.Column(db.String(50),ForeignKey("Pet.nome"))
    dia_hora=db.Column(db.String(11),nullable=False,unique=True)
    banho=db.Column(db.Boolean,nullable=False)
    tosa=db.Column(db.Boolean,nullable=False)

    def json(self):
        return{
            "id_dono": self.id_dono,
            "nome_pet": self.nome_pet,
            "dia_hora": self.dia_hora,
            "banho": self.banho,
            "tosa": self.tosa}