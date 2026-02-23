from core.database import db
from datetime import datetime, timedelta


class Membresia(db.Model):
    __tablename__ = "membresias"

    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey("clientes.id"))
    plan_id = db.Column(db.Integer, db.ForeignKey("planes.id"))
    fecha_inicio = db.Column(db.DateTime)
    fecha_fin = db.Column(db.DateTime)

    cliente = db.relationship("Cliente")
    plan = db.relationship("Plan")

    def __init__(self, cliente_id, plan):
        self.cliente_id = cliente_id
        self.plan_id = plan.id
        self.fecha_inicio = datetime.now()

        if plan.tipo_plan == "sesion":
            horas = plan.duracion_horas if plan.duracion_horas else 0
            self.fecha_fin = self.fecha_inicio + timedelta(hours=horas)
        else:
            dias = plan.duracion_dias if plan.duracion_dias else 0
            self.fecha_fin = self.fecha_inicio + timedelta(days=dias)

    # 🔥 ESTADO DINÁMICO
    @property
    def estado_actual(self):
        ahora = datetime.now()
        if self.fecha_fin < ahora:
            return "vencida"
        return "activa"

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Membresia.query.all()

    @staticmethod
    def get_by_id(id):
        return Membresia.query.get(id)

    def delete(self):
        db.session.delete(self)
        db.session.commit()