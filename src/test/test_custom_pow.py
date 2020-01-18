import os

os.environ["DATABASE_URI"] = "/Users/chenjienan/PycharmProjects/PoML/src/test/testDatabase.db"

import time
import unittest

from src.blockchain.consesus.custom_pow import CustomPow, DEFAULT_DIFFICULTY

from src.blockchain.persistence.database import BlockChain, init_database


class TestCustomPow(unittest.TestCase):
    consensus = CustomPow()

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
        for i in range(1000):
            begin_time = time.time()
            print(f'正在挖{i}个块，当前目标值为{self.consensus.calculate_target_value()}')
            block = self.consensus.make_block('233')
            block.save_to_database()
            finish_time = time.time()
            print(f'挖到块了，耗时{finish_time - begin_time}')
            print(block)


if __name__ == '__main__':
    unittest.main()
