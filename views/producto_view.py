from flask import render_template

def list(data):
    return render_template("productos/index.html", data=data)

def create():
    return render_template("productos/create.html")

def edit(item):
    return render_template("productos/edit.html", item=item)
