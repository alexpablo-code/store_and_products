from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash 


class Store:
    DB = "store_and_products"

    def __init__(self, data):
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