from web3 import Web3, EthereumTesterProvider
import os
import segno

def signContract(to, value, privateKey):
    w3 = Web3(Web3.WebsocketProvider('wss://eth-sepolia.g.alchemy.com/v2/' + os.environ["Alchemy_API"]))
    acct = w3.eth.account.from_key(privateKey)
    value = value*(10**18)
    contract = {
        "from": acct.address,
        "to": to,
        'gas': 21000,
        'maxFeePerGas': 2000000000,
        'maxPriorityFeePerGas': 1000000000,
        "nonce": w3.eth.get_transaction_count(acct.address),
        'chainId': 11155111,
        "value": int(value)
    }
    # 2. Sign tx with a private key
    signed = w3.eth.account.sign_transaction(contract, privateKey)
    print(f"Raw tx: {signed.rawTransaction.hex()}")

    segno.make_qr(signed.rawTransaction).save("Transaction_QR_Code.png", scale = 100)
    return signed.rawTransaction


