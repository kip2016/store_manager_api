from flask import jsonify, make_response, request
from flask_restful import Api, Resource

cart = []


class Products(Resource):
    # Get all cart entries
    def get(self):
        return make_response(jsonify({
            'Status': 'Ok',
            'Message': "Success",
            'My orders': cart
        }), 200)

    # Add to cart
    def post(self):

        id = len(cart) + 1
        data = request.get_json()
        name = data['name']
        description = data['description']
        price = data['price']

        item = {
            'id': id,
            'name': name,
            'description': description,
            'price': price
        }

        cart.append(item)
        return make_response(jsonify({
            'Status': 'Ok',
            'Message': "Post Success",
            'My Cart': cart
        }), 201)


class SingleProduct(Resource):
    # Get a single cart entry
    def get(self, orderID):
        order = [order for order in cart if order['id'] == orderID]
        if len(order) == 1:
            return make_response(jsonify({
                                 'Status': 'Ok',
                                 'Message': "Success",
                                 'My order': order
                                 }), 200)

