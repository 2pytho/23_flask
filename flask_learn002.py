#-*-coding:utf8-*-
from flask import Flask
import config

app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def hello_world():
    return 'hello,flask 002 '
@app.route('/name/<id>')
def name(id):
    return '%s is name'%id
if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 9001)