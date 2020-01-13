from ..consensus_connector_model import ConsensusConnectorModel


class RPCConnector(ConsensusConnectorModel):

    def broadcast(self, data, target: list):
        pass

    def handle_customer_request(self):
        pass

    def __init__(self, peer):
        super().__init__(peer)
