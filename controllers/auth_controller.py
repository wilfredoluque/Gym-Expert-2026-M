from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.usuario_model import Usuario

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = Usuario.get_by_email(email)

        if user and user.check_password(password):
            session["user_id"] = user.id
            session["user_nombre"] = user.nombre
            session["user_rol"] = user.rol
            if user.rol == "admin":
                return redirect(url_for("dashboard.index"))
            else:
                    return redirect(url_for("asistencias.index"))

        else:
            flash("Credenciales incorrectas", "danger")

    return render_template("auth/login.html")

@bp.route("/register", methods=["GET","POST"])
def register():
    from models.usuario_model import Usuario

    if request.method == "POST":
        u = Usuario(
            request.form["nombre"],
            request.form["email"],
            request.form["password"],
            request.form["rol"]
        )
        u.save()
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html")



@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
