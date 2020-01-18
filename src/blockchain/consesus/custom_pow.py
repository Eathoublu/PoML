import json
import random
import time

from src.blockchain.peer.consensus_peer import ConsensusPeer
from src.blockchain.persistence.database import query_latest_block, BlockChain
from src.error.blockchain import DatabaseException
from .consesus_model import ConsensusModel
from ...util.hash import sha256str

DEFAULT_DIFFICULTY = 1
DEFAULT_OUTPUT_PERIOD = 30
DEFAULT_PREVIEW_BLOCK = 100
MAX_TARGET_VALUE = 0x000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF


class CustomPow(ConsensusModel):
    current_difficulty = DEFAULT_DIFFICULTY

    def __init__(self, peer: ConsensusPeer):
        super().__init__(peer)

    def handle_block(self, block):
        pass

    def make_consensus(self, data):
        block = self.make_block(data)
        BlockChain.create(
            block_height=block.height,
            current_hash=block.get_block_hash(),
            previous_hash=block.previous_hash,
            create_time=block.create_time,
            header=block.get_header(),
            body=block.body
        )

    def make_block(self, data):
        while True:
            body = data
            block = query_latest_block()
            if block is None:
                raise DatabaseException()

            block_height = block.block_height + 1
            previous_hash = block.current_hash
            create_time = int(time.time() * 1000)

            block = Block(previous_hash, body, block_height, create_time, random.random())
            header_hash = block.get_header_hash()
            target_value = self.calculate_target_value()

            if header_hash < target_value:
                return block

    def calculate_difficulty(self):
        """
        Calculate the difficulty of mining.

        :return:
        """
        query = BlockChain.select().order_by(BlockChain.block_height.desc()).limit(DEFAULT_PREVIEW_BLOCK)

        if len(query) < DEFAULT_PREVIEW_BLOCK:
            return DEFAULT_DIFFICULTY

        new_block = query[0]
        old_block = query[len(query) - 1]

        period = new_block.create_time - old_block.create_time

        self.current_difficulty = self.current_difficulty * (period / DEFAULT_OUTPUT_PERIOD)

    def calculate_target_value(self):
        """
        Calculate the target value that is used to check whether the block is valid.
        :return:
        """
        self.calculate_difficulty()
        return MAX_TARGET_VALUE / self.current_difficulty


class Block:
    """
    The data structure for pow algorithm
    """

    def __init__(self, previous_hash, data, height, create_time, nonce):
        self.body = data
        self.previous_hash = previous_hash
        self.height = height
        self.create_time = create_time
        self.nonce = nonce

    def get_header(self):
        return {
            'body_hash': sha256str(self.body),
            'previous_hash': self.previous_hash,
            'height': self.height,
            'create_time': self.create_time,
            'nonce': self.nonce
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
