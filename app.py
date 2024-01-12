from flask import Flask, render_template, request, jsonify
from neo.query import query

app = Flask(__name__)


# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'


@app.route('/', methods=['GET', 'POST'], endpoint='home')
def index(name=None):
    return render_template('index.html', name=name)


@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template('search.html')


@app.route('/search_name', methods=['GET', 'POST'])
def search_name():
    name = request.args.get('name')
    json_data = query(str(name))
    return jsonify(json_data)


# @app.route('/get_all_relation', methods=['GET', 'POST'])
# def get_all_relation():
#     return render_template('all_relation.html')


# @app.route('/query_all_relation', methods=['GET', 'POST'])
# def query_all_relation():
#     res = query_all_rela()
#     return jsonify(res)


if __name__ == '__main__':
    app.run()
