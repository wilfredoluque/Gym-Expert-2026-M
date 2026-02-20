from flask import Blueprint, render_template, request, redirect, url_for
from models.entrenador_model import Entrenador

bp = Blueprint("entrenadores", __name__, url_prefix="/entrenadores")


@bp.route("/")
def index():
    data = Entrenador.get_all()
    return render_template("entrenadores/index.html", data=data)


@bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        e = Entrenador(
            request.form["nombre"],
            request.form["telefono"],
            request.form["especialidad"]
        )
        e.save()
        return redirect(url_for("entrenadores.index"))

    return render_template("entrenadores/create.html")


@bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    e = Entrenador.get_by_id(id)

    if request.method == "POST":
        e.update(
            nombre=request.form["nombre"],
            telefono=request.form["telefono"],
            especialidad=request.form["especialidad"]
        )
        return redirect(url_for("entrenadores.index"))

    return render_template("entrenadores/edit.html", item=e)


@bp.route("/delete/<int:id>")
def delete(id):
    e = Entrenador.get_by_id(id)
    e.delete()
    return redirect(url_for("entrenadores.index"))
