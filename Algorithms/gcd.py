import random
import matplotlib.pyplot as plt
average = 0.0
def GCD(a, b):
    average=float((a+b)/2)
    count=0
    while (b != 0):
        remainder  = a % b
        a = b
        b = remainder
        count+=1
    return count

gcd_values = GCD(random.randint(1,10000),random.randint(1,10000))
print "It takes " +str(gcd_values) +  " steps to find the GCD"
gcdSteps = plt.bar(1,gcd_values, width=0.3,color='c',label="gcd steps")
averageSteps = plt.bar(2,1,width=0.3,color='m',label="average")
plt.show()
