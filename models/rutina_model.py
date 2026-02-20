from core.database import db
from datetime import datetime

class Rutina(db.Model):
    __tablename__ = "rutinas"

    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey("clientes.id"))
    entrenador_id = db.Column(db.Integer, db.ForeignKey("entrenadores.id"))
    nombre = db.Column(db.String(120))
    fecha_inicio = db.Column(db.DateTime, default=datetime.now)

    cliente = db.relationship("Cliente")
    entrenador = db.relationship("Entrenador")

    def __init__(self, cliente_id, entrenador_id, nombre):
        self.cliente_id = cliente_id
        self.entrenador_id = entrenador_id
        self.nombre = nombre

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Rutina.query.all()

    @staticmethod
    def get_by_id(id):
        return Rutina.query.get(id)

    def delete(self):
        db.session.delete(self)
        db.session.commit()
