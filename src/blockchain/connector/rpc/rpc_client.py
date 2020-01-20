import grpc

from .interface_pb2_grpc import ConsensusStub
from ....blockchain.connector.rpc.interface_pb2 import Proposal, Batch


class RPCClient:
    def __init__(self, target):
        self.target = target
        channel = grpc.insecure_channel(target)
        self.stub = ConsensusStub(channel)

    def send_proposal(self, block: str):
        # print("sending proposal")
        self.stub.Make_consensus(Proposal(data=block))

    def upload_batch(self, batch_id, data):
        result = self.stub.Upload_batch(Batch(
            batch_id=batch_id,
            data=data
        ))
        print(result)
