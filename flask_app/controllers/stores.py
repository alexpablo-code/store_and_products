from flask_app import app
from flask import render_template, redirect, request, session



@app.route("/")
def dashboard():
    return render_template("dashboard.html")