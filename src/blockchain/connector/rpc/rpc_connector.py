from ..consensus_connector_model import ConsensusConnectorModel


class RPCConnector(ConsensusConnectorModel):

    def handle_training_request(self, data):
        pass

    def broadcast(self, data, target: list):
        pass

    def handle_upload_request(self, data):
        self.peer.handle_upload_request(data)

    def __init__(self, peer):
        super().__init__(peer)
