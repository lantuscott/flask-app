from flask import Flask, render_template, json
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/jsonInvasion')
def jsonInvasion():
    with open('jason.txt', 'r') as json_file:
        data = json.load(json_file)
        return data

    # return render_template("jason.txt")

if __name__ == '__main__':
    app.run(debug=True)



