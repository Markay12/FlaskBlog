from flask import Flask, render_template
# __name__ == special module in python
app = Flask(__name__)

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
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)