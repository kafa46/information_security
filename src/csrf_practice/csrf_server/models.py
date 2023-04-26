from csrf_server import db

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    writer = db.Column(db.String(200), nullable=True)
    title = db.Column(db.String(200), nullable=True)
    content = db.Column(db.Text(), nullable=True)
    create_date = db.Column(db.DateTime(), nullable=True)
    
class User(db.Model):
    '''사용자 정보'''
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(200), nullable=True)
    passwd = db.Column(db.String(200), nullable=True)
    name = db.Column(db.String(200), nullable=True)
    email = db.Column(db.String(200), nullable=True)
    university = db.Column(db.String(200), nullable=True)