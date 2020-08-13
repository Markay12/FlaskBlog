from flask import Flask, render_template, url_for
#import forms
from forms import RegistrationForm, LoginForm
# __name__ == special module in python
app = Flask(__name__)

#secret key
app.config['SECRET KEY'] = '78c8a537a0e2c41c76ce6b48947b0cce'

# post library that allows us to keep track of user information and posts
# used in home.html to post and understand the template and output
posts = [

    {

        'author': 'Mark Ashinhust',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 06, 2020'


    },

    {

        'author': 'Mark Ashinhust',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 06, 2020'


    },


]


@app.route("/")
@app.route('/home')
# multiple routes to the same webpage localhost:5000/home and localhost:5000
def home():
    #returns our html template from templates folder
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.register('/register')
def register():
    form = RegistrationForm()  #create instance of registration form from template
    return render_template('register.html', title='Register', form=form)

@app.login('/login')
def login():
    form = LoginForm()  #create instance of login form from template
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)