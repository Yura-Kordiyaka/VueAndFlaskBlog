from flask import request, jsonify
from main import app
import requests


@app.route('/getdata')
def query_example():
    q = request.args.get('query')
    params = {'q': q}
    link = "https://api.github.com/search/topics"
    respone = requests.get(link, params)
    return jsonify(
        {'episodes': respone.json()},

    )


@app.route('/name')
def query_ds():
    return jsonify(
        {'episodes': 'stepan'},
    )
