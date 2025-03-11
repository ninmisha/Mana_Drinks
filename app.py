from flask import Flask, render_template, jsonify, request, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os
import json
from datetime import datetime

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "your-secret-key-here")

# Simplified MongoDB Configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/mana_drinks"
try:
    mongo = PyMongo(app)
    # Test the connection
    mongo.db.command('ping')
    print("MongoDB connection successful!")
except Exception as e:
    print(f"MongoDB connection error: {e}")

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shop')
def shop():
    products = list(mongo.db.products.find())
    return render_template('shop.html', products=products)

@app.route('/flavours')
def flavours():
    products = list(mongo.db.products.find())
    return render_template('flavours.html', products=products)

@app.route('/subscription')
def subscription():
    return render_template('subscription.html')

@app.route('/points-of-sale')
def points_of_sale():
    # Store data with correct image paths
    stores = [
        {
            'name': 'Downtown Store',
            'address': '123 Main St, City Center',
            'phone': '(555) 123-4567',
            'image': '/static/images/downtown.png',
            'directions': 'https://goo.gl/maps/example1'
        },
        {
            'name': 'Westside Location',
            'address': '456 West Ave, Shopping District',
            'phone': '(555) 234-5678',
            'image': '/static/images/westside.png',
            'directions': 'https://goo.gl/maps/example2'
        },
        {
            'name': 'Mall Kiosk',
            'address': '789 Mall Road, Food Court',
            'phone': '(555) 345-6789',
            'image': '/static/images/mall-kiosk.png',
            'directions': 'https://goo.gl/maps/example3'
        }
    ]
    return render_template('points-of-sale.html', stores=stores)

@app.route('/cart')
def cart():
    return render_template('cart.html')

# API Routes
@app.route('/api/products', methods=['GET'])
def get_products():
    products = list(mongo.db.products.find())
    for product in products:
        product['_id'] = str(product['_id'])
    return jsonify(products)

@app.route('/api/products/<product_id>', methods=['GET'])
def get_product(product_id):
    try:
        product = mongo.db.products.find_one({'_id': ObjectId(product_id)})
        if product:
            product['_id'] = str(product['_id'])
            return jsonify(product)
        return jsonify({'error': 'Product not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/products', methods=['POST'])
def add_product():
    try:
        new_product = request.json
        new_product['created_at'] = datetime.utcnow()
        result = mongo.db.products.insert_one(new_product)
        return jsonify({
            'message': 'Product added successfully',
            'id': str(result.inserted_id)
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/cart', methods=['GET'])
def get_cart():
    cart = session.get('cart', [])
    return jsonify(cart)

@app.route('/api/cart/add', methods=['POST'])
def add_to_cart():
    try:
        product_id = request.json.get('product_id')
        quantity = request.json.get('quantity', 1)
        
        product = mongo.db.products.find_one({'_id': ObjectId(product_id)})
        if not product:
            return jsonify({'error': 'Product not found'}), 404
            
        cart = session.get('cart', [])
        
        # Check if product already in cart
        product_in_cart = next((item for item in cart if item['product_id'] == product_id), None)
        
        if product_in_cart:
            product_in_cart['quantity'] += quantity
        else:
            cart.append({
                'product_id': product_id,
                'quantity': quantity,
                'name': product['name'],
                'price': product['price'],
                'image': product['image']
            })
            
        session['cart'] = cart
        return jsonify({
            'message': 'Product added to cart',
            'cart': cart
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/cart/update', methods=['PUT'])
def update_cart():
    try:
        product_id = request.json.get('product_id')
        quantity = request.json.get('quantity')
        
        cart = session.get('cart', [])
        product_in_cart = next((item for item in cart if item['product_id'] == product_id), None)
        
        if not product_in_cart:
            return jsonify({'error': 'Product not found in cart'}), 404
            
        if quantity <= 0:
            cart.remove(product_in_cart)
        else:
            product_in_cart['quantity'] = quantity
            
        session['cart'] = cart
        return jsonify({
            'message': 'Cart updated',
            'cart': cart
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/cart/remove', methods=['DELETE'])
def remove_from_cart():
    try:
        product_id = request.json.get('product_id')
        cart = session.get('cart', [])
        
        product_in_cart = next((item for item in cart if item['product_id'] == product_id), None)
        if product_in_cart:
            cart.remove(product_in_cart)
            
        session['cart'] = cart
        return jsonify({
            'message': 'Product removed from cart',
            'cart': cart
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/cart/clear', methods=['POST'])
def clear_cart():
    session['cart'] = []
    return jsonify({
        'message': 'Cart cleared',
        'cart': []
    })

if __name__ == '__main__':
    app.run(debug=True) 