import os

from peewee import *

db = SqliteDatabase(os.environ.get("DATABASE_URI"))


class BaseModel(Model):
    class Meta:
        database = db


class BlockChain(BaseModel):
    block_height = IntegerField(primary_key=True, index=True)
    current_hash = TextField(null=False)
    previous_hash = TextField(null=False)
    create_time = DateTimeField(null=False)
    header = TextField(null=False)
    body = TextField(null=False)


def init_database():
    try:
        db.execute_sql("drop table blockchain")
    except Exception:
        pass
    BlockChain.create_table()


def clean_database():
    db.execute_sql("delete from blockchain where true")


def query_latest_block():
    return BlockChain.select().order_by(BlockChain.block_height)[-1]
