#Author:Geraldo Braho
#Data:10/04/2016
#Implementation of the binary search algorithm


def binarySearch(theValues,target):
#start with the entire sequence of the elements
    low=0
    high=len(theValues)-1
#repeatedly subdivide the sequence in the half until the target is found
    while low <=high:
#find the midpoint of the sequence
        mid=(high+low)//2
#does the midpoint contains the target ?

        if theValues[mid]==target:
            return True
#or does the target precede the midpoint?
        elif target<theValues[mid]:
            high=mid-1
#or does it follow the midpoint?
        else:
            low=mid+1
#if the sequence cannot be subdivided further we're done.
    return False
