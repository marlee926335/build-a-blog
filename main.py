from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy

#MAKE SURE TO SET UP SQL DATABASE

app = Flask(__name__)
app.config['Debug'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = #add sql and mysql info
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'randomstring'


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(500))

    def __init__(self, title, body):
        self.title = title
        self.body = #body
        self.owner = owner



@app.route('/blog', methods =['POST', 'GET'])
def blog ():


    return render_template('blogpage.html')


@app.route('/new-post', methods=['POST'])
def new_post():
       if request.method == 'POST':
        blog_post = request.form['blog']
        new_blog_post = Blog(title, body)
        db.session.add(new_blog_post)
        db.session.commit()

    return redirect('/blog')


if __name__ == '__main__':
    app.run()