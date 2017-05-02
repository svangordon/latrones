from flask import render_template, flash, redirect, request, jsonify, g, session, make_response
from app import app, db
from .forms import LoginForm
from .models import User, Game, Participant
from flask_restful import Resource, Api, reqparse
from flask_httpauth import HTTPBasicAuth
from flask_oauthlib.client import OAuth
from oauth_config import oauth_credentials
from flask_login import login_user
from random import randrange

api = Api(app)
auth = HTTPBasicAuth()

oauth = OAuth()
twitter = oauth.remote_app('twitter',
    base_url='https://api.twitter.com/1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authenticate',
    consumer_key=oauth_credentials["twitter"]["consumer_key"],
    consumer_secret=oauth_credentials["twitter"]["consumer_secret"]
)
twitter_oauth = "twitter_oauthtok"

@twitter.tokengetter
def get_twitter_token():
    print('trying to get token')
    if twitter_oauth in session:
        resp = session[twitter_oauth]
        print('found twitter token, ==', resp)
        return resp #resp['oauth_token'], resp['oauth_token_secret']

@app.before_request
def before_request():
    print('before request', session)
    g.user = None
    if twitter_oauth in session:
        print('oauth in session', session[twitter_oauth])
        g.user = session[twitter_oauth]

@app.route('/latr/api/v1.0/login', methods=["POST"])
def login():
    print('===== start =====')
    # print('request data', request.view_args, request.form)
    form = request.form
    # print('form.get', form['username'])
    # return 'bang'
    # print('nick', User.query.filter_by(nickname=form["nickname"]).one())
    u = User.query.filter_by(nickname=form['nickname']).one()
    # print(User.query.all())
    # print(u)
    if not u:
        return ("Unknown user", 400)
    if not u.verify_password(form['password']):
        return ("Bad password", 400)
    print('u', u)
    print('verify', u.verify_password(form['password']))
    login_user_result = login_user(u)
    print('login_user_result', login_user_result)
    # return session
    session["user"] = u.json
    return jsonify(u.json)
    # print('session', session)
    # resp = make_response("good job")
    # resp.set_cookie("dummy", "dummy_data")
    # return resp
    # return login_user_result
    # callback_url = 'http://localhost:5000/protected'#url_for('oauthorized', next=request.args.get('next'))
    # return twitter.authorize(callback=callback_url or request.referrer or None)

@app.route('/loginTwitter', methods=["POST"])
def login_twitter():
    callback_url = 'http://localhost:3000/'#url_for('oauthorized', next=request.args.get('next'))
    return twitter.authorize(callback=callback_url or request.referrer or None)

@app.route('/logout')
def logout():
    session.pop(twitter_oauth, None)
    return redirect(url_for('index'))

@app.route('/protected', methods=["GET", "POST"])
def protected():
    print('hitting protectd route', g.user)
    print('session', session)
    if g.user is None:
        return "you are not authorized!!!"
    return "you are authorized"

class UserListAPI(Resource):
    """ Responsible for creating new users and, I guess, getting a list of all users """
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('nickname', type=str, required=True, location='form')
        self.reqparse.add_argument('email', type=str, required=True, location='form')
        self.reqparse.add_argument('password', type=str, required=True, location='form')
        super(UserListAPI, self).__init__()

    def get(self):
        users = User.query.all()
        return jsonify([{"id":u.id, "nickname":u.nickname, "email":u.email} for u in users])

    def post(self):
        """ Create user """
        args = self.reqparse.parse_args()
        print("===============", args["nickname"], User.query.filter_by(nickname=args["nickname"]).first())
        if User.query.filter_by(nickname=args["nickname"]).first() is not None:
            print("user is not unique")
            return 400
        user = User(nickname=args["nickname"], email=args["email"])
        user.hash_password(args["password"])
        user.set_gravatar()
        db.session.add(user)
        db.session.commit()
        respo = User.query.filter(User.nickname == args["nickname"]).first()
        print(respo)
        return user.json

class UserAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        # self.reqparse.add_argument('user_id', type=int, required=True)
        self.reqparse.add_argument('email', type=str, location='json')
        self.reqparse.add_argument('nickname', type=str, location='json')
        super(UserAPI, self).__init__()

    def get(self, user_id):
        u = User.query.get(user_id)
        print(u)
        return jsonify({'id': u.id, 'nickname': u.nickname, 'email': u.email})

    def put(self, user_id):
        """ Edit a user's record. """
        args = self.reqparse.parse_args()
        print('===', app.config['DEBUG'], '===')
        if not app.config['DEBUG']:
            raise NotImplementedError("validate that user is modifying own record")
        u = User.query.get(user_id)
        u.nickname = args['nickname']
        u.email = args['email']
        db.session.commit()
        return jsonify({'id': u.id, 'nickname': u.nickname, 'email': u.email})

    def post(self, user_id):
        """ Read the user off the session, and return their own user object to them. """
        print("beginning post")
        if int(user_id) != 0:
            return ("Bad request. Expected user_id == 0", 400) # just some error checking
        try:
            u = User.query.get(session["user"]["id"])
            print("returning", u)
            return u.json
        except (KeyError, AttributeError):
            return None

    def delete(self, user_id):
        args = self.reqparse.parse_args()
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()
        return 'user deleted'

class GameAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        # self.reqparse.add_argument('user_id', type=int, required=True)
        # self.reqparse.add_argument('email', type=str, location='json')
        # self.reqparse.add_argument('nickname', type=str, location='json')
        super(GameAPI, self).__init__()

    def get(self, game_id):
        game = Game.query.get(game_id)
        print(game)
        # return jsonify({'id': u.id, 'nickname': u.nickname, 'email': u.email})
        return 'you got game {0}'.format(game.game_id)

    def delete(self, game_id):
        game = Game.query.get(game_id)
        db.session.delete(game)
        db.session.commit()
        return True

# responsible for getting a list of all games
class GameListAPI(Resource):
    def __init__(self):
        super(GameListAPI, self).__init__()

    def get(self):
        games = Game.query.all()
        # print('players',games[0].players.all())
        participants = Participant.query.all()
        # print(participants[-1].user)
        print(games[-1].players.all())
        return jsonify([{
            "game_id": g.id,
            "start_time": g.start_time,
            "status_id": g.status_id,
            "players": [{"nickname": p.user.nickname, 'user_id': p.user.id} for p in g.players.all()]
        } for g in games])

    def start_game(self, game):
        print('starting game', game)
        print('participants', game.players.all())
        player_color = randrange(2)
        opponent_color = 1 - player_color

    def post(self, user_id=None):
        """ To become the matchmaking route. """
        # self.reqparse = reqparse.RequestParser()
        # self.reqparse.add_argument('user_id', type=str, required=True)
        # args = self.reqparse.parse_args()
        # print('q string', request.args.get('user_id'))

        # #
        # print(Game.query.first().players.all())
        # games = Game.query.filter(db.session.query.get(Game.id).players.all().count() == 1).all()
        # print(db.func.count(1))
        # games = Game.query.filter(db.func.count(1) == 1).all()
        user_id = session["user"]["id"]
        # check to make sure user doesn't have a game already open
        open_game = db.session.query(Game)\
            .join(Participant)\
            .group_by(Game)\
            .filter(Game.players.any() == user_id)\
            .first()
        if open_game:
            print('returning open game')
            print(open_game.rules.initial_fen)
            return open_game.json

        games = db.session.query(Game)\
            .join(Participant)\
            .group_by(Game)\
            .having(db.func.count(Participant.id) < 2)\
            .filter(Game.players.any() != user_id)\
            .all()
        print("games", games)
        game = None
        if len(games) == 0:
            """ No open games, so open one"""
            print('creating game')
            game = Game()
            game.status_id = 1
            game.game_rule_id = 1
            db.session.add(game)
            db.session.commit()
            # print(game, game.id, addResult, commitResult)
        else:
            game = games[0]

        game.add_participant(user_id)

        if len(game.players.all()) == 2:
            game.start_game()

        return jsonify({
            "game_id": game.id,
            "start_time": game.start_time,
            "status_id": game.status_id,
            "players": [{"nickname": p.user.nickname, 'user_id': p.user.id} for p in game.players.all()]
        })

# Setup the API endpints, and connect them to the ORM wrappers
api.add_resource(GameAPI, '/latr/api/v1.0/game/<game_id>', endpoint='game')
api.add_resource(GameListAPI, '/latr/api/v1.0/games', endpoint='games')
api.add_resource(UserListAPI, '/latr/api/v1.0/users', endpoint='users')
api.add_resource(UserAPI, '/latr/api/v1.0/user/<user_id>', endpoint='user')


# These are the 'non-api' routes. Ignore them. except for reference as needed
@app.route('/')
@app.route('/index')
# @auth.login_required
def index():
    # user = {'nickname': 'Miguel'}
    # posts = [
    #     {
    #         'author': {'nickname': 'John'},
    #         'body': 'Beautiful day in Portland!'
    #     },
    #     {
    #         'author': {'nickname': 'Susan'},
    #         'body': 'The Avengers movie was so cool!'
    #     }
    # ]
    return "Good boy"
    # return render_template('index.html',
    #                        title='Home',
    #                        user=user,
    #                        posts=posts)

# @app.route('/latr/api/v1.0/games', methods=["GET"])
# def butts():
#     return 'you touched the butt'

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         flash('Login requested for OpenID="%s", remember_me=%s' %
#               (form.openid.data, str(form.remember_me.data)))
#         return redirect('/index')
#     return render_template('login.html',
#                            title='Sign In',
#                            form=form,
#                            providers=app.config['OPENID_PROVIDERS'])

# @app.route('/user', methods=['GET', 'POST'])
# def user(user_id=None):
#     # user = User.query.filter_by(nickname='john').first()
#     # print(user)
#     return 'does this work?'
#
# @app.route('/user', methods=['POST'])
# @app.route('/user/<user_id>', methods=['GET', 'POST'])
# def user(user_id=None):
#     user = User.query.filter_by(nickname='john').first()
#     print(user)
#     return 'user_id = {0}'.format(user_id)
#
# @app.route('/game')
