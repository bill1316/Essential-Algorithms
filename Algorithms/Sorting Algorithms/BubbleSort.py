#Bubble  Sort Algorithms.
#Author: Geraldo Braho
#date:10/03/2016



def bubbleSort(A):
    for i in range(0,len(A)-1):
        for j in range(0,len(A)-1-i):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]

    return A


my_list=['b','f','c','a','e','m']
print (bubbleSort(my_list))
