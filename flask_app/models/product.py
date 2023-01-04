from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash

class Product:
    DB = "store_and_products"

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.price = data["price"]
        self.category = data["category"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create_product(cls, product_data):
        data = {
            "name": product_data['name'],
            "price": product_data['price'],
            "category": product_data['category'],
            "store_id": product_data['store_id']
        }

        query = """
                INSERT INTO products (name, price, category, store_id, created_at, updated_at)
                VALUES (%(name)s,%(price)s,%(category)s,%(store_id)s,NOW(),NOW());
                """

        return connectToMySQL(cls.DB).query_db(query,data)

    # @classmethod 
    # def store_products(cls, store_id):
    #     data = {
    #         "store_id": store_id
    #     }

    #     query = """
    #             SELECT * FROM products
    #             WHERE products.user_id = %(store_id)s;
    #             """

    #     results = connectToMySQL(cls.DB).query_db(query,data)

    #     store_products = []

    #     for row in results:
    #         product = cls(row)

    #         store_products.append(product)

    #     return store_products
