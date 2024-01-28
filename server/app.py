#!/usr/bin/env python3

from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, User, Review, Game
from models import Game

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return "Index for Game/Review/User API"


@app.route('/games')
def games():

    games = []
    for game in Game.query.all():
        game_dict = {
            "title": game.title,
            "genre": game.genre,
            "platform": game.platform,
            "price": game.price,
        }
        games.append(game_dict)

    response = make_response(
        jsonify(games),
        200
    )
    response.headers["Content-Type"] = "application/json"
    return response

@app.route('/games_by_title')
def games_by_title():
    games_by_title = Game.query.order_by(Game.title).all()

    game_titles = [game.title for game in games_by_title]

    response = make_response(
        jsonify(game_titles),
        200
    )

    return response

@app.route('/first_10_games')
def first_10_games():
    first_10_games = Game.query.limit(10).all()

    first_games=[]
    for game in first_10_games:
        game_dict = {
            "title":game.title,
            "genre": game.genre,
            "platform": game.platform,
            "price": game.price,
        }
        first_games.append(game_dict)
    response = make_response(jsonify(first_games), 200)
    #return "Testing route"
    return response    

@app.route('/games/<int:id>')
def game_by_id(id):
    game = Game.query.filter_by(id=id).first()

    game_dict = game.to_dict()
    #{
        #"title": game.title,
        #"genre": game.genre,
        #"platform": game.platform,
        #"price": game.price,

    #}
    response = make_response(jsonify(game_dict), 200)
    return response

if __name__ == '__main__':
    app.run(port=5557, debug=True)

  