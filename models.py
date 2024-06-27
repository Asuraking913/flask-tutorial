from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Player(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    play_name = db.Column(db.String(50))
    power = db.relationship("Powers", backref = 'player')
    
class Powers(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'))
