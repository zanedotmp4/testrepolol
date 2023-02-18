from App.database import db
from App.models import user

class departmentMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    isHod = db.Column(db.Boolean, default = False)

    def isHOD(self):
        return self.isHOD
    def assignHOD(self):
        self.isHod = True
    def toJSON(self):
        return{
            'id':self.id,
            'userID':self.userID,
            'isHod':self.isHod

        }
        