from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
capture_method = Table('capture_method', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('desc', String(length=16)),
)

chat = Table('chat', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('participant_id', Integer),
    Column('message', String(length=256)),
)

game = Table('game', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('status_id', Integer),
    Column('start_time', DateTime),
)

game_piece = Table('game_piece', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('piece_id', Integer),
    Column('participant_id', Integer),
    Column('position', Integer),
    Column('trapped', Boolean),
)

game_rule = Table('game_rule', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('height', Integer),
    Column('width', Integer),
    Column('capture_method', Integer),
)

game_status = Table('game_status', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('desc', String(length=32)),
)

move = Table('move', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('piece_id', Integer),
    Column('origin', Integer),
    Column('destination', Integer),
    Column('fen', String(length=64)),
    Column('notation', String(length=16)),
    Column('half_move', Integer),
)

participant = Table('participant', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('user_id', Integer),
    Column('game_id', Integer),
    Column('playing', Boolean),
    Column('color', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['capture_method'].create()
    post_meta.tables['chat'].create()
    post_meta.tables['game'].create()
    post_meta.tables['game_piece'].create()
    post_meta.tables['game_rule'].create()
    post_meta.tables['game_status'].create()
    post_meta.tables['move'].create()
    post_meta.tables['participant'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['capture_method'].drop()
    post_meta.tables['chat'].drop()
    post_meta.tables['game'].drop()
    post_meta.tables['game_piece'].drop()
    post_meta.tables['game_rule'].drop()
    post_meta.tables['game_status'].drop()
    post_meta.tables['move'].drop()
    post_meta.tables['participant'].drop()
