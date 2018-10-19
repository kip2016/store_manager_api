from flask import jsonify, make_response, request
from flask_restful import Api, Resource

cart = []

class SaleOrder(Resource):
    # Get all sales orders
    def get(self):
        return make_response(jsonify({
            'Status': 'Ok',
            'Message': "Success",
            'My sales': cart
        }), 200)

    #add a sale order
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


class SingleSale(Resource):
    # Get a single sale order
    def get(self, orderID):
        order = [order for order in cart if order['id'] == orderID]
        if len(order) == 1:
            return make_response(jsonify({
                                 'Status': 'Ok',
                                 'Message': "Success",
                                 'My order': order
                                 }), 200)
    

