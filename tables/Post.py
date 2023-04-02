from main import db


class Post(db.Model):
    _tablname_ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    like = db.Column(db.Integer, nullable=False)
    dislike = db.Column(db.Integer, nullable=False)
    name_of_post = db.Column(db.String(100), nullable=False)
    text_of_post = db.Column(db.Text, nullable=False)
    category = (db.Column(db.String(100), nullable=False))
    comment = db.Column(db.Text)

    def to_dict(self):
        return {'id': self.id, 'user_id': self.user_id, 'name_of_post': self.name_of_post,
                'like': self.like,
                'dislike': self.dislike,
                'text_of_post': self.text_of_post,
                'category': self.category,
                'comment': self.comment}
