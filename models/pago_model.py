from core.database import db
from datetime import datetime
from sqlalchemy import extract, func


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
        return Pago.query.order_by(Pago.fecha.desc()).all()

    @staticmethod
    def get_by_id(id):
        return Pago.query.get(id)

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # ==========================================
    # MÉTODOS PRO PARA DASHBOARD
    # ==========================================

    @staticmethod
    def ingresos_totales():
        total = db.session.query(func.sum(Pago.monto)).scalar()
        return float(total or 0)

    @staticmethod
    def ingresos_por_mes(anio=None):

        if not anio:
            anio = datetime.now().year

        resultados = (
            db.session.query(
                extract('month', Pago.fecha).label('mes'),
                func.sum(Pago.monto).label('total')
            )
            .filter(extract('year', Pago.fecha) == anio)
            .group_by('mes')
            .all()
        )

        ingresos = [0] * 12

        for mes, total in resultados:
            ingresos[int(mes) - 1] = float(total)

        return ingresos