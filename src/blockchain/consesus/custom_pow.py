import json
import time

from src.blockchain.persistence.database import query_latest_block
from src.error.blockchain import DatabaseException
from .consesus_model import ConsensusModel
from ..connector import consensus_connector_model
from ..persistence.data_model import BlockChain
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

    def verify_block(self, block):
        pass

    def make_consensus(self, data):
        pass

    def make_block(self, data):
        body = sha256str(data)
        block = query_latest_block()
        if block is None:
            raise DatabaseException()

        block_height = block.block_height + 1
        previous_hash = block.previous_hash
        create_time = int(time.time() * 1000)

        block = Block(previous_hash, data, block_height, create_time)
        pass

    def calculate_difficulty(self):
        query = BlockChain.select().order_by(BlockChain.block_height.desc()).limit(DEFINE_PREVIEW_BLOCK)

        if len(query) < DEFINE_PREVIEW_BLOCK:
            return DEFINE_DIFFICULTY

        new_block = query[0]
        old_block = query[len(query) - 1]

        period = new_block.create_time - old_block.create_time

        self.current_difficulty = self.current_difficulty * (period / DEFINE_OUTPUT_PERIOD)

    def calculate_target_value(self):
        return MAX_TARGET_VALUE / self.current_difficulty


class Block:

    def __init__(self, previous_hash, data, height, time):
        self.body_hash = sha256str(data)
        self.previous_hash = previous_hash
        self.height = height
        self.time = time

    def get_header(self):
        return {
            'body_hash': self.body_hash,
            'previous_hash': self.previous_hash,
            'height': self.height,
            'time': self.time
        }

    def get_herder_hash(self, nonce):
        return int(sha256str(sha256str(json.dumps(self.get_header().update({"nonce": nonce})))), 16)
