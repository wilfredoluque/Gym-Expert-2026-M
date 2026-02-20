from flask import Blueprint, render_template, request, redirect, url_for
from models.cliente_model import Cliente

bp = Blueprint("clientes", __name__, url_prefix="/clientes")


@bp.route("/")
def index():
    data = Cliente.get_all()
    return render_template("clientes/index.html", data=data)


@bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        cliente = Cliente(
            request.form["nombre"],
            request.form["apellido"],
            request.form["telefono"],
            request.form["ci"]
        )
        cliente.save()
        return redirect(url_for("clientes.index"))

    return render_template("clientes/create.html")


@bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    cliente = Cliente.get_by_id(id)

    if request.method == "POST":
        cliente.update(
            nombre=request.form["nombre"],
            apellido=request.form["apellido"],
            telefono=request.form["telefono"],
            ci=request.form["ci"]
        )
        return redirect(url_for("clientes.index"))

    return render_template("clientes/edit.html", item=cliente)


@bp.route("/delete/<int:id>")
def delete(id):
    cliente = Cliente.get_by_id(id)
    cliente.delete()
    return redirect(url_for("clientes.index"))
