from flask import Flask, render_template, url_for, flash, redirect
#import forms
from forms import RegistrationForm, LoginForm
# __name__ == special module in python
app = Flask(__name__)

#secret key
app.config['SECRET_KEY'] = '78c8a537a0e2c41c76ce6b48947b0cce'

# post library that allows us to keep track of user information and posts
# used in home.html to post and understand the template and output
posts = [

    {

        'author': 'Mark Ashinhust',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 07, 2020'


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

#methods allowed to accept, to be able to submit personal information
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()  #create instance of registration form from template
    #validate the form to see if the information provided can create an account
    if form.validate_on_submit():
        #flash a one time message to show if a message can be created
        flash(f'Account Created for { form.username.data }!', 'success')
        #redirect user back to home page when the user successfully creates an account
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()  #create instance of login form from template
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)