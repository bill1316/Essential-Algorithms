import random
def calc_power(b,p):
       val = b
       for i in range (b,p+1):
          val = val*b
       return val
b=(random.randint(1,10000))
p=(random.randint(1,10000))
numP=calc_power(b,p)
print b,p
print numP
