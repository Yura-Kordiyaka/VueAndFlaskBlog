from main import db


class Coment(db.Model):
    _tablname_ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    post_id = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {'id': self.id, 'user_id': self.user_id, 'post_id': self.post_id, 'text': self.text}