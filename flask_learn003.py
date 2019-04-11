#-*-coding:utf8-*-

from flask import Flask,redirect,url_for
print("hello flask ")

app=Flask(__name__)
@app.route('/')
def hello_world():
    login_url = url_for('login')
    return redirect(login_url)
    return 'hello world flask003'

@app.route('/login/')
def login():
    return 'hello login 11'
if __name__  =='__main__':
    app.run(host='0.0.0.0',port = 9003 , debug = True)
