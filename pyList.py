import sys
from random import randrange

array=[]
maxIters=int(sys.argv[1])
for i in range(maxIters):
  randNum = randrange(100000)
  array.append(randNum)
