///Selection Sort Algorithms.
//Author: Geraldo Braho
//date:10/03/2016

''' With Selection sort first we identify the minimum value(element of the array) and swap it with the first position.
Selection sort is nit a fast sorting algorithm because it uses nested loop to sort.
It is useful for small data set < 10,000.
It runs in O(n**2)'''

def selecion_sort(A):
    for i in range(0,len(A)-1):
        minIndex=i
        for j in range(i+1,len(A)):
            if A[j]<A[minIndex]:
                minIndex=j
            if minIndex !=i:
                A[i],A[minIndex]=A[minIndex],A[i]
                
