from flask import render_template

def list(data):
    return render_template("inventario/index.html", data=data)

def create(productos):
    return render_template("inventario/create.html", productos=productos)
