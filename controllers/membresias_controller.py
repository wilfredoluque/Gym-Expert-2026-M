from flask import Blueprint, render_template, request, redirect, url_for
from models.membresia_model import Membresia
from models.cliente_model import Cliente
from models.plan_model import Plan
from core.database import db

bp = Blueprint("membresias", __name__, url_prefix="/membresias")


@bp.route("/")
def index():
    data = Membresia.get_all()
    return render_template("membresias/index.html", data=data)


@bp.route("/create", methods=["GET", "POST"])
def create():
    clientes = Cliente.get_all()
    planes = Plan.get_all()

    if request.method == "POST":
        cliente_id = request.form["cliente_id"]
        plan = Plan.get_by_id(request.form["plan_id"])

        m = Membresia(cliente_id, plan)
        m.save()
        return redirect(url_for("membresias.index"))

    return render_template("membresias/create.html", clientes=clientes, planes=planes)


@bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    m = Membresia.get_by_id(id)
    clientes = Cliente.get_all()
    planes = Plan.get_all()

    if request.method == "POST":
        m.cliente_id = request.form["cliente_id"]
        m.plan_id = request.form["plan_id"]
        db.session.commit()
        return redirect(url_for("membresias.index"))

    return render_template(
        "membresias/edit.html",
        item=m,
        clientes=clientes,
        planes=planes
    )


@bp.route("/delete/<int:id>")
def delete(id):
    m = Membresia.get_by_id(id)
    m.delete()
    return redirect(url_for("membresias.index"))
