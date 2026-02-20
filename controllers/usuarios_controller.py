from flask import Blueprint, render_template, request, redirect, url_for
from config.security import requiere_admin
from models.usuario_model import Usuario

bp = Blueprint("usuarios", __name__, url_prefix="/usuarios")


@bp.route("/")
@requiere_admin
def index():
    data = Usuario.get_all()
    return render_template("usuarios/index.html", data=data)


@bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        u = Usuario(
            request.form["nombre"],
            request.form["email"],
            request.form["password"],
            request.form["rol"]
        )
        u.save()
        return redirect(url_for("usuarios.index"))

    return render_template("usuarios/create.html")


@bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    u = Usuario.get_by_id(id)

    if request.method == "POST":
        u.update(
            nombre=request.form["nombre"],
            email=request.form["email"],
            rol=request.form["rol"],
            password=request.form.get("password")
        )
        return redirect(url_for("usuarios.index"))

    return render_template("usuarios/edit.html", item=u)


@bp.route("/delete/<int:id>")
def delete(id):
    u = Usuario.get_by_id(id)
    u.delete()
    return redirect(url_for("usuarios.index"))
