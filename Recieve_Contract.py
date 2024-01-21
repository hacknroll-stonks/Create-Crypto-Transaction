from web3 import Web3, EthereumTesterProvider
import os


def recieveContract(signed):
    w3 = Web3(Web3.WebsocketProvider('wss://eth-sepolia.g.alchemy.com/v2/ph6OA3wr7PivjGt3mmV8nXahcn5tJ2hM'))
    tx_hash = w3.eth.send_raw_transaction(signed)
    tx = w3.eth.get_transaction(tx_hash)
    print(tx)
