from src.blockchain.persistence.data_model import BlockChain
from src.blockchain.persistence.database import db

if __name__ == '__main__':
    db.create_tables([BlockChain])
