from flask import Flask
from flask import request
# app is the object
app = Flask(__name__)

@app.route("/")# decorating the function
def hello_world():
    return "Hello, World!"

@app.route("/hello1")
def hello_world1():
    return "Hello, World1!"    

@app.route("/jello2")
def hello_world2():
    return "Hello, World2!" 

@app.route("/hello3")
def hello_world3():
    return "Hello, World3!"    

@app.route("/test1")
def test():
    a = 5+6
    return 'this is my first fun in flast {}'.format(a)

@app.route("/input_url")
def request_input():
    data = request.args.get('x')
    return'this is my inpurt from url {}'.format(data)



if __name__=="__main__":
    app.run(host="0.0.0.0")
