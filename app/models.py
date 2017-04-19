from app import db, lm
from flask_login import UserMixin
from passlib.apps import custom_app_context as pwd_context

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    # __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, nullable=False, unique=True)
    email = db.Column(db.String(120), index=True, nullable=False, unique=True)
    password_hash = db.Column(db.String(128), index=True)
    social_id = db.Column(db.String(64), nullable=True)
    # posts = db.relationship('Post', backref='author', lazy='dynamic')
    participation = db.relationship('Participant', back_populates='user', lazy='dynamic')
    rating = db.Column(db.Integer)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        # !!!: Remember to change this so it doesn't bite you in the rear end
        if self.password_hash is None:
            return True
        return pwd_context.verify(password, self.password_hash)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status_id = db.Column(db.Integer, db.ForeignKey('game_status.id'))
    start_time = db.Column(db.DateTime)
    players = db.relationship('Participant', back_populates="game", lazy='dynamic')

    def __repr__(self):
        return '<Game %r>' % (self.id)

class GameStatus(db.Model):
    __tablename__ = 'game_status'
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(32), index=True)

    def __repr__(self):
        return '<GameStatus %r>' % (self.desc)

class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    playing = db.Column(db.Boolean)
    color = db.Column(db.Integer)
    game = db.relationship("Game", back_populates="players")
    user = db.relationship("User", back_populates="participation")

    def __repr__(self):
        return '<Participant %r Game: %r User: %r' % (self.user_id, self.game_id, self.user.nickname)

class GameRule(db.Model):
    """ holds the rules for an individual game """
    __tablename__ = 'game_rule'
    id = db.Column(db.Integer, primary_key=True)
    width = db.Column(db.Integer)
    height = db.Column(db.Integer)
    capture_method_id = db.Column(db.Integer, db.ForeignKey('capture_method.id'))
    # capture_method = db.relationship('CaptureMethod', lazy='dynamic')

    def __repr__(self):
        return '<GameRule %r by %r %r>' % (self.width, self.height, self.capture_method_id)

class CaptureMethod(db.Model):
    __tablename__ = 'capture_method'
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(16))

    def __repr__(self):
        return '<CaptureMethod %r %r>' % (self.id, self.desc)

class Move(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # participant_id = db.Column(db.Integer, db.ForeignKey('participant.id')) # we can figure this out from the game_piece
    piece_id = db.Column(db.Integer, db.ForeignKey('game_piece.id'))
    origin = db.Column(db.Integer)
    destination = db.Column(db.Integer)
    fen = db.Column(db.String(64))
    notation = db.Column(db.String(16))
    half_move = db.Column(db.Integer)

    def __repr__(self):
        return '<Move %r %r %r>' % (self.half_move, self.origin, self.destination)

class Piece(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16))
    move_pattern = db.Column(db.String(4))
    jump_pattern = db.Column(db.String(4))
    fen_char = db.Column(db.String(1))

class GamePiece(db.Model):
    __tablename__ = 'game_piece'
    id = db.Column(db.Integer, primary_key=True)
    piece_id = db.Column(db.Integer, db.ForeignKey('piece.id'))
    participant_id = db.Column(db.Integer, db.ForeignKey('participant.id'))
    position = db.Column(db.Integer)
    trapped = db.Column(db.Boolean)

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participant.id'))
    message = db.Column(db.String(256))
