#Merge Sort Algorithms.
#Author: Geraldo Braho
#date:10/03/2016


''' Merge Sort  is recursive(method that calls itself)
Devide and Conquer algorithm.
Very efficient for large data set.
Merge sort does log n merge steps because each merge step doubles the list size
It does n work for each merge step because it must look at every item
So it runs O(n log n).'''



def merge_sort(A):
    merge_sort2(A,0,len(A)-1)

def merge_sort2(A,first,last):
    if first<last:
        middle=(first+last)//2
        merge_sort2(A,first,middle)
        merge_sort2(A,middle+1,last)
        merge(A,first,middle,last)

def merge(A,first,middle,last):
    L=A[first:middle]
    R=A[middle:last+1]
    L.append(999999999)
    R.append(999999999)
    i=j=0
    for k in range(first,last+1):
        if L[i]<=R[j]:
            A[k]=L=[i]
            i+=1
        else:
            A[k]=R[j]
            j+=1
