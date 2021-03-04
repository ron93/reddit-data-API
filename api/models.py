from . import db

class Thread(db.Model):
    __tablename__ = 'threads'
    id = db.Column(db.Integer, primary_key=True)
    thread = db.Column(db.String())
    sentiment = db.Column(db.Float())
    time = db.Column(db.DateTime()) 