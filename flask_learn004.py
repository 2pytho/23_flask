#-*-coding:utf8 -*-
from flask import Flask,render_template,url_for
app = Flask(__name__)

person = {
    'age':23,
    'id' :25,
}
@app.route('/')
def index():
    #return render_template('index.html',username=u'孙旭元')
    return render_template('index.html', **person)

@app.route('/login')
def login():
    return render_template('login.html')
if __name__ == '__main__':
    app.run(port=9004,debug=True)