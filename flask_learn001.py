#-*-coding:utf8-*-

from flask import Flask
print("hello flask ")

app=Flask(__name__)
@app.route('/')
def hello_world():
    return 'hello world flask'

if __name__  =='__main__':
    app.run(host='0.0.0.0',port = 9000 , debug = True)
