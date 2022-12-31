from flask_app import app
from flask import render_template, redirect, request, session



@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/add-store")
def add_store():
    return render_template("add_store.html")