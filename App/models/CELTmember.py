from App.database import db
from App.models import user

class departmentMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def toJSON(self):
        return{
            'id':self.id,
            'userID':self.userID,
            'isHod':self.isHod

        }