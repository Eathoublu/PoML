import os
import time
from concurrent.futures.thread import ThreadPoolExecutor

os.environ["DATABASE_URI"] = "/Users/chenjienan/PycharmProjects/PoML/src/test/testDatabase.db"

import unittest

from ..blockchain.connector.rpc import RPCConnector
from ..blockchain.connector.rpc.rpc_client import RPCClient
from ..blockchain.consesus.custom_pow import CustomPow


class TestRpcConnector(unittest.TestCase):
    executors = ThreadPoolExecutor(max_workers=10)

    def setUp(self) -> None:
        consensus1 = CustomPow()
        consensus2 = CustomPow()
        os.environ['peers'] = '127.0.0.1:2333;127.0.0.1:2334'
        os.environ['port'] = '2333'
        self.connector1 = RPCConnector(consensus1)
        os.environ['port'] = '2334'
        self.connector2 = RPCConnector(consensus2)

    def test_make_consensus_invalid_input(self):
        for i in range(100):
            self.connector1.broadcast_proposal(str(i))

        input()

    def test_make_consensus_valid_input(self):
        self.connector1.handle_consensus_data()
        input()

    def test_make_consensus_mining(self):
        for j in range(1000):
            for i in [1234, 1235, 1236, 1237, 1238]:
                client = RPCClient(f'127.0.0.1:{i}')
                client.upload_batch("2333", f"lalala{j}")
            time.sleep(30)
        input()

    def test_exist(self):
        client1 = RPCClient('127.0.0.1:1234')
        client1.send_proposal("2333")


if __name__ == '__main__':
    unittest.main()
