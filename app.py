from flask import Flask
from config import Config, Configdb
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow


# init app
app = Flask(__name__)
app.config.from_object(Config)
app.config.from_object(Configdb)

# init db
db = SQLAlchemy(app)
# init ma
ma = Marshmallow(app)
# init migration
migrate = Migrate(app, db)

# import both routes and models 
import routes, models
