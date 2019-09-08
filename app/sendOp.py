from . import opReturn as op
from time import sleep
import os
import json

dashCliPath = "/home/phillipsw1/Desktop/dashcore-0.14.0/bin/dash-cli "


def sendOpTx(data):
    txid = op.OP_RETURN_store(str.encode(data))['txids'][0]
    return txid


def getOpFromTx(tx):
    tx = getRawTx(tx)
    txDict = json.loads(os.popen(dashCliPath + "decoderawtransaction " + str(tx)).read())
    return txDict["vout"][1]["scriptPubKey"]['asm'].split()[1]


def getRawTx(tx):
    rawTx = os.popen(dashCliPath + "getrawtransaction " + str(tx)).read()
    return rawTx

def getBlockHash(tx):

    t = json.load(os.popen(dashCliPath + "gettransaction " + str(tx)).read())
    return t
