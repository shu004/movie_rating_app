"""CRUD operations"""

from operator import pos
from model import db, User, Movie, Rating, connect_to_db


#----------------------user functions--------------------#
def create_user(email, password):
    """Create and return a new user."""

    user = User (email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def get_users():
    """Return all users"""
    return User.query.all()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def get_user_by_email(email):
    return User.query.filter(User.email == email).one()

def verify_password(email, password):
    user = User.query.filter(User.email == email).one()
    return user.password == password

#----------------------movies functions ------------------#
def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    mov = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path);
    db.session.add(mov)
    db.session.commit()

    return mov

def get_movies():
    """Returns all movies"""
    return Movie.query.all()


def get_movie_by_id(movie_id):
    return Movie.query.get(movie_id)


#----------------------rating functions--------------------#
def create_rating(user, movie, score):
    """Create and return a new rating."""
    rating = Rating(user=user, movie=movie, score=score)

    db.session.add(rating)
    db.session.commit()

    return rating


if __name__ == '__main__':
    from server import app
    connect_to_db(app)