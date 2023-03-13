from functools import wraps

from flask import Flask, request, jsonify, redirect, url_for, session, make_response, Response
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_session import Session
import jwt
from datetime import *
import requests

app = Flask(__name__)
CORS(app)
engine = create_engine('mysql+pymysql://root:password@localhost:3306/vueAndFlask', pool_size=20)
app.config['SQLALCHEMY_DATABASE_URI'] = ('mysql+pymysql://root:password@localhost:3306/vueAndFlask')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SECRET_KEY'] = 'my_secret_key'
Session(app)
db = SQLAlchemy(app)
db.init_app(app)

with app.app_context():
    from tables.UserDb import *
    from tables.Post import *
    from tables.Coment import *

    db.create_all()


def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization')

        invalid_msg = {
            'message': 'Invalid token. Registeration and / or authentication required',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token. Reauthentication required.',
            'authenticated': False
        }
        if not auth_headers:
            return jsonify(invalid_msg), 401
        try:
            token = auth_headers.split(' ')[1]
            data = jwt.decode(token, app.config['SECRET_KEY'])
            user = UserDb.query.filter_by(id=data['sub']).first()
            if not user:
                raise RuntimeError('User not found')
            return f(user, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401  # 401 is Unauthorized HTTP status code
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify(invalid_msg), 401
        # # Perform authentication here
        # # If authentication fails, return 401 Unauthorized response
        # # Otherwise, call the original view function with the provided argument

    return _verify


@app.route('/getdata')
def query_example():
    q = request.args.get('query')
    params = {'q': q}
    link = "https://api.github.com/search/topics"
    respone = requests.get(link, params)
    return jsonify(
        {'episodes': respone.json()},
        {'status': 'suecsees'}

    )


@app.route('/Authorization', methods=['POST'])
def Authorization():
    name = request.args.get('name')
    password = str(request.args.get('password'))
    email = str(request.args.get('email'))
    user = UserDb(email=email, password=password, name=name)
    db.session.add(user)
    db.session.commit()
    return jsonify({"status": "successfully"})


@app.route('/Login', methods=['GET'])
def login():
    password = str(request.args.get('password'))
    email = str(request.args.get('email'))
    user = UserDb.query.filter_by(email=email, password=password).first()
    if user:
        token = jwt.encode({
            'sub': user.id,
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }, app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8'),
                        'status': 'successfully'})
    else:
        return 'Error'


@app.route('/CreatePost', methods=['POST'])
@token_required
def CreatePost(user):
    user = user
    data = request.json
    name_of_post = data.get('name_of_post')
    text_of_post = data.get('text_of_post')
    category_of_post = data.get('category_of_post')

    # тут має бути session і передавати сесію потрібно
    if user:
        post = Post(user_id=user.id, name_of_post=name_of_post, text_of_post=text_of_post,
                    category=category_of_post, like=0, dislike=0)
        db.session.add(post)
        db.session.commit()
        return jsonify({"status": "successfully"})
    else:
        return "hello"


@app.route('/ShowAllPost')
@token_required
def ShowAllPost(user):
    user = user
    all_post = Post.query.all()
    all_post = [
        item.to_dict() for item in all_post]
    comment = Coment.query.all()
    comment = [
        item.to_dict() for item in comment]
    return jsonify({'all_post': all_post,
                    'all_comments': comment})


@app.route('/ShowMyPost')
@token_required
def ShowMyPost(user):
    user = user
    my_post = Post.query.filter_by(user_id=user.id)
    my_post = [item.to_dict() for item in my_post]
    return jsonify(my_post)


@app.route('/AddLike', methods=['POST'])
def AddLike():
    id = request.args.get('id')
    post = Post.query.filter_by(id=int(id)).first()
    post.like += 1
    db.session.add(post)
    db.session.commit()
    all_post = Post.query.all()
    my_post = [
        item.to_dict() for item in all_post]
    return jsonify(my_post)


@app.route('/AddDislike', methods=['POST'])
def AddDislike():
    id = request.args.get('id')
    post = Post.query.filter_by(id=int(id)).first()
    post.dislike += 1
    db.session.add(post)
    db.session.commit()
    all_post = Post.query.all()
    my_post = [
        item.to_dict() for item in all_post]
    return jsonify(my_post)


@app.route('/EditPost', methods=['GET', 'POST'])
def EditPost():
    if request.method == 'GET':
        id = request.args.get('id')
        post = Post.query.filter_by(id=id).first()
        edit_post = post.to_dict()
        return jsonify({'post': edit_post})
    elif request.method == 'POST':
        data = request.json
        id = data.get('id')
        name = data.get('name_of_post')
        text = data.get('text_of_post')
        category = data.get('category_of_post')
        post = Post.query.filter_by(id=id).first()
        post.name_of_post = name
        post.text_of_post = text
        post.category = category
        db.session.add(post)
        db.session.commit()
        return jsonify({'status': 'successfully'})


@app.route('/AddComent', methods=['POST'])
def AddComent():
    post_id = request.args.get('id')
    text_of_comment = request.args.get('text_of_comment')
    coment = Coment(post_id=post_id, user_id=2, text=text_of_comment)
    db.session.add(coment)
    db.session.commit()
    return str(coment)


@app.route('/ShowComment')
def ShowComment():
    post_id = request.args.get('post_id')
    coment = Coment.query.filter_by(post_id=post_id).all()
    if coment:
        comment = [
            item.to_dict() for item in coment]
        return jsonify({'comment': comment})
    else:
        return 'This post does not has any comments'


@app.route('/LogOut')
def LogOut():
    session['id'] = None
    return 'Hello'


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True)
