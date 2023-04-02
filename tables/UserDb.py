from main import db


class UserDb(db.Model):
    _tablname_ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)

    @property
    def Tostring(self):
        return {
            'id':self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password
        }
