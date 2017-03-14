from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    games = db.relationship('Participant', backref='user', lazy='dynamic')

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

class GameStatus(db.Model):
    __tablename__ = 'game_status'
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(32), index=True)

class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    playing = db.Column(db.Boolean)
    color = db.Column(db.Integer)

class GameRule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Integer)
    width = db.Column(db.Integer)
    capture_method = db.Column(db.Integer, db.ForeignKey('capture_method.id'))

class CaptureMethod(db.Model):
    __tablename__ = 'capture_method'
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(16))

class Move(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # participant_id = db.Column(db.Integer, db.ForeignKey('participant.id')) # we can figure this out from the game_piece
    piece_id = db.Column(db.Integer, db.ForeignKey)
    origin = db.Column(db.Integer)
    destination = db.Column(db.Integer)
    fen = db.Column(db.String(64))
    notation = db.Column(db.String(16))
    half_move = db.Column(db.Integer)

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
