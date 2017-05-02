from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
game_rule = Table('game_rule', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('width', Integer),
    Column('height', Integer),
    Column('capture_method_id', Integer),
    Column('initial_fen', String(length=256)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['game_rule'].columns['initial_fen'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['game_rule'].columns['initial_fen'].drop()
