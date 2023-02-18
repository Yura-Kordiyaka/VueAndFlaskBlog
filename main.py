from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)


@app.route('/getdata')
def query_example():
    q = request.args.get('query')
    params = {'q': q}
    link = "https://api.github.com/search/topics"
    respone = requests.get(link, params)
    return jsonify(
        {'episodes': respone.json()},

    )


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True)
