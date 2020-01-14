from .consesus_model import ConsensusModel
from ..connector import consensus_connector_model


class CustomPow(ConsensusModel):

    def __init__(self, connector: consensus_connector_model):
        super().__init__(connector)

    def handle_block(self, block):
        pass

    def verify_block(self, block):
        pass

    def make_consensus(self, data):
        pass

    def make_block(self):
        pass

    def calculate_difficulty(self):
        pass
