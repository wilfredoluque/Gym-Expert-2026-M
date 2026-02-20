from flask import render_template

def list(data):
    return render_template("clientes/index.html", data=data)

def create():
    return render_template("clientes/create.html")

def edit(item):
    return render_template("clientes/edit.html", item=item)
