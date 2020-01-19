import os
import time

os.environ.setdefault('DATABASE_URI', 'src/database.db')
os.environ.setdefault('port', '2333')
os.environ.setdefault('peers', '127.0.0.1:2333')

from src.blockchain.connector.rpc import RPCConnector
from src.blockchain.consesus.custom_pow import CustomPow

if __name__ == '__main__':

    consensus = CustomPow()
    connector = RPCConnector(consensus)
    print("start working")
    while True:
        time.sleep(0.5)
