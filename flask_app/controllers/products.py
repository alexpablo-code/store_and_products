from flask_app import app
from flask import render_template, request, session, redirect
from flask_app.models.product import Product
from flask_app.models.store import Store


@app.route("/add-product/<int:store_id>")
def add_product(store_id):
    store= Store.select_one(store_id)
    return render_template("add_product.html", store=store)

@app.route("/create-product", methods=['POST'])
def create_product():
    Product.create_product(request.form)

    store_id = request.form["store_id"]

    return redirect(f"/store/{store_id}")

@app.route("/sell-product/<int:product_id>/<int:store_id>")
def sell_product(product_id, store_id):
    Product.delete(product_id)

    return redirect(f"/store/{store_id}")
