from flask import Flask
from config import Appconfig
from extensions import db
from routes import root_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Appconfig)
    root_routes(app)
    with app.app_context(): 
        db.init_app(app)
        db.create_all()

    return app