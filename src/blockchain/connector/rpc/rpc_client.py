import grpc

from src.blockchain.connector.rpc.interface_pb2 import Proposal
from .interface_pb2_grpc import ConsensusStub


class RPCClient:
    def __init__(self, target):
        channel = grpc.insecure_channel(target)
        self.stub = ConsensusStub(channel)

    def send_proposal(self, block):
        result = self.stub.Make_consensus(Proposal(data=block))
        print(result)

    def upload_batch(self):
        result = self.stub.Upload_batch()
