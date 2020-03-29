from app import db, ma
from sqlalchemy.orm import validates


# category class and model
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, index=True)

    @validates('name')
    def validate_category_name(self, key, name):
        if not name:
            raise AssertionError('No category name provided')

        if Category.query.filter(Category.name == name):
            raise AssertionError('Category name already used')

        if len(name) < 5 or len(name) > 20:
            raise AssertionError('Category name must be more between 5 and 20 characters')
    

# product class and model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False, index=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float())
    qty = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref='products')

    def __init__(self, name, description, price, qty, category_id):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty
        self.category_id = category_id

    @validates('name')
    def validate_product_name(self, key, name):
        if not name:
            raise AssertionError('No product name provided')

        if Product.query.filter(Product.name == name):
            raise AssertionError('Product name already used')

        if len(name) < 5 or len(name) > 20:
            raise AssertionError('Product name must be more between 5 and 20 characters')

    @validates('price')
    def validate_product_price(self, key, price):
        if price < 0 or price > 1000:
            raise AssertionError('Price must be between 0 and 1000')

    @validates('qty')
    def validate_product_qty(self, key, qty):
        if qty < 0 or qty > 100:
            raise AssertionError('Qty must be between 0 and 100')


# Category schema
class CategorySchema(ma.ModelSchema):
    class Meta:
        model = Category


# Product schema
class ProductSchema(ma.ModelSchema):
    class Meta:
        # fields = ('id', 'name', 'description', 'price', 'qty', 'category_id')
        model = Product
        include_fk = True
