from core.database import db
from sqlalchemy import func
from models.pago_model import Pago
from models.asistencia_model import Asistencia
from models.cliente_model import Cliente


class Estadistica:

    @staticmethod
    def total_clientes():
        return db.session.query(func.count(Cliente.id)).scalar()

    @staticmethod
    def ingresos_mes():
        return db.session.query(func.sum(Pago.monto)).scalar() or 0

    @staticmethod
    def asistencias_hoy():
        return db.session.query(func.count(Asistencia.id)).scalar()
