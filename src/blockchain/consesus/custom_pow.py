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
        body = sha256str(sha256str(data))

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

    def __init__(self, previous_hash, data):
        self.body_hash = sha256str(sha256str(data))
        self.previous_hash = previous_hash
