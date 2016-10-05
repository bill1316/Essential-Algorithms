#Bubble  Sort Algorithms.
#Author: Geraldo Braho
#date:10/03/2016

'''Insertion sort is not a fast sorting algorithm, because it uses nested loops to sort.
It is useful only for small data set.
It runs O(n**2)'''



#1.Using for loop to sort
def insertion_sort(A):
    for i in range(1,len(A)):
        for j in range(i-1,0,-1):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
            else:
                break


#2.Using while loop to sort which is more cleaner

def insertion_sort(A):
    for i in range(1,len(A)):
        j=i-1
        while A[j]>A[j+1] and j>=0:
            A[j],A[j+1]=A[j+1],A[j]
            j-=1



'''Shifting elements of the array is two times faster then swapping them'''
#1.Optimized
def insertion_sort(A):
    for i in range(1,len(A)):
        curNum=A[i]
        for j in range(i-1,0,-1):
            if A[j]>curNum:
                A[j+1]=A[j]
            else:
                A[j+1]=curNum
                break
