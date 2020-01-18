from ..consensus_connector_model import ConsensusConnectorModel


class RPCConnector(ConsensusConnectorModel):

    def handle_training_request(self, data):
        pass

    def broadcast(self, data, target: list):
        pass

    def handle_upload_request(self, data):
        pass

    def __init__(self):
        super().__init__()
