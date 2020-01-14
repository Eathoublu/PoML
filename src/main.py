from src.blockchain.persistence.data_model import BlockChain

query = BlockChain.select().limit(100)

print(query[2])
