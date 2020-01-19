from concurrent.futures.thread import ThreadPoolExecutor

from src.blockchain.connector.rpc.rpc_client import RPCClient
from src.blockchain.connector.rpc.rpc_server import RPCServer
from src.blockchain.consesus.consesus_model import ConsensusModel
from ..consensus_connector_model import ConsensusConnectorModel


class RPCConnector(ConsensusConnectorModel):

    def __init__(self, consensus: ConsensusModel):
        super().__init__(consensus)
        self.rpc_server = RPCServer(self)
        self.rpc_server.serve()

    def handle_training_request(self, data):
        pass

    def broadcast_proposal(self, block):
        executors = ThreadPoolExecutor(max_workers=2)

        for peer in self.peers:
            client = RPCClient(peer)
            executors.submit(client.send_proposal, block)

    def handle_upload_request(self, data):
        self.consensus.make_consensus(data=data, connector=self)

    def handle_consensus_data(self, data):
        print(data)

        self.consensus.handle_block(data)
