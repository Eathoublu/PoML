import json
import os
from concurrent import futures

import grpc

from src.blockchain.connector.rpc.interface_pb2 import Result
from .interface_pb2_grpc import ConsensusServicer, add_ConsensusServicer_to_server
from ..consensus_connector_model import ConsensusConnectorModel


class RPCServer(ConsensusServicer):

    def __init__(self, connector: ConsensusConnectorModel):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        self.connector = connector

    def Upload_batch(self, request, context):
        print("receive upload request")
        try:
            self.connector.handle_upload_request(json.dumps({
                'batch_id': request.batch_id,
                'data': request.data
            }))
        except Exception:
            return Result(code=2, description="boom!")
        return Result(code=0, description="ok!")

    def Train(self, request, context):
        pass

    def Fetch_training_result(self, request, context):
        pass

    def Make_consensus(self, request, context):
        block = request.data
        try:
            self.connector.handle_consensus_data(block)
        except Exception:
            return Result(code=2, description="failed to make consensus")

        return Result(code=0)

    def serve(self):
        add_ConsensusServicer_to_server(self, self.server)
        self.server.add_insecure_port("0.0.0.0:" + os.environ.get("port"))
        self.server.start()
