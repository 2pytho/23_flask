#-*-coding:utf8-*-

from flask import Flask,render_template,request
print("hello flask ")

app=Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('get_post.html')
@app.route('/search/')
def search():
    print(request.args)
    print(request.args.get('q'))
    return 'search test %s'%request.args.get('q')
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        return "post hello %s,%s"%(request.form.get('name'),request.form.get('passwd'))

if __name__  =='__main__':
    app.run(host='0.0.0.0',port = 9005 , debug = True)
