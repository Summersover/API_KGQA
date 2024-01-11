from flask import Flask, render_template, jsonify
from neo.query import query_all_rela

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/get_all_relation', methods=['GET', 'POST'])
def get_all_relation():
    return render_template('all_relation.html')


@app.route('/query_all_relation', methods=['GET', 'POST'])
def query_all_relation():
    res = query_all_rela()
    return jsonify(res)


if __name__ == '__main__':
    app.run()
