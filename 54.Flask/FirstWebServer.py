from flask import Flask
import random

app = Flask(__name__)

# print(random.__name__)
# print(__name__)

@app.route('/')
def hello():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
        '<p>This is a paragraph.</p>' \
        '<img src="https://media.giphy.com/media/Zkss0cvI6TJki5gS7G/giphy.gif" width=200>'

# -- Differnt routes using the app.route decotator -- #
        
# @app.route("/bye")
# @make_bold
# @make_emphasis
# @make_underlined

def bye():
    return "Bye!"

# -- Differnt routes using the app.route decotator -- #
# @app.route("/bye")
# def bye():
#     return "Bye!"
#     return "<u><em><b>Bye!</b></em></u>"

# -- Creating variable patha and converting the path to a specified data type -- #

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"

if __name__ == "__main__":
    # -- Run the app in debug mode to auto-reload -- #
    app.run(debug=True)




# app.run()
# if __name__ == "__main__":
#     app.run()
