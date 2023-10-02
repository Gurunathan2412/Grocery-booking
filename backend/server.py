from flask import Flask, jsonify, request
from products import get_all_product
from sql_connection import get_connection
import products,unit
import json,orders

app = Flask(__name__)
cnx = get_connection()


@app.route('/')
def hello_name():
    return 'Hello World!'


@app.route('/products', methods=["GET"])
def get_products():
    cnx = get_connection()
    response = jsonify(get_all_product(cnx))
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/get_unit', methods=['GET'])
def get_unit():
    cnx = get_connection()
    response = unit.get_unit(cnx)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/insertProduct', methods=['GET', 'POST'])
def insert_product():
    cnx = get_connection()
    request_payload = json.loads(request.form['data'])
    product_id = products.add_product(cnx, request_payload)
    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    # return  "Hello"


@app.route('/insertOrder', methods=['GET', 'POST'])
def insert_order():
    cnx = get_connection()
    request_payload = json.loads(request.form['data'])
    order_id = orders.insert_order(cnx, request_payload)
    response = jsonify({
        'order_id': order_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    cnx = get_connection()
    response = orders.get_all_orders(cnx)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/deleteProduct', methods=['GET', 'POST'])
def delete_product():
    cnx = get_connection()
    return_id = products.delete_product(cnx, request.form['product_id'])
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.run(debug=True)