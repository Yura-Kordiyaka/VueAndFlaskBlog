from main import db


class Dislike(db.Model):
    _tablname_ = 'dislike'
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer)
    dislike = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {'id': self.id, 'user_id': self.user_id, 'dislike': self.dislike,
                'post_id': self.post_id,
                }
