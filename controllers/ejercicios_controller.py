from flask import Blueprint, render_template, request, redirect, url_for
from models.ejercicio_model import Ejercicio

bp = Blueprint("ejercicios", __name__, url_prefix="/ejercicios")


@bp.route("/")
def index():
    data = Ejercicio.get_all()
    return render_template("ejercicios/index.html", data=data)


@bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        e = Ejercicio(
            request.form["nombre"],
            request.form["grupo_muscular"]
        )
        e.save()
        return redirect(url_for("ejercicios.index"))

    return render_template("ejercicios/create.html")


@bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    e = Ejercicio.get_by_id(id)

    if request.method == "POST":
        e.nombre = request.form["nombre"]
        e.grupo_muscular = request.form["grupo_muscular"]
        e.save()
        return redirect(url_for("ejercicios.index"))

    return render_template("ejercicios/edit.html", item=e)


@bp.route("/delete/<int:id>")
def delete(id):
    e = Ejercicio.get_by_id(id)
    e.delete()
    return redirect(url_for("ejercicios.index"))
