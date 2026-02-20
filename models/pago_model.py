from core.database import db
from datetime import datetime

class Pago(db.Model):
    __tablename__ = "pagos"

    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey("clientes.id"))
    membresia_id = db.Column(db.Integer, db.ForeignKey("membresias.id"))
    fecha = db.Column(db.DateTime, default=datetime.now)
    monto = db.Column(db.Float)
    metodo = db.Column(db.String(50))
    descripcion = db.Column(db.String(200))

    cliente = db.relationship("Cliente")
    membresia = db.relationship("Membresia")

    def __init__(self, cliente_id, membresia_id, monto, metodo):
        self.cliente_id = cliente_id
        self.membresia_id = membresia_id
        self.monto = monto
        self.metodo = metodo

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Pago.query.all()

    @staticmethod
    def get_by_id(id):
        return Pago.query.get(id)

    def delete(self):
        db.session.delete(self)
        db.session.commit()
