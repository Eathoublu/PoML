import time

from src.blockchain.connector.rpc.rpc_client import RPCClient

for j in range(1000):
    for i in [1234, 1235, 1236, 1237, 1238]:
        client = RPCClient(f'127.0.0.1:{i}')
        client.upload_batch("2333", f"lalala{j}")
    time.sleep(30)
input()
