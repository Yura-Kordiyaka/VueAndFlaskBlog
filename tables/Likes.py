from main import db


class Likes(db.Model):
    _tablname_ = 'likes'
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer)
    like = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {'id': self.id, 'user_id': self.user_id, 'like': self.like,
                'post_id': self.post_id,
                }
