from src import OP_RETURN
from time import sleep
import subprocess
import ast


dashCliPath = "/home/nova/Desktop/apps/dash/dashcore-0.14.0/bin/dash-cli "
#print(OP_RETURN.OP_RETURN_send("yLU43aF46rhPctw1afe5vrtDt3jPRWqTt5", 0.00001, "hello world"))
tx = OP_RETURN.OP_RETURN_store(b"hello")['txids'][0]
#print(tx)
sleep(.5)
tx = subprocess.check_output(dashCliPath + "gettransaction " + str(tx), shell=True)
print(ast.literal_eval(tx.decode('utf-8')))
#print(type(tx))
