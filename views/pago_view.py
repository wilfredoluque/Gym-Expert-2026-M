from flask import render_template

def list(data):
    return render_template("pagos/index.html", data=data)

def create(clientes, membresias):
    return render_template("pagos/create.html", clientes=clientes, membresias=membresias)

def edit(item, clientes):
    return render_template("pagos/edit.html", item=item, clientes=clientes)
