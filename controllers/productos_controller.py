from flask import Blueprint, render_template, request, redirect, url_for
from config.security import requiere_admin
from models.producto_model import Producto

bp = Blueprint("productos", __name__, url_prefix="/productos")


@bp.route("/")
@requiere_admin
def index():
    data = Producto.get_all()
    return render_template("productos/index.html", data=data)


@bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        p = Producto(
            request.form["nombre"],
            request.form["precio"],
            request.form["stock"]
        )
        p.save()
        return redirect(url_for("productos.index"))

    return render_template("productos/create.html")
@bp.route("/edit/<int:id>", methods=["GET","POST"])
def edit(id):
    p = Producto.get_by_id(id)

    if request.method == "POST":
        p.update(
            nombre=request.form["nombre"],
            precio=request.form["precio"],
            stock=request.form["stock"]
        )
        return redirect(url_for("productos.index"))

    return render_template("productos/edit.html", item=p)

@bp.route("/delete/<int:id>")
def delete(id):
    p = Producto.get_by_id(id)
    p.delete()
    return redirect(url_for("productos.index"))

