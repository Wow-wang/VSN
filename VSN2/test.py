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
import hmac
import hashlib
import gmpy2
from gmpy2 import mpz
import os
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
readFileDir = "/home/node4/yangxu/ICC20/rangeStreaming/testdata/"

subs = os.listdir(readFileDir)
# 参数
g=mpz(2141434891434191460597654106285009794456474073127443963580690795002163321265105245635441519012876162226508712450114295048769820153232319693432987768769296824615642594321423205772115298200265241761445943720948512138315849294187201773718640619332629679913150151901308086084524597187791163240081868198195818488147354220506153752944012718951076418307414874651394412052849270568833194858516693284043743223341262442918629683831581139666162694560502910458729378169695954926627903314499763149304778624042360661276996520665523643147485282255746183568795735922844808611657078638768875848574571957417538833410931039120067791054495394347033677995566734192953459076978334017849678648355479176605169830149977904762004245805443987117373895433551186090322663122981978369728727863969397652199851244115246624405814648225543311628517631088342627783146899971864519981709070067428217313779897722021674599747260345113463261690421765416396528871227)
p=mpz(3268470001596555685058361448517594259852327289373621024658735136696086397532371469771539343923030165357102680953673099920140531685895962914337283929936606946054169620100988870978124749211273448893822273457310556591818639255714375162549119727203843057453108725240320611822327564102565670538516259921126103868685909602654213513456013263604608261355992328266121535954955860230896921190144484094504405550995009524584190435021785232142953886543340776477964177437292693777245368918022174701350793004000567940200059239843923046609830997768443610635397652600287237380936753914127667182396037677536643969081476599565572030244212618673244188481261912792928641006121759661066004079860474019965998840960514950091456436975501582488835454404626979061889799215263467208398224888341946121760934377719355124007835365528307011851448463147156027381826788422151698720245080057213877012399103133913857496236799905578345362183817511242131464964979)
q=mpz(93911948940456861795388745207400704369329482570245279608597521715921884786973)
S = {}
# AIhex=hex(int(5))
# AIhex=AIhex[2:]
# AItian="0x"+"0"*(768-len(AIhex))+AIhex
# print(AItian)
# AIhex=hex(int(2))
# AIhex=AIhex[2:]
# AItian="0x"+"0"*(768-len(AIhex))+AIhex
# print(AItian)

def fileParser(dir,fileid,dic):
    wordset = []
    wordlist = []
    path = dir+fileid
    with open(path,"r") as f:
        for line in f.readlines():
            wordset = line.split(",")
    # print("fileID",fileid)
    # print(wordset)

    for word in wordset:
        if word not in wordlist:
            wordlist.append(word)
            if word not in dic:
                dic[word] = []
                # dic[word] = [str(fileid).zfill(16)]
                dic[word].append(str(fileid))
                # st=os.urandom(16)    #生成16位byte
                # dic[word].insert(0,st)
            else:
                dic[word].append(str(fileid))


def setup():
	owner_ID='owner1'  # 初始化owner ID
	owner_ID=owner_ID.encode('utf-8') # owner ID 转字节

	owner_key=hmac.new(b'owner').digest() # 生成owner密钥 k_o
	G_o = hmac.new(owner_key, owner_ID, digestmod=hashlib.sha256).digest() # G_o <--- F(k_o, id_o)

	G_o=int.from_bytes(G_o, byteorder='big')  # G_o 转字节

	user_ID='user1' # 初始化user ID
	user_ID=user_ID.encode('utf-8') # user ID 转字节

	user_key_1=hmac.new(b'user_1').digest() # 生成user密钥 k_u_1
	user_key_2=hmac.new(b'user_2').digest() # 生成user密钥 k_u_2 长度16


	G_u_1 = hmac.new(user_key_1, user_ID, digestmod=hashlib.sha256).digest() # G_u_1 <--- F(k_u_1, id_u) 长度32
	G_u_2 = hmac.new(user_key_2, user_ID, digestmod=hashlib.sha256).digest() # G_u_2 <--- F(k_u_2, id_u)
	# print(G_u_1)
	# Gu1_bytes = G_u_1#保证 bytes 格式
	# Gu2_bytes = G_u_2
	G_u_1=int.from_bytes(G_u_1, byteorder='big') # G_u_1 转字节
	G_u_2=int.from_bytes(G_u_2, byteorder='big') # G_u_2 转字节


	# Gu1_bytes = hex(G_u_1)
	# Gu2_bytes = hex(G_u_2)


	temp1 = gmpy2.invert(G_u_2, q) # G_u_2 求逆 
	temp2 = ((mpz(G_o) % q) * (mpz(temp1) % q)) % q 
	AI = gmpy2.powmod(g, temp2, p) # 计算 AI_o->u 925位
	AIhex=hex(int(AI))
	# print("-----------------AI_hex--------------------")
	# print(AIhex)
	# print("-----------------AI_hex_length-------------")
	# print(len(AIhex))
	# AIhex=AIhex[2:]
	# print(AIhex)
	# # print('AI_hex:' , len(AIhex))
	# AItian="0x"+"0"*(768-len(AIhex))+AIhex
	store_var_contract.functions.set_AL(G_u_1,AIhex).transact({#32 384
		"from": from_account,
		"gas": 3000000,
		"gasPrice": 0,
	})
	return G_o,G_u_1,G_u_2



def update(Kw_File_Use,G_o):
	for w in Kw_File_Use.keys():
		# print(type(w))
		kw = w.encode('utf-8') # w转字节
		h = hmac.new(kw).digest() # 计算h <--- H1(w) 长度16
		h = int.from_bytes(h, byteorder='big') # w 转 大数

		temp = ((mpz(h) % q) * (mpz(G_o) % q)) % q
		T = gmpy2.powmod(g, temp, p) # 计算 T <--- g^(h * G_o)
		Thex=hex(int(T))
		# Thex=Thex[2:]
		# Ttian="0x"+"0"*(768-len(Thex))+Thex
		# print(Thex.encode())
		t = Web3.keccak(hexstr=Thex)
		# print(t)
		st_1=hmac.new(b'st_1').digest()#预定义
		for ind in Kw_File_Use[w]:
			# print(ind)
			#对于一个ind
			global S
			if S.get(w) == None:
				st_1=hmac.new(b'st_1').digest()
			else:
				st_1 = S[w]
			#暂时设置的随机性
			st = secrets.randbelow(100)
			st = hmac.new(str(st).encode()).digest()
			S[w] = st
			# print("st_1",w,ind,(("and"+ind).encode()+st_1).zfill(32))
			l = Web3.keccak(st.zfill(32))
			l = Web3.keccak(st.zfill(32))#保证时间
			v1 = ((ind+"and").encode()+st_1).zfill(32)
			print('------------------- v1 -----------------')
			print(v1)
			print('------------------- v1[0] -----------------')
			print(v1[12])
			while(v1[0]!=48):#防止zfill生成错误
				v1 = ((ind+"and").encode()+st_1).zfill(32)
			v = bytes(a ^ b for a,b in zip(l,v1));#异或多少位？用什么加密方法
			
			store_var_contract.functions.set_I(l,v).transact({#32 32
				"from": from_account,
				"gas": 3000000,
				"gasPrice": 0,
			})
		t = Web3.keccak(hexstr=Thex)#测时间专用
		P = bytes(a ^ b for a,b in zip(t,st.zfill(32)))#st 而不是 st_1
		
		store_var_contract.functions.set_I(t,P).transact({#32 32
			"from": from_account,
			"gas": 3000000,
			"gasPrice": 0,
		})

def search(w,G_u_1,G_u_2):
	#与update H1保持一致
	w = w.encode('utf-8')
	h = hmac.new(w).digest()
	h = int.from_bytes(h, byteorder='big') # w 转大数
	# G_u_2=int.from_bytes(G_u_2, byteorder='big') # G_u_2 转 大数
	tk = ((mpz(h) % q) * (mpz(G_u_2) % q)) % q # 计算tk <--h *G_u_2
	tk=int(tk)
	# print(tk)
	# print("hhhhhhhhhhhhhhhhhhhh")
	tx = store_var_contract.functions.search(G_u_1,tk).transact({
		"from": from_account,
		"gas": 5000000,
		"gasPrice": 0,
	})
	result = store_var_contract.functions.retrieve0().call()
	print(result)
	# result = store_var_contract.functions.retrieve1().call()
	# print("上一个st",result)
	# result = store_var_contract.functions.retrieve2().call()
	# print(result)
	# result = store_var_contract.functions.retrieve3().call()
	# print("本次st",result)

abi_build_index = """
[
	{
		"constant": false,
		"inputs": [
			{
				"name": "add",
				"type": "uint256"
			},
			{
				"name": "val",
				"type": "bytes"
			}
		],
		"name": "set_AL",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "result1",
		"outputs": [
			{
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
				"name": "",
				"type": "bytes13[]"
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
				"name": "",
				"type": "uint256"
			}
		],
		"name": "AL",
		"outputs": [
			{
				"name": "",
				"type": "bytes"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "pp",
		"outputs": [
			{
				"name": "",
				"type": "bytes"
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
				"name": "g",
				"type": "bytes"
			},
			{
				"name": "x",
				"type": "uint256"
			},
			{
				"name": "p",
				"type": "bytes"
			}
		],
		"name": "expmod",
		"outputs": [
			{
				"name": "",
				"type": "bytes"
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
				"name": "",
				"type": "bytes32"
			}
		],
		"name": "I",
		"outputs": [
			{
				"name": "",
				"type": "bytes32"
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
				"name": "G_u_1",
				"type": "uint256"
			},
			{
				"name": "tk",
				"type": "uint256"
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
				"name": "add",
				"type": "bytes32"
			},
			{
				"name": "val",
				"type": "bytes32"
			}
		],
		"name": "set_I",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"name": "R",
		"outputs": [
			{
				"name": "",
				"type": "bytes13"
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
	address=w3.toChecksumAddress('0x867203f9BE162eD53E278e7CC4Bc72a43780d4bB'),
	abi=abi_build_index)

# phex = hex(int(p))
# print(q)
# phex=phex[2:]
# ptian="0x"+"0"*(768-len(phex))+phex
# store_var_contract.functions.setP(ptian.encode()).transact({
# 	"from": from_account,
# 	"gas": 3000000,
# 	"gasPrice": 0,
# })

Kw_File_Use ={}
for sub in subs:
	# print(sub)
	fileParser(readFileDir,sub,Kw_File_Use)
print(Kw_File_Use)


# phex = hex(int(p))
# print(phex)
G_o,G_u_1,G_u_2= setup()
# print("-----------------G_u_1--------------------")
# print(G_u_1)

update(Kw_File_Use,G_o)


#####################
# result = store_var_contract.functions.retrieve_g_length(G_u_1).call()
# print("-----------------AI from Solidity--------------------")
# print(result)
# result = store_var_contract.functions.retrieve_p_length().call()
# print(result)


########################

search("a",G_u_1,G_u_2)


	








