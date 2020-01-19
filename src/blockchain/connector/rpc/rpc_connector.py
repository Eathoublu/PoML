from concurrent.futures.thread import ThreadPoolExecutor

from src.blockchain.connector.rpc.rpc_client import RPCClient
from src.blockchain.connector.rpc.rpc_server import RPCServer
from src.blockchain.consesus.consesus_model import ConsensusModel
from ..consensus_connector_model import ConsensusConnectorModel


class RPCConnector(ConsensusConnectorModel):

    def __init__(self, consensus: ConsensusModel, *args, **kwargs):
        super().__init__(consensus)
        self.rpc_server = RPCServer(self)
        self.rpc_server.serve()
        self.executors = ThreadPoolExecutor(max_workers=10)

    def handle_training_request(self, data):
        pass

    def broadcast_proposal(self, data):
        print("begin to broadcast")

        for peer in self.peers:
            client = RPCClient(peer)
            client.send_proposal(data)

    def handle_upload_request(self, data: str):
        print("handling upload request")
        self.executors.submit(self.consensus.make_consensus, data=data, connector=self)

    def handle_consensus_data(self, data):
        print('received proposal')
        self.consensus.handle_block(data)
