from flask import Flask
from models import db
from config import Appconfig
from routes import roout_route

app = Flask(__name__)
app.config.from_object(Appconfig)
roout_route(app)

if __name__ == "__main__":
    with app.app_context(): 
        db.init_app(app)
        db.create_all()
    app.run(debug=True)