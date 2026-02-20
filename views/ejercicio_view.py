from flask import render_template

def list(data):
    return render_template("ejercicios/index.html", data=data)

def create():
    return render_template("ejercicios/create.html")

def edit(item):
    return render_template("ejercicios/edit.html", item=item)
