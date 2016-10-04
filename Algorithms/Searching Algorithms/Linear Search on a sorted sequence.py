#Author:Geraldo Braho
#Data:10/04/2016
#Implementation on the linear search on a sorted sequence

def sortedLinearSearch(theValues,item):
    n=len(theValuess)
    for i in range(n):
#if the target is found in the ith element,Return True
        if theValues[i]==item:
            return True
#if the target is larger than the ith element, it's not in the sequence.
        elif theValues[i]>item:
            return False

     return False #the item is not in the sequence.
