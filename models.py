from app import db, ma


# category class and model
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, index=True)
    

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
