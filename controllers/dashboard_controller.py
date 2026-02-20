from flask import Blueprint, render_template
from models.estadistica_model import Estadistica

bp = Blueprint("dashboard", __name__)


@bp.route("/")
def index():
    total_clientes = Estadistica.total_clientes()
    ingresos = Estadistica.ingresos_mes()
    asistencias = Estadistica.asistencias_hoy()

    return render_template(
        "dashboard/index.html",
        total_clientes=total_clientes,
        ingresos=ingresos,
        asistencias=asistencias
    )
