def FindMinimum(array):
        #write your code here
        for i in range(len(array)):
            if i == 0:
                minimum = array[i]
            if(array[i]<minimum):
			minimum = array[i]
 
        return minimum

def FindMax(array):
        #write your code here
        maximum=0
        for i in range(len(array)):
	     	if(array[i]>maximum):
			max = array[i]
        return maximum

def FindAverage(array):
        #write your code here
        average = 0
        sum = 0    
        for i in (array):
         sum = sum + i
         average = float(sum) / len(array)
        return average

list = [2,4,6,8,1,3,5,7]
print "min: ", FindMinimum(list)
print "max: ", FindMaximum(list)
print "average: ", FindAverage(list)



