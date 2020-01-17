import os
import time
import unittest

os.environ["DATABASE_URI"] = "/Users/chenjienan/PycharmProjects/PoML/src/test/testDatabase.db"
from src.blockchain.persistence.database import BlockChain, init_database


class MyTestCase(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
