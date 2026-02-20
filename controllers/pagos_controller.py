from flask import Blueprint, render_template, request, redirect, url_for
from models.pago_model import Pago
from models.membresia_model import Membresia
from models.cliente_model import Cliente
from config.security import requiere_admin

bp = Blueprint("pagos", __name__, url_prefix="/pagos")


@bp.route("/")
@requiere_admin
def index():
    data = Pago.get_all()
    return render_template("pagos/index.html", data=data)


@bp.route("/create", methods=["GET", "POST"])
def create():
    clientes = Cliente.get_all()
    membresias = Membresia.get_all()

    if request.method == "POST":
        cliente_id = request.form["cliente_id"]
        membresia_id = request.form["membresia_id"]
        monto = float(request.form["monto"])
        metodo = request.form["metodo"]

        pago = Pago(cliente_id, membresia_id, monto, metodo)
        pago.save()

        return redirect(url_for("pagos.index"))

    return render_template(
        "pagos/create.html",
        clientes=clientes,
        membresias=membresias
    )


@bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    pago = Pago.get_by_id(id)
    clientes = Cliente.get_all()
    membresias = Membresia.get_all()

    if request.method == "POST":
        pago.cliente_id = request.form["cliente_id"]
        pago.membresia_id = request.form["membresia_id"]
        pago.monto = float(request.form["monto"])
        pago.metodo = request.form["metodo"]
        pago.save()

        return redirect(url_for("pagos.index"))

    return render_template(
        "pagos/edit.html",
        item=pago,
        clientes=clientes,
        membresias=membresias
    )


@bp.route("/delete/<int:id>")
def delete(id):
    pago = Pago.get_by_id(id)
    pago.delete()
    return redirect(url_for("pagos.index"))
