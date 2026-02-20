from flask import Blueprint, render_template, request, redirect, url_for
from models.asistencia_model import Asistencia
from models.cliente_model import Cliente

bp = Blueprint("asistencias", __name__, url_prefix="/asistencias")


@bp.route("/")
def index():
    asistencias = Asistencia.get_all()
    return render_template("asistencias/index.html", data=asistencias)


# CREAR
@bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        cliente_id = request.form["cliente_id"]
        a = Asistencia(cliente_id)
        a.save()
        return redirect(url_for("asistencias.index"))

    clientes = Cliente.get_all()
    return render_template("asistencias/create.html", clientes=clientes)


# EDITAR
@bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    item = Asistencia.get_by_id(id)

    if request.method == "POST":
        item.cliente_id = request.form["cliente_id"]
        from core.database import db
        db.session.commit()
        return redirect(url_for("asistencias.index"))

    clientes = Cliente.get_all()
    return render_template("asistencias/edit.html", item=item, clientes=clientes)


# ELIMINAR
@bp.route("/delete/<int:id>")
def delete(id):
    from core.database import db
    item = Asistencia.get_by_id(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for("asistencias.index"))


# SALIDA
@bp.route("/salida/<int:id>")
def salida(id):
    a = Asistencia.get_by_id(id)
    a.cerrar()
    return redirect(url_for("asistencias.index"))
