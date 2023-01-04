from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import product
from flask_app import app
from flask import flash 


class Store:
    DB = "store_and_products"

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.products = []



    @classmethod
    def create_store(cls, store_data):
        data = {
            "name" : store_data['name']
        }

        query = """
                INSERT INTO stores (name, created_at, updated_at)
                VALUES (%(name)s, NOW(), NOW());
                """

        results = connectToMySQL(cls.DB).query_db(query,data)

        return results 

    @classmethod
    def all_stores(cls):
        query = """
                SELECT * FROM stores;
                """

        results = connectToMySQL(cls.DB).query_db(query)
        stores = []

        for row in results:
            store = cls(row)

            stores.append(store)

        return stores 

    @classmethod
    def select_one(cls, store_id):
        data = {
            "id": store_id
        }

        query = """
                Select * FROM stores
                WHERE id = %(id)s;
                """
        results = connectToMySQL(cls.DB).query_db(query, data)
        store = cls(results[0])

        return store 

    @classmethod
    def store_with_products(cls, store_id):
        data = {
            "id": store_id
        }

        query = """
                SELECT * FROM stores 
                LEFT JOIN products
                ON stores.id = products.store_id
                WHERE stores.id = %(id)s;
                """

        results = connectToMySQL(cls.DB).query_db(query, data)

        store = cls(results[0])

        for row in results:
            product_data = {
                "id": row["products.id"],
                "name": row["products.name"],
                "price": row["price"],
                "category": row["category"],
                "created_at": row["products.created_at"],
                "updated_at": row["products.updated_at"]
            }

            store.products.append(product.Product(product_data))

        return store