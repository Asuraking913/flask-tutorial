from flask import Flask, g
from config import Appconfig
from extensions import db
from routes import root_routes
from events import socket
from werkzeug.middleware.proxy_fix import ProxyFix

def create_app():
    app = Flask(__name__)
    app.config.from_object(Appconfig)
    # app.wsgi_app = ProxyFix(app.wsgi_app)

    root_routes(app)
    socket.init_app(app)
    with app.app_context(): 
        db.init_app(app)
        db.create_all()

    return app