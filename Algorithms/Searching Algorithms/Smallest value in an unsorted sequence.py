#Author:Geraldo Braho
#Data:10/04/2016
#Implementation of the linear search on an unsorted sequence

def findSmallest(theValues):
    n=len(theValues)
#Assume the first item is the smallest value.
    smallest=theValues[0]
#Determine if any other item in the seqence is smaller.
    for i in range(1,n):
        if theList[i]<smallest:
            smallest=theValues[i]
    return smallest #Return the smallest found
