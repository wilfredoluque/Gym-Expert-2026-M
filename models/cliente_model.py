from core.database import db
from datetime import datetime

class Cliente(db.Model):
    __tablename__ = "clientes"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120))
    apellido = db.Column(db.String(120))
    telefono = db.Column(db.String(50))
    ci = db.Column(db.String(50))
    fecha_nacimiento = db.Column(db.String(50))
    sexo = db.Column(db.String(20))
    direccion = db.Column(db.String(200))
    fecha_registro = db.Column(db.DateTime, default=datetime.now)
    estado = db.Column(db.String(20), default="activo")

    def __init__(self, nombre, apellido, telefono, ci):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.ci = ci

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Cliente.query.all()

    @staticmethod
    def get_by_id(id):
        return Cliente.query.get(id)

    def update(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
