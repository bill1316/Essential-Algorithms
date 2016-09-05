#Write a program that simulates rolling two six-sided dice and draws a bar chart or graph showing the number of times each roll occurs. Compare thenumber of times each value occurs with the number you would expect fortwo fair dice in that many trials. How many trials do you need to performbefore the results fi t the expected distribution well?***

import matplotlib.pyplot as plt
import random
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
count1_2=0
count2_2=0
count3_2=0
count4_2=0
count5_2=0
count6_2=0


for i in range(10000):
    dice1=random.randint(1,6)
    if dice1==1:
        count1+=1
    if dice1==2:
        count2+=1
    if dice1==3:
        count3+=1
    if dice1==4:
        count4+=1
    if dice1==5:
        count5+=1
    if dice1==6:
        count6+=1
for i in range(10000):
    dice2=random.randint(1,6)
    if dice2==1:
        count1_2+=1
    if dice2==2:
        count2_2+=1
    if dice2==3:
        count3_2+=1
    if dice2==4:
        count4_2+=1
    if dice2==5:
        count5_2+=1
    if dice2==6:
        count6_2+=1
print "You entered from first dice  "+ str(count1)+ " ones, " + str(count2) + " twos, "+str(count3) + " threes, " +str(count4)+ " fours, " +str(count5)+ " fives, and "+str(count6) +" sixes."
count1 = plt.bar( 1,count1, width=0.3,color='b',label='dice 1 ')
count2= plt.bar( 2,count2,  width=0.3,color='b',label='dice 1 ')
count3 = plt.bar( 3,count3, width=0.3, color='b',label='dice 1 ')
count4 = plt.bar( 4,count4,  width=0.3,color='b',label='dice 1 ')
count5 = plt.bar( 5,count5, width=0.3, color='b',label='dice 1 ')
count6 = plt.bar( 6,count6, width=0.3, color='b',label='dice 1 ')
plt.show()
print "You entered from second dice "+ str(count1_2)+ " ones, " + str(count2_2) + " twos, "+str(count3_2) + " threes, " +str(count4_2)+ " fours, " +str(count5_2)+ " fives, and "+str(count6_2) +" sixes."
count1_2 = plt.bar( 1,count1_2, width=0.3,color='c',label='dice 2')
count2_2= plt.bar( 2,count2_2,  width=0.3,color='c',label='dice 2')
count3_2 = plt.bar( 3,count3_2, width=0.3, color='c',label='dice 2')
count4_2 = plt.bar( 4,count4_2,  width=0.3,color='c',label='dice 2')
count5_2 = plt.bar( 5,count5_2, width=0.3, color='c',label='dice 2')
count6_2 = plt.bar( 6,count6_2, width=0.3, color='c',label='dice 2')
plt.show()
