from flask import Flask


# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "Hello, World!"

# from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/harry")
def harry():
    return "Hello harry bhai4!"
app.run(debug=True)
