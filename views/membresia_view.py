from flask import render_template

def list(data):
    return render_template("membresias/index.html", data=data)

def create(clientes, planes):
    return render_template("membresias/create.html", clientes=clientes, planes=planes)

def edit(item, clientes, planes):
    return render_template("membresias/edit.html", item=item, clientes=clientes, planes=planes)
