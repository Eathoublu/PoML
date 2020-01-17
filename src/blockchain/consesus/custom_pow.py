import json
import random
import time

from src.blockchain.persistence.database import query_latest_block, BlockChain
from src.error.blockchain import DatabaseException
from .consesus_model import ConsensusModel
from ..connector import consensus_connector_model
from ...util.hash import sha256str

DEFINE_DIFFICULTY = 1
DEFINE_OUTPUT_PERIOD = 30
DEFINE_PREVIEW_BLOCK = 100
MAX_TARGET_VALUE = 0x00000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF


class CustomPow(ConsensusModel):
    current_difficulty = DEFINE_DIFFICULTY

    def __init__(self, connector: consensus_connector_model):
        super().__init__(connector)

    def handle_block(self, block):
        pass

    def make_consensus(self, data):
        """
        This method is used to make a consensus using pow algorithm.
        This method will take for a long time.
        :param data: the data which will be shared
        :return: the block that shared successfully
        """
        while True:
            block = self.make_block(data)
            header_hash = block.get_herder_hash(random.random())
            if header_hash < self.calculate_target_value():
                return block

    @staticmethod
    def make_block(data):
        """
        Make a block with pow data structure.
        :param data: the body
        :return: the block
        """
        body = sha256str(data)
        block = query_latest_block()
        if block is None:
            raise DatabaseException()

        block_height = block.block_height + 1
        previous_hash = block.previous_hash
        create_time = int(time.time() * 1000)

        return Block(previous_hash, body, block_height, create_time)

    def calculate_difficulty(self):
        """
        Calculate the difficulty of mining.

        :return:
        """
        query = BlockChain.select().order_by(BlockChain.block_height.desc()).limit(DEFINE_PREVIEW_BLOCK)

        if len(query) < DEFINE_PREVIEW_BLOCK:
            return DEFINE_DIFFICULTY

        new_block = query[0]
        old_block = query[len(query) - 1]

        period = new_block.create_time - old_block.create_time

        self.current_difficulty = self.current_difficulty * (period / DEFINE_OUTPUT_PERIOD)

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

    def __init__(self, previous_hash, data, height, create_time):
        self.body = data
        self.previous_hash = previous_hash
        self.height = height
        self.create_time = create_time

    def get_header(self):
        return {
            'body_hash': sha256str(self.body),
            'previous_hash': self.previous_hash,
            'height': self.height,
            'time': self.create_time
        }

    def get_herder_hash(self, nonce):
        return int(sha256str(sha256str(json.dumps(self.get_header().update({"nonce": nonce})))), 16)

    def save_to_database(self):
        BlockChain.create(
            block_height=self.height,
            current_hash=self.get_block_hash(),
            previous_hash=self.previous_hash,
            create_time=self.create_time,
            header=json.dumps(self.get_header()),
            body=self.body
        )

    def get_block_hash(self):
        block = self.get_header()

        block.update({
            'body': self.body
        })

        return sha256str(json.dumps(block))
