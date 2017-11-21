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
    cnx = MySQLdb.connect(user='npatel', passwd='namrata',
                          host='127.0.0.1', db='docker_connect')
    add_employee = ("INSERT INTO access_log "
                    "(request_data, access_timestamp) "
                    "VALUES (%s, %s)")
    ip = request.environ['REMOTE_ADDR']

    with cnx.cursor() as cursor:
        cursor.execute(add_employee, [ip, datetime.today()])
    cnx.close()

    return 'Hello, {}'.format(ip)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
