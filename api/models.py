from . import db

class Thread(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    thread = db.Column(db.String())
    sentiment = db.Column(db.Float())
    time = db.Columns(db.DateTime())