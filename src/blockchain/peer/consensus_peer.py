from src.blockchain.connector.consensus_connector_model import ConsensusConnectorModel
from src.blockchain.consesus.consesus_model import ConsensusModel


class ConsensusPeer:

    def __init__(self, consensus: ConsensusModel, connector: ConsensusConnectorModel, peer_list: list):
        self.peer_list = peer_list
        self.consensus = consensus
        self.connector = connector

    def broadcast(self, data):
        self.connector.broadcast(data, self.peer_list)

    def handle_training_request(self, data):
        pass

    def handle_upload_request(self, data):
        pass
