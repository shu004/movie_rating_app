"""Populating the database with Data """

import os
import json
from random import choice, randint
from datetime import datetime
import crud, server, model



os.system('dropdb ratings')
os.system('createdb ratings')
model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as file:
    #movie_data (a list of dicts)
    movie_data = json.loads(file.read())

movies_in_db = []

for movie in movie_data:
    date = datetime.strptime(movie['release_date'],"%Y-%m-%d")
    each_movie = crud.create_movie(movie['title'], movie['overview'], date, movie['poster_path'])
    movies_in_db.append(each_movie)

for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    user = crud.create_user(email, password) #generate 10 users

    #generating 10 ratings for each user
    for _ in range(10):
        random_movie = choice(movies_in_db)
        random_score = randint(1, 5)

        crud.create_rating(user, random_movie, random_score) 
