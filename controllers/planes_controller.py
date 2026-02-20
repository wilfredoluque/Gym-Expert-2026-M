from flask import Blueprint, render_template, request, redirect, url_for
from config.security import requiere_admin
from models.plan_model import Plan
import calendar
from datetime import datetime

bp = Blueprint("planes", __name__, url_prefix="/planes")


@bp.route("/")
@requiere_admin
def index():
    data = Plan.get_all()
    return render_template("planes/index.html", data=data)


@bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":

        tipo_plan = request.form["tipo_plan"]

        duracion_dias = None
        duracion_horas = None

        if tipo_plan == "mensual":
            now = datetime.now()
            duracion_dias = calendar.monthrange(now.year, now.month)[1]

        elif tipo_plan == "trimestral":
            duracion_dias = 90

        elif tipo_plan == "semestral":
            duracion_dias = 180

        elif tipo_plan == "anual":
            duracion_dias = 365

        elif tipo_plan == "sesion":
            duracion_horas = int(request.form["duracion_horas"])

        plan = Plan(
            nombre=request.form["nombre"],
            precio=float(request.form["precio"]),
            tipo_plan=tipo_plan,
            duracion_dias=duracion_dias,
            duracion_horas=duracion_horas
        )

        plan.save()
        return redirect(url_for("planes.index"))

    return render_template("planes/create.html")


@bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    plan = Plan.get_by_id(id)

    if request.method == "POST":

        tipo_plan = request.form["tipo_plan"]

        duracion_dias = None
        duracion_horas = None

        if tipo_plan == "mensual":
            now = datetime.now()
            duracion_dias = calendar.monthrange(now.year, now.month)[1]

        elif tipo_plan == "trimestral":
            duracion_dias = 90

        elif tipo_plan == "semestral":
            duracion_dias = 180

        elif tipo_plan == "anual":
            duracion_dias = 365

        elif tipo_plan == "sesion":
            duracion_horas = int(request.form["duracion_horas"])

        plan.update(
            nombre=request.form["nombre"],
            precio=float(request.form["precio"]),
            tipo_plan=tipo_plan,
            duracion_dias=duracion_dias,
            duracion_horas=duracion_horas
        )

        return redirect(url_for("planes.index"))

    return render_template("planes/edit.html", item=plan)


@bp.route("/delete/<int:id>")
def delete(id):
    plan = Plan.get_by_id(id)
    plan.delete()
    return redirect(url_for("planes.index"))