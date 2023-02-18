from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120),nullable=False)
    type1 = db.Column(db.String(120),default=False)

    def __init__(self, username,email,type1,password):
        self.username = username
        self.set_password(password)
        self.email = email
        self.type1 = type1

    def toJSON(self):
        return{
            'id': self.id,
            'username': self.username
            'email':self.email
            'isHOD'.self.isHOD
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

