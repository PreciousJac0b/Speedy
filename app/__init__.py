from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from sqlalchemy.engine import Engine 
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
app.app_context().push()
db = SQLAlchemy(app)
migrate = Migrate(app, db)



from app import routes
from app.models import *
