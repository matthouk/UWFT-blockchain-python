import subprocess
import json
import os
from dotenv import load_dotenv
from constants import *
load_dotenv()

mnemonic = os.getenv('MNEMONIC-HW')

command = './derive -g --mnemonic=mnemonic --numderive=5 --coin=ETH --cols=path,address,privkey,pubkey --format=json'

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output, err = p.communicate()
p_status = p.wait()

keys = json.loads(output)
print(keys)

# for i in range(5): 
#    print(keys[i]['address'])



# Web3 stuff: 

from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account import Account


from pathlib import Path
from getpass import getpass


# LocalHost stuff here 
3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

account_one = # this is where the "keys" should go 

with open(
    Path(
        "" 
    )
) as keyfile:
    encrypted_key = keyfile.read()
    private_key = w3.eth.account.decrypt(
        encrypted_key, getpass("Enter keystore password: ")
    )
    account_two = Account.from_key(private_key)


# Creating a transaction 
def create_raw_tx(account, recipient, amount):
    gasEstimate = w3.eth.estimateGas(
        {"from": account.address, "to": recipient, "value": amount}
    )
    return {
        "from": account.address,
        "to": recipient,
        "value": amount,
        "gasPrice": w3.eth.gasPrice,
        "gas": gasEstimate,
        "nonce": w3.eth.getTransactionCount(account.address),
    }


#Sending it 
def send_tx(account, recipient, amount):
    tx = create_raw_tx(account, recipient, amount)
    signed_tx = account.sign_transaction(tx)
    result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(result.hex())
    return result.hex()


