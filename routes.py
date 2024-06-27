from models import db, Player, Powers
from flask import request, redirect, url_for, render_template

def roout_route(app):
    
    @app.route("/")
    def home(): 
        return "This is the home page"
    
    @app.route("/create", methods = ['POST', 'GET'])
    def create_usr(): 
        if request.method == "POST":
            playername = request.form['player']
            powername = request.form['power']
            new_player = Player(play_name = playername)
            db.session.add(new_player)
            db.session.commit()
            if powername != "":
                new_power = Powers(name = powername, player = new_player)
                db.session.add(new_power)
                db.session.commit()
            


            return "Done"
        else:
            return render_template("index.html")