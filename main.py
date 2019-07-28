from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['Debug'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:password@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(500))

    def __init__(self, title, body):
        self.title = title
        self.body = body


@app.route('/blog', methods =['POST', 'GET'])
def blog ():

    blogs = Blog.query.all()
    return render_template('blog.html',title="Your Blog Posts", blogs=blogs)


@app.route('/new-post', methods=['POST', 'GET'])
def new_post():
        if request.method == 'POST':
            blog_post = request.form['blog']
            new_blog_post = Blog(title, blog_post)
            db.session.add(new_blog_post)
            db.session.commit()

            return render_template('new-post.html')


if __name__ == '__main__':
    app.run()