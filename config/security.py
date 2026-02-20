from werkzeug.security import generate_password_hash, check_password_hash
from flask import session, redirect, url_for
from functools import wraps

def hash_password(password):
    return generate_password_hash(password)

def verify_password(hashed, password):
    return check_password_hash(hashed, password)
def requiere_admin(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("auth.login"))
        if session.get("user_rol") != "admin":
            return redirect(url_for("dashboard.index"))
        return f(*args, **kwargs)
    return wrap

