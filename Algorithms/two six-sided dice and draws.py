#Write a program that simulates rolling two six-sided dice and draws a bar chart or graph showing the number of times each roll occurs. Compare thenumber of times each value occurs with the number you would expect fortwo fair dice in that many trials. How many trials do you need to performbefore the results fi t the expected distribution well?***

import matplotlib.pyplot as plt
import random
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0

for i in range(10000):
    dice=random.randint(1,6)
    if dice==1:
        count1+=1
    if dice==2:
        count2+=1
    if dice==3:
        count3+=1
    if dice==4:
        count4+=1
    if dice==5:
        count5+=1
    if dice==6:
        count6+=1
print "You entered "+ str(count1)+ " ones, " + str(count2) + " twos, "+str(count3) + " threes, " +str(count4)+ " fours, " +str(count5)+ " fives, and "+str(count6) +" sixes."
count1 = plt.bar( 1,count1, width=1,color='b')
count2= plt.bar( 2,count2,  width=1,color='g')
count3 = plt.bar( 3,count3, width=1, color='r')
count4 = plt.bar( 4,count4,  width=1,color='c')
count5 = plt.bar( 5,count5, width=1, color='m')
count6 = plt.bar( 6,count6, width=1, color='b')
plt.show()
