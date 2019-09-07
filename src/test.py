import sys
import os
inp1 = str(sys.argv[1])
# inp2 = str(sys.argv[2])
# inp3 = sys.argv[3]
# inp4 = sys.argv[4]


def thing1(a = inp1):

    print(thing2(a))

def thing2(thing):
    os.popen("pwd", shell=True)

thing1()