from .interface_pb2_grpc import ConsensusServicer
from ..consensus_connector_model import ConsensusConnectorModel


class RPCServer(ConsensusServicer):

    def __init__(self, connector: ConsensusConnectorModel):
        self.connector = connector

    def Upload_batch(self, request, context):
        self.connector.handle_upload_request(4)

    def Train(self, request, context):
        pass

    def Fetch_training_result(self, request, context):
        pass
