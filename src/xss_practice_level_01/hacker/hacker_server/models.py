from hacker_server import db

class Hacker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    writer = db.Column(db.String(200), nullable=True)
    title = db.Column(db.String(200), nullable=True)
    content = db.Column(db.Text(), nullable=True)
    create_date = db.Column(db.DateTime(), nullable=True)