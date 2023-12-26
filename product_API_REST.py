from flask import Flask
from flask_restful import Resource, Api, reqparse

app=Flask(__name__)
api=Api(app)


#Product list put directly in the code at first - to be replaced by a database connexion#
products = [
    { "id": 1, "name": "Stylo 4 couleurs", "price": 10, "category": "Papeterie" },
    { "id": 2, "name": "Cahier vert", "price": 20, "category": "Papeterie" },
    { "id": 3, "name": "Télévision 4K", "price": 30, "category": "Tech" },
    { "id": 4, "name": "Souris sans fil", "price": 40, "category": "Tech" },
    { "id": 5, "name": "Ananas", "price": 50, "category": "Alimentaire" },
    { "id": 6, "name": "Kinder Bueno", "price": 60, "category": "Alimentaire" },
    { "id": 7, "name": "Chemise de président", "price": 70, "category": "Textile" },
    { "id": 8, "name": "T-shirt de punk", "price": 80, "category": "Textile" },
    { "id": 9, "name": "Tournevis bleu", "price": 90, "category": "Bricolage" },
    { "id": 10, "name": "Marteau rouge", "price": 100, "category": "Bricolage" }
    ]

class Product(Resource):
    def get(self, id):
        for product in products:
            if (id == product["id"]):
                return product, 200
            return "Product not found", 404

    def post(self, id):
        parser = reqparse.Parser()
        parser.add_argument("name")
        parser.add_argument("price")
        parser.add_argument("category")
        args=parser.parse.args()

        for product in products:
            if(id==product["id"]):
                return "The product {} already exists".format(id),400
            
        product ={
            "id": id,
            "name": args["name"],
            "price":args["price"],
            "category":args["category"]
        }

        products.append(product)
        return product, 201

    def put(self, id):
        parser = reqparse.Parser()
        parser.add_argument("name")
        parser.add_argument("price")
        parser.add_argument("category")
        args=parser.parse.args()

        for product in products:
            if(id==product["id"]):
                product["name"] = args["name"]
                product["price"] = args["price"]
                product["category"] = args["category"]
                return product, 200
            
        product ={
            "id": id,
            "name": args["name"],
            "price":args["price"],
            "category":args["category"]
        }

        products.append(product)
        return product, 201

    def delete(self, id):
        global products
        products = [product for product in products if product["id"] != id]
        return "{} is deleted".format(id), 200
    
api.add_resource(Product, "/product/<int:id>")
app.run(debug=True)





