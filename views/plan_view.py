from flask import render_template

def list(data):
    return render_template("planes/index.html", data=data)

def create():
    return render_template("planes/create.html")

def edit(item):
    return render_template("planes/edit.html", item=item)
