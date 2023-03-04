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
from web3 import Web3
import json
from bplib import bp
import secrets
import math



#公共参数
tpN = 75285740785471847697928274317260872220053075039512266400838219410235694454753 # 公共参数
tpE = 65537 # 公钥
tpD = 24421312592250881337416378285711107962134904078804043489873387100470794191149 # 私钥
G = bp.BpGroup()
P = G.gen2()
EV = G.gen2()
w_st_c = {}
tw = G.gen1()
tw = G.pair(tw,P)
r = 0
# tp_stc = []

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
# w3.middleware_onion.inject(geth_poa_middleware, layer=0)
# print(w3.eth.blockNumber)

def keygen():
	sk_du = 1
	# sk_du = secrets.randbelow(10)# sk_du随机整数
	pk_du = P * sk_du
	print(pk_du)
	return sk_du,pk_du

def update(pk_du,op,w,ind,w_st_c):
	global r 
	r = r + 1
	#r = secrets.randbelow(pow(2, 128))
	global EV
	EV = P * r

	if w_st_c.get(w) == None:
		st_0 = 3
		#st_0 = secrets.randbelow(pow(2, 128))# lamda随机生成字符串
		c = 0
	else:
		st_0,c=w_st_c[w]

	#伪随机置换
	k = secrets.randbelow(pow(2, 128))
	st_1 = pow(st_0, tpD, tpN)
	# global tp_stc
	# tp_stc.append(st_1)
	tx_hash=store_var_contract.functions.set_st(str(st_1)[:32].encode()).transact({
		"from": from_account,
		"gas": 3000000,
		"gasPrice": 0,
	})

	# print("st_1",st_1)
	w_st_c[w] = st_1,c+1
	st_1 = str(st_1)[:32].encode()
	add_st = Web3.keccak(st_1)#h1
	temp = Web3.keccak(st_1)#h2
	val_st = bytes(a ^ b for a, b in zip(("1"+str(k)).zfill(32).encode(),temp))#需要填充至32字节
	# print("val_st",val_st)

	EI = Web3.keccak((r * pk_du).export() + w.encode())#H1 大数的hash运算  G->int
	# print("EI    ",EI)
	EI = bytes(a ^ b for a, b in zip(EI,(op+ind).zfill(32).encode()))
	# print("EI    ",EI)
	add_ind = Web3.keccak(st_1)#h3
	temp = Web3.keccak(st_1)#h4
	val_ind = bytes(a ^ b for a, b in zip(temp,EI))

	temp = G.hashG1(w.encode()) #H0 大数的hash运算 byte->G2
	global tw
	tw = G.pair(temp,r * pk_du) 

	add_tw = Web3.keccak(tw.export()) #H2 大数hash G->int 智能合约需要能计算H2
	# print("add_tw",add_tw)
	temp = Web3.keccak(tw.export())
	val_tw = bytes(a ^ b for a, b in zip(temp,st_1)) # H2与H3一致 看作一个hash 是否需要多做一次hash 来保证时间？
	# print(len(temp))
	# print("val_tw",val_tw)
	# print("st",st_1)
	#智能合约上传函数 
	tx_hash=store_var_contract.functions.set_edb(add_st,val_st).transact({
		"from": from_account,
		"gas": 3000000,
		"gasPrice": 0,
	})
	tx_hash=store_var_contract.functions.set_edb(add_ind,val_ind).transact({
		"from": from_account,
		"gas": 3000000,
		"gasPrice": 0,
	})
	tx_hash=store_var_contract.functions.set_edb(add_tw,val_tw).transact({
		"from": from_account,
		"gas": 3000000,
		"gasPrice": 0,
	})

def trapdoor(sk_du,w):
	temp = G.hashG1(w.encode())
	Tw = G.pair(temp*sk_du,EV)
	print("tw与Tw是否相等",G.pair(temp*sk_du,EV)==tw)
	return Tw


def decrypt_mei(sk_du,w,mei):
	i = r
	for Ei in mei:
		EV_temp = i * P
		temp = sk_du * EV_temp
		temp = Web3.keccak(temp.export()+w.encode())# 大数hash 暂时还没确定
		opind = bytes(a ^ b for a, b in zip(temp,Ei))
		print(opind,i)
		i = i - 1
		if i == 0 :
			break
		

#abi
abi_build_index = """
[
	{
		"constant": true,
		"inputs": [
			{
				"internalType": "bytes32",
				"name": "",
				"type": "bytes32"
			}
		],
		"name": "edb",
		"outputs": [
			{
				"internalType": "bytes32",
				"name": "",
				"type": "bytes32"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "mei",
		"outputs": [
			{
				"internalType": "bytes32",
				"name": "",
				"type": "bytes32"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "retrieve0",
		"outputs": [
			{
				"internalType": "bytes32[]",
				"name": "",
				"type": "bytes32[]"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "retrieve1",
		"outputs": [
			{
				"internalType": "bytes32[]",
				"name": "",
				"type": "bytes32[]"
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
				"internalType": "bytes32",
				"name": "tw",
				"type": "bytes32"
			}
		],
		"name": "search",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"internalType": "bytes32",
				"name": "add",
				"type": "bytes32"
			},
			{
				"internalType": "bytes32",
				"name": "val",
				"type": "bytes32"
			}
		],
		"name": "set_edb",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"internalType": "bytes32",
				"name": "val",
				"type": "bytes32"
			}
		],
		"name": "set_st",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "st",
		"outputs": [
			{
				"internalType": "bytes32",
				"name": "",
				"type": "bytes32"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	}
]
"""


# # # # # # # # # # # # # # #
# # # #   连接testrpc   # # #  
# # # # # # # # # # # # # # # 

#随机选取一个账户地址
from_account = w3.toChecksumAddress(w3.eth.accounts[0])
print(w3.eth.accounts[0])
abi_build_index = json.loads(abi_build_index)
#合约地址
store_var_contract = w3.eth.contract(
	address=w3.toChecksumAddress('0x6542307BC52fc9d0Ae180DACd1ACE011202dE2f5'),
	abi=abi_build_index)


sk_du, pk_du = keygen()


update(pk_du,"1op","w","1ind",w_st_c)
update(pk_du,"2op","w","2ind",w_st_c)
update(pk_du,"3op","w","3ind",w_st_c)
update(pk_du,"yang","w","xu",w_st_c)

# print(w_st_c["w"])
Tw = trapdoor(sk_du,"w")




# 搜索
tx_hash=store_var_contract.functions.search(Web3.keccak(Tw.export())).transact({
	"from": from_account,
	"gas": 3000000,
	"gasPrice": 0,
})

#测试
# print("add_tw",Web3.keccak(Tw.export()))
# print("ST_C ",bytes(a ^ b for a, b in zip(Web3.keccak(Tw.export()),val_tw)))
#取值
mei = store_var_contract.functions.retrieve0().call()
# print(mei)
decrypt_mei(sk_du,"w",mei)

