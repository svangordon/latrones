from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
piece = Table('piece', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=16)),
    Column('move_pattern', String(length=4)),
    Column('jump_pattern', String(length=4)),
    Column('fen_char', String(length=1)),
)

game_rule = Table('game_rule', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('height', INTEGER),
    Column('width', INTEGER),
    Column('capture_method', INTEGER),
)

game_rule = Table('game_rule', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('width', Integer),
    Column('height', Integer),
    Column('capture_method_id', Integer),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('nickname', String(length=64)),
    Column('email', String(length=120)),
    Column('rating', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['piece'].create()
    pre_meta.tables['game_rule'].columns['capture_method'].drop()
    post_meta.tables['game_rule'].columns['capture_method_id'].create()
    post_meta.tables['user'].columns['rating'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['piece'].drop()
    pre_meta.tables['game_rule'].columns['capture_method'].create()
    post_meta.tables['game_rule'].columns['capture_method_id'].drop()
    post_meta.tables['user'].columns['rating'].drop()
