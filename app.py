from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World! <h1>Hello!!</h1>'

@app.route('/<name>')
def user(name):
    return f"Hello {name.title()}!"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)