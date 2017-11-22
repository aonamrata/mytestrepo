
from datetime import datetime

from flask import Flask
from flask import request
import MySQLdb
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    cnx = MySQLdb.connect(user='root', passwd='namrata',
                          host='box.vr.devorch.com', db='docker_logs',port=33061)
    select_query = ("SELECT * FROM access_log ")
    data = {'Hello': 'world'}
    with cnx.cursor() as cursor:
        cursor.execute(select_query)
        data = cursor.fetchall()
    cnx.close()
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0")