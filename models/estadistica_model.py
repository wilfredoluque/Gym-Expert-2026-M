from core.database import db
from sqlalchemy import func, extract
from datetime import datetime

from models.pago_model import Pago
from models.asistencia_model import Asistencia
from models.cliente_model import Cliente
from models.membresia_model import Membresia


class Estadistica:

    # ==============================
    # TOTAL CLIENTES
    # ==============================
    @staticmethod
    def total_clientes():
        return db.session.query(func.count(Cliente.id)).scalar() or 0

    # ==============================
    # TOTAL MEMBRESIAS
    # ==============================
    @staticmethod
    def total_membresias():
        return db.session.query(func.count(Membresia.id)).scalar() or 0

    # ==============================
    # INGRESOS TOTALES
    # ==============================
    @staticmethod
    def ingresos_total():
        return db.session.query(func.sum(Pago.monto)).scalar() or 0

    # ==============================
    # INGRESOS DEL MES ACTUAL
    # ==============================
    @staticmethod
    def ingresos_mes_actual():
        hoy = datetime.now()
        return (
            db.session.query(func.sum(Pago.monto))
            .filter(extract('month', Pago.fecha) == hoy.month)
            .filter(extract('year', Pago.fecha) == hoy.year)
            .scalar() or 0
        )

    # ==============================
    # ASISTENCIAS HOY
    # ==============================
    @staticmethod
    def asistencias_hoy():
        hoy = datetime.now().date()

        return (
            db.session.query(func.count(Asistencia.id))
            .filter(func.date(Asistencia.fecha) == hoy)
            .scalar() or 0
        )