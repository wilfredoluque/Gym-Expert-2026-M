from flask import Blueprint, render_template, request, redirect, url_for
from models.rutina_model import Rutina
from models.rutina_detalle_model import RutinaDetalle
from models.cliente_model import Cliente
from models.entrenador_model import Entrenador
from models.ejercicio_model import Ejercicio

bp = Blueprint("rutinas", __name__, url_prefix="/rutinas")


@bp.route("/")
def index():
    data = Rutina.get_all()
    return render_template("rutinas/index.html", data=data)


@bp.route("/create", methods=["GET", "POST"])
def create():
    clientes = Cliente.get_all()
    entrenadores = Entrenador.get_all()

    if request.method == "POST":
        r = Rutina(
            request.form["cliente_id"],
            request.form["entrenador_id"],
            request.form["nombre"]
        )
        r.save()
        return redirect(url_for("rutinas.index"))

    return render_template(
        "rutinas/create.html",
        clientes=clientes,
        entrenadores=entrenadores
    )


@bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    rutina = Rutina.get_by_id(id)
    clientes = Cliente.get_all()
    entrenadores = Entrenador.get_all()

    if request.method == "POST":
        rutina.nombre = request.form["nombre"]
        rutina.cliente_id = request.form["cliente_id"]
        rutina.entrenador_id = request.form["entrenador_id"]
        rutina.save()
        return redirect(url_for("rutinas.index"))

    return render_template(
        "rutinas/edit.html",
        item=rutina,
        clientes=clientes,
        entrenadores=entrenadores
    )


@bp.route("/<int:rutina_id>")
def detalle(rutina_id):
    rutina = Rutina.get_by_id(rutina_id)
    ejercicios = Ejercicio.get_all()
    detalles = RutinaDetalle.query.filter_by(rutina_id=rutina_id).all()

    return render_template(
        "rutinas/detalle.html",
        rutina=rutina,
        ejercicios=ejercicios,
        detalles=detalles
    )


@bp.route("/agregar_ejercicio", methods=["POST"])
def agregar_ejercicio():
    d = RutinaDetalle(
        request.form["rutina_id"],
        request.form["ejercicio_id"],
        request.form["series"],
        request.form["repeticiones"],
        request.form["peso"]
    )
    d.save()
    return redirect(url_for("rutinas.detalle", rutina_id=request.form["rutina_id"]))


@bp.route("/delete/<int:id>")
def delete(id):
    r = Rutina.get_by_id(id)
    r.delete()
    return redirect(url_for("rutinas.index"))
