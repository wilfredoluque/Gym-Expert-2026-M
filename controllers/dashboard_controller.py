from flask import Blueprint, render_template
from models.estadistica_model import Estadistica
from models.pago_model import Pago
from datetime import datetime

bp = Blueprint("dashboard", __name__)


@bp.route("/")
def index():

    total_clientes = Estadistica.total_clientes()
    total_membresias = Estadistica.total_membresias()
    total_asistencias = Estadistica.asistencias_hoy()

    total_ingresos = Pago.ingresos_totales()
    ingresos_por_mes = Pago.ingresos_por_mes()

    meses = [
        "Enero", "Febrero", "Marzo", "Abril",
        "Mayo", "Junio", "Julio", "Agosto",
        "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]

    mes_actual = datetime.now().month

    return render_template(
        "dashboard/index.html",
        total_clientes=total_clientes,
        total_membresias=total_membresias,
        total_asistencias=total_asistencias,
        total_ingresos=total_ingresos,
        ingresos_por_mes=ingresos_por_mes,
        meses=meses,
        mes_actual=mes_actual
    )