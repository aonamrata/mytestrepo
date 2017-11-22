from datetime import datetime

from flask import Flask
from flask import request
import MySQLdb

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    cnx = MySQLdb.connect(user='root', passwd='secret',
                          host='127.0.0.1', db='homestead',port=3306)
    
    ip = request.environ['REMOTE_ADDR']

    cnx.close()

    return 'Hello, {}'.format(ip)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
