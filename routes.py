from flask import request, render_template

def root_routes(app): 
    

    @app.route("/")
    def home():
        return render_template('index.html')