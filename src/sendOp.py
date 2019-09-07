import opReturn as op
from time import sleep
import os
import json
import sys


command = sys.argv[1]
arg1 = sys.argv[2]
dashCliPath = "/home/nova/Desktop/apps/dash/dashcore-0.14.0/bin/dash-cli "


def sendOp(data=arg1):
    txid = op.OP_RETURN_store(str.encode(data))['txids'][0]
    sleep(2)
    print(txid)


def getOpFromTx(tx=arg1):
    tx = getRawTx(tx)
    txDict = json.loads(os.popen(dashCliPath + "decoderawtransaction " + str(tx)).read())
    print(txDict["vout"][1]["scriptPubKey"]['asm'].split()[1])


def getRawTx(tx):
    rawTx = os.popen(dashCliPath + "getrawtransaction " + str(tx)).read()
    return rawTx


if command == "sendOpReturn":
    sendOp(arg1)

if command == "getOpFromTx":
    getOpFromTx(arg1)
print("hello")
# print(getOpFromTx(sendOp("hello")))

