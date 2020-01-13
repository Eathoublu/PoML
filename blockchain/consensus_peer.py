from .consesus.consesus_model import ConsensusModel


class ConsensusPeer:


    def __init__(self, consensus: ConsensusModel, peer_list: list):
        self.peer_list = peer_list
        self.consensus = consensus

    def broadcast(self):
        pass
