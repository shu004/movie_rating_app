"""Server for movie ratings app."""

from flask import (Flask, render_template, session, redirect, request, flash)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """view homepage."""
    return render_template('homepage.html')

@app.route('/login', methods=['POST'])
def login():
    """logging an existing user"""
    email = request.form.get("email")
    password = request.form.get("password")

    if crud.verify_password(email, password):
        session['user_email'] = email
        flash(f'Logged in as {email}')
    else:
        flash('Incorrect Login')
    return redirect('/')

@app.route('/movies')
def all_movies():
    """View all movies"""
    movies = crud.get_movies()
    return render_template('all_movies.html', movies=movies)

@app.route('/movies/<movie_id>')
def movie_detail(movie_id):
    """show movie details"""
    movie = crud.get_movie_by_id(movie_id)
    return render_template("movie_details.html", movie=movie)

@app.route('/users')
def all_users():
    """view all users"""
    users = crud.get_users()
    return render_template('all_users.html', users=users)


@app.route('/users', methods=['POST'])
def add_user():
    """adding a new user"""
    email = request.form.get("email")
    password = request.form.get("password")

    if crud.get_user_by_email(email):
        flash("You already have an account, please log in")
    else:
        crud.create_user(email=email, password=password)
        flash("You've created your account!")
    return redirect('/')


@app.route('/users/<user_id>')
def user_detail(user_id):
    """show user details"""
    user = crud.get_user_by_id(user_id)
    return render_template("user_details.html", user=user)




if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
