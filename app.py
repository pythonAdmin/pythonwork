# -*- coding: utf-8 -*-
import pymysql
import config
from flask import Flask, escape, request, render_template, session, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key="djskla"
app.config.from_object(config)


@app.route('/user/<username>', methods=['get'])
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)


db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username


# db.create_all()


# @app.route('/', defaults={"name": 'world'})
# def index(name):
#     return render_template('index.html', name=name)

@app.route('/users')
def users():
    if session.get('user_id'):
        user = User.query.first()
        print(user.username)
        return render_template('index.html', username=user.username)
    else:
        return redirect('/')



@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/login', methods=['GET', 'PoSt'])
def login():
    if request.method == 'GET':
        return render_template('Wopop.html')
    else:
        name = request.form.get('name')
        pwd = request.form.get('password')

        user = User.query.filter(User.username == name).first()

        if user and user.password == pwd:
            session['user_id'] = user.id
            return redirect(url_for('users'))
        else:
            flash('登陆失败')
            return render_template('Wopop.html')


if __name__ == '__main__':
    # app.run('0.0.0.0', 8099, debug=True)
    app.run()
