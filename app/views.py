from flask import render_template, flash, redirect, request, jsonify
from app import app, db
from .forms import LoginForm
from .models import User
from flask_restful import Resource, Api, reqparse
from flask_httpauth import HTTPBasicAuth

api = Api(app)
auth = HTTPBasicAuth()

@auth.get_password
def get_pw(nickname):
    u = User.query.filter_by(nickname=nickname)
    if u:
        return u.password
    return None

class UserListAPI(Resource):
    """ Responsible for creating new users and, I guess, getting a list of all users """
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('nickname', type=str, required=True, location='json')
        self.reqparse.add_argument('email', type=str, required=True, location='json')
        super(UserListAPI, self).__init__()

    def get(self):
        users = User.query.all()
        return jsonify([{"id":u.id, "nickname":u.nickname, "email":u.email} for u in users])

    def post(self):
        args = self.reqparse.parse_args()
        user = User(**args)
        print('===')
        print(user)
        db.session.add(user)
        db.session.commit()
        respo = User.query.filter(User.nickname == args["nickname"])
        print(respo)
        return 'user added'



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
        args = self.reqparse.parse_args()
        print('===', app.config['DEBUG'], '===')
        if not app.config['DEBUG']:
            raise NotImplementedError("validate that user is modifying own record")
        u = User.query.get(user_id)
        u.nickname = args['nickname']
        u.email = args['email']
        db.session.commit()
        return jsonify({'id': u.id, 'nickname': u.nickname, 'email': u.email})

    def delete(self, user_id):
        args = self.reqparse.parse_args()
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()
        return 'user deleted'

api.add_resource(UserListAPI, '/latr/api/v1.0/users', endpoint='users')
api.add_resource(UserAPI, '/latr/api/v1.0/user/<user_id>', endpoint='user')

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])

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
