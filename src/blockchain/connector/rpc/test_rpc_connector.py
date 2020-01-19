import os
import unittest

from src.blockchain.connector.rpc import RPCConnector
from src.blockchain.connector.rpc.rpc_client import RPCClient
from src.blockchain.consesus.custom_pow import CustomPow


class TestRpcConnector(unittest.TestCase):

    def setUp(self) -> None:
        consensus = CustomPow()
        os.environ['peers'] = '127.0.0.1:2333;127.0.0.1:2334'
        os.environ['port'] = '2333'
        self.connector1 = RPCConnector(consensus)
        os.environ['port'] = '2334'
        self.connector2 = RPCConnector(consensus)

    def test_make_consensus_invalid_input(self):
        for i in range(100):
            self.connector1.broadcast_proposal(str(i))

        input()

    def test_make_consensus_mining(self):
        client1 = RPCClient('127.0.0.1:2333')
        client2 = RPCClient('127.0.0.1:2334')


if __name__ == '__main__':
    unittest.main()
