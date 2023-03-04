import numpy as np
import time
import sys
import datetime
import os
from scipy.sparse import csr_matrix
import re
import random
import hmac
import random 
import pickle
from Crypto.Cipher import AES
import json
import string
from web3 import HTTPProvider, Web3
import json
from web3.middleware import geth_poa_middleware
# sys.setrecursionlimit(10000) # 设置递归深度

# w3 = Web3(Web3.WebsocketProvider("ws://127.0.0.1:8545")) # 连接以太坊
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
print(w3.isConnected())


abi_build_index= """
[
	{
		"constant": true,
		"inputs": [],
		"name": "get",
		"outputs": [
			{
				"name": "",
				"type": "int256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "recordtoken",
		"outputs": [
			{
				"name": "",
				"type": "int256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "num",
				"type": "int256"
			}
		],
		"name": "set",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	}
]
"""



from_account = w3.toChecksumAddress(w3.eth.accounts[0])
print(from_account)

abi_build_index = json.loads(abi_build_index)
store_var_contract = w3.eth.contract(
    address=w3.toChecksumAddress('0x6eb95A63b1ba9d662538068a1592A2E517cF29e6'),
#    address=w3.toChecksumAddress('0xae6c81f9ec3f7603B1D909DbD5672a057C07aCB5'),
    abi=abi_build_index)

tx_hash11=store_var_contract.functions.set(1000).transact({
            "from": from_account,
            "gas": 300000,
            "gasPrice": 0,
})



num = store_var_contract.functions.get().call()
print(num)