from peewee import *

from .database import db


class BaseModel(Model):
    class Meta:
        database = db


class BlockChain(BaseModel):
    block_height = IntegerField(primary_key=True)
    current_hash = TextField(null=False)
    previous_hash = TextField(null=False)
    crete_time = TimeField(null=False)
    header = TextField(null=False)
    body = TextField(null=False)
