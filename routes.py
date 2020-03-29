from flask import request, jsonify
from app import app, db
from models import Category, Product, CategorySchema, ProductSchema


# init schema
category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


# home 
@app.route('/', methods=['GET'])
def home():
    response= {
            'data': 'Welcome',
            'status_code' : 202
             }
    return jsonify(response)
    
# add product
@app.route('/product', methods=['POST'])
def add_product():
   name = request.json['name']
   description = request.json['description']
   price = request.json['price']
   qty = request.json['qty']
   cat = request.json['category']

   category = Category.query.filter_by(name=cat).first()
   category_id = category.id
   
   new_product = Product(name, description, price, qty, category_id)
   db.session.add(new_product)
   db.session.commit()
   result = product_schema.dump(new_product)
   response = {
       'data': result,
            'status_code' : 202
   }

   return jsonify(response)

# all categories
@app.route('/category', methods=['GET'])
def get_categories():
   all_categories = Category.query.all()
   result = categories_schema.dump(all_categories)
   response = {
       'data': result,
            'status_code' : 202
   }

   return jsonify(response)

   
# all products
@app.route('/product', methods=['GET'])
def get_products():
   all_products = Product.query.all()
   result = products_schema.dump(all_products)
   response = {
       'data': result,
            'status_code' : 202
   }

   return jsonify(response)

# one product
@app.route('/product/<id>', methods=['GET'])
def get_product(id):
   product = Product.get(id)
   result = product_schema.dump(product)
   response = {
       'data': result,
            'status_code' : 202
   }
   
   return jsonify(response)

# update product
@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
   product = Product.query.get(id)

   name = request.json['name']
   description = request.json['description']
   price = request.json['price']
   qty = request.json['qty']
   category_id = product.category_id
   
   product.name = name
   product.description = description
   product.price = price
   product.qty = qty

   db.session.commit()
   result = product_schema.dump(product)
   response = {
       'data': result,
            'status_code' : 202
   }

   return jsonify(response)

# delete product
@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
   product = Product.query.get(id)
   db.session.delete(product)
   db.session.commit()
   result = product_schema.dump(product)
   response = {
       'data': result,
            'status_code' : 202
   }

   return jsonify(response)


# run server
if __name__ == '__main__':
    app.run(debug=True)
