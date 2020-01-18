import os

os.environ["DATABASE_URI"] = "/Users/chenjienan/PycharmProjects/PoML/src/test/testDatabase.db"

import time
import unittest

from src.blockchain.consesus.custom_pow import CustomPow, DEFAULT_DIFFICULTY
from src.blockchain.peer.consensus_peer import ConsensusPeer

from src.blockchain.persistence.database import BlockChain, init_database


class TestCustomPow(unittest.TestCase):
    peer = ConsensusPeer()
    consensus = CustomPow(peer)

    def test_calculate_difficulty_less_blocks(self):
        init_database()
        BlockChain.create(
            block_height=1,
            current_hash='233',
            previous_hash='',
            create_time=int(time.time() * 1000),
            header='2333',
            body='this is the first block'
        )
        self.assertEqual(self.consensus.calculate_difficulty(), DEFAULT_DIFFICULTY)

    def test_mine_one_block(self):
        block = self.consensus.make_block('233')
        block.save_to_database()
        print(block)
        self.assertIsNotNone(block)

    def test_mine_more_blocks(self):
        pass

if __name__ == '__main__':
    unittest.main()
