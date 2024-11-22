from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    role = db.Column(db.SmallInteger, nullable=False)
    adress = db.Column(db.String(256))
    email = db.Column(db.String(256), unique=True)

    def __repr__(self):
        return f"<User {self.username}>"
    
    