#Bubble  Sort Algorithms.
#Author: Geraldo Braho
#date:10/03/2016

def InsertionSort(list):
    #loop the number of elements in the list
    for i in xrange(1,len(list)):
        #save the value to be positioned
        value=list[i]
        #find the position where the value fits
        #in the ordered part of the list
        pos=i
        #checking conditions
        while pos>0 and value <list[pos-1]:
            #shift the items to the right during search
            list[pos]=list[pos-1]
            pos-=1
        list[pos]=value
    return list

list=[1,4,1234,9,3,7,98,45,12233,8,43,987,10938]
print InsertionSort(list)
