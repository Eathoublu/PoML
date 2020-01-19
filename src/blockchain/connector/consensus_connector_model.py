import os
from abc import abstractmethod

from src.blockchain.consesus.consesus_model import ConsensusModel


class ConsensusConnectorModel:
    """
    this abstract class define the method of the connector
    
    """

    def __init__(self, consensus: ConsensusModel):
        self.peers = str(os.environ['peers']).split(";")
        self.consensus = consensus

    @abstractmethod
    def broadcast_proposal(self, data):
        """
        broadcast the data to all peers
        :param data:
        :param target:
        """
        pass

    @abstractmethod
    def handle_training_request(self, data):
        pass

    @abstractmethod
    def handle_upload_request(self, data):
        pass

    @abstractmethod
    def handle_consensus_data(self, data):
        pass
