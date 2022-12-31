from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.store import Store



@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/add-store")
def add_store():
    return render_template("add_store.html")

@app.route("/create-store", methods=['POST'])
def create_store():
    print(request.form)
    Store.create_store(request.form)

    return redirect("/")