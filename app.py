from flask import Flask
# __name__ == special module in python
app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run(debug=True)