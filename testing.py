from src import opReturn
from time import sleep
import os
import json


dashCliPath = "/home/nova/Desktop/apps/dash/dashcore-0.14.0/bin/dash-cli "
#print(OP_RETURN.OP_RETURN_send("yLU43aF46rhPctw1afe5vrtDt3jPRWqTt5", 0.00001, "hello world"))
tx = OP_RETURN.OP_RETURN_store(b"hello")['txids'][0]
#print(tx)
sleep(.5)
tx = os.popen(dashCliPath + "gettransaction " + str(tx)).read()
tx = json.loads(tx)
print(tx["hex"])