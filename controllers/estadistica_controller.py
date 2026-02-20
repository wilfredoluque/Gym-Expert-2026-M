from flask import Blueprint, render_template
from config.security import requiere_admin
from sqlalchemy import func
from core.database import db

from models.cliente_model import Cliente
from models.pago_model import Pago
from models.asistencia_model import Asistencia

bp = Blueprint("estadistica", __name__, url_prefix="/estadisticas")

@bp.route("/")
@requiere_admin
def index():
    total_clientes = db.session.query(func.count(Cliente.id)).scalar()
    total_ingresos = db.session.query(func.sum(Pago.monto)).scalar() or 0
    total_asistencias = db.session.query(func.count(Asistencia.id)).scalar()

    return render_template(
        "estadisticas/index.html",
        total_clientes=total_clientes,
        total_ingresos=total_ingresos,
        total_asistencias=total_asistencias
    )
