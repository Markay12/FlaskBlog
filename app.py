from flask import Flask
# __name__ == special module in python
app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'Hello World!'