from core.database import db
from datetime import datetime

class Asistencia(db.Model):
    __tablename__ = "asistencias"

    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey("clientes.id"))
    fecha = db.Column(db.DateTime, default=datetime.now)
    hora_entrada = db.Column(db.DateTime, default=datetime.now)
    hora_salida = db.Column(db.DateTime)

    cliente = db.relationship("Cliente")

    def __init__(self, cliente_id):
        self.cliente_id = cliente_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Asistencia.query.all()

    @staticmethod
    def get_by_id(id):
        return Asistencia.query.get(id)

    def cerrar(self):
        self.hora_salida = datetime.now()
        db.session.commit()
