from flask import Blueprint, render_template, request, redirect, url_for
from config.security import requiere_admin
from models.inventario_model import InventarioMovimiento
from models.producto_model import Producto

bp = Blueprint("inventario", __name__, url_prefix="/inventario")


@bp.route("/")
@requiere_admin
def index():
    data = InventarioMovimiento.get_all()
    productos = Producto.get_all()
    return render_template("inventario/index.html", data=data, productos=productos)


@bp.route("/create")
def create():
    productos = Producto.get_all()
    return render_template("inventario/create.html", productos=productos)


@bp.route("/movimiento", methods=["POST"])
def movimiento():
    mov = InventarioMovimiento(
        request.form["producto_id"],
        request.form["tipo"],
        request.form["cantidad"]
    )
    mov.save()
    return redirect(url_for("inventario.index"))
