from peewee import *

from src.config import *
from .data_model import BlockChain
db = SqliteDatabase(DATABASE_URI)


def query_latest_block():
    query = BlockChain.select().order_by(BlockChain.block_height).limit(1)
    if len(query) > 0:
        return query[0]
    return None
