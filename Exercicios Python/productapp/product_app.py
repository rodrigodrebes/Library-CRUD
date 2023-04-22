# product_app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'product.db')
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(200), nullable=True)
    price = db.Column(db.Float, nullable=False)

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

with app.app_context():
    db.create_all()


# product_app.py (continuação)

# Create a Product
@app.route('/products', methods=['POST'])
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']

    new_product = Product(name, description, price)

    db.session.add(new_product)
    db.session.commit()

    return jsonify({'message': 'Product created successfully', 'product': {'id': new_product.id, 'name': new_product.name, 'description': new_product.description, 'price': new_product.price}}), 201

# Get All Products
@app.route('/products', methods=['GET'])
def get_products():
    all_products = Product.query.all()
    result = [{'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price} for product in all_products]
    return jsonify(result)

# Get Single Product
@app.route('/products/<id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    if product:
        return jsonify({'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price})
    else:
        return jsonify({'error': 'Product not found'}), 404

# Update a Product
@app.route('/products/<id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)

    if product:
        product.name = request.json.get('name', product.name)
        product.description = request.json.get('description', product.description)
        product.price = request.json.get('price', product.price)

        db.session.commit()

        return jsonify({'message': 'Product updated successfully', 'product': {'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price}})
    else:
        return jsonify({'error': 'Product not found'}), 404

# Delete Product
@app.route('/products/<id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Product deleted successfully'})
    else:
        return jsonify({'error': 'Product not found'}), 404

#Run Server
if __name__ == '__main__':
    app.run(debug=True)
