import json
import random
import time

from src.blockchain.persistence.database import query_latest_block, BlockChain
from src.error.blockchain import DatabaseException, ValidationException
from .consesus_model import ConsensusModel
from ...util.hash import sha256str

DEFAULT_DIFFICULTY = 1
DEFAULT_OUTPUT_TIME_PERIOD = 30 * 1000
DEFAULT_PREVIEW_BLOCK = 10
MAX_TARGET_VALUE = 0x000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF


class CustomPow(ConsensusModel):

    def handle_block(self, raw_block):
        block_json = json.loads(raw_block)
        block = Block(
            previous_hash=block_json['previous_hash'],
            body=block_json['body'],
            height=block_json['height'],
            create_time=block_json['create_time'],
            nonce=block_json['nonce'],
            target_value=block_json['target_value']
        )
        if self.validate_block(block):
            block.save_to_database()
        else:
            raise ValidationException()

    def validate_block(self, block) -> bool:
        latest_block = query_latest_block()
        if latest_block.block_height + 1 != block.height:
            return False
        elif latest_block.current_hash != block.previous_hash:
            return False
        elif sha256str(latest_block.body) != block.get_header()['body_hash']:
            return False
        elif block.get_header_hash() >= self.calculate_target_value():
            return False
        return True

    def make_consensus(self, data, *args, **kwargs):
        block = self.make_block(data)
        kwargs['connector'].broadcast_proposal(block)

    def make_block(self, data):
        while True:
            body = data
            block = query_latest_block()
            if block is None:
                raise DatabaseException()

            block_height = block.block_height + 1
            previous_hash = block.current_hash
            create_time = int(time.time() * 1000)
            target_value = self.calculate_target_value()

            block = Block(previous_hash, body, block_height, create_time, random.random(), target_value)
            header_hash = block.get_header_hash()

            if header_hash < target_value:
                return block

    @staticmethod
    def calculate_difficulty():
        """
        Calculate the difficulty of mining.

        :return:
        """
        query = BlockChain.select().order_by(BlockChain.block_height.desc())

        if len(query) < DEFAULT_PREVIEW_BLOCK:
            return DEFAULT_DIFFICULTY

        offset = len(query) % DEFAULT_PREVIEW_BLOCK
        new_block = query[offset]
        old_block = query[offset + DEFAULT_PREVIEW_BLOCK - 1]

        period = new_block.create_time - old_block.create_time
        difficulty = MAX_TARGET_VALUE / json.loads(new_block.header)['target_value']

        if period / DEFAULT_OUTPUT_TIME_PERIOD > 1:
            return difficulty * 1.1
        elif period / DEFAULT_OUTPUT_TIME_PERIOD < 1:
            return difficulty * 0.9
        else:
            return difficulty

    def calculate_target_value(self):
        """
        Calculate the target value that is used to check whether the block is valid.
        :return:
        """
        difficulty = self.calculate_difficulty()
        return MAX_TARGET_VALUE / difficulty


class Block:
    """
    The data structure for pow algorithm
    """

    def __init__(self, previous_hash, body, height, create_time, nonce, target_value):
        self.body = body
        self.previous_hash = previous_hash
        self.height = height
        self.create_time = create_time
        self.nonce = nonce
        self.target_value = target_value

    def get_header(self):
        return {
            'body_hash': sha256str(self.body),
            'previous_hash': self.previous_hash,
            'height': self.height,
            'create_time': self.create_time,
            'nonce': self.nonce,
            'target_value': self.target_value
        }

    def get_header_hash(self):
        header = self.get_header()

        return int(sha256str(sha256str(json.dumps(header))), 16)

    def save_to_database(self):
        BlockChain.create(
            block_height=self.height,
            current_hash=self.get_block_hash(),
            previous_hash=self.previous_hash,
            create_time=self.create_time,
            header=json.dumps(self.get_header()),
            body=self.body
        )

    def get_block(self):
        block = self.get_header()

        block.update({
            'body': self.body
        })

        return block

    def get_block_hash(self):
        block = self.get_block()

        return sha256str(json.dumps(block))

    def __str__(self):
        return json.dumps(self.get_block())
