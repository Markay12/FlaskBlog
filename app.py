from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# '////' is an absolute path and '///' is relative so we don't add a specific location
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.database'
database = SQLAlchemy(app)

class Todo(database.Model):
    #database model for list
    id = database.Column(database.Integer, primary_key=True)
    content = database.Column(database.String(200), nullable=False)
    data_created = database.Column(database.DateTime, default=datetime.utcnow)

    def __repr__(self):
        #returns task that we just created
        return '<Task %r>' % self.id


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)