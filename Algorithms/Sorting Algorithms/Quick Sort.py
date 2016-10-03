#Qucik Sort Sort Algorithms.
#Author: Geraldo Braho
#date:10/03/2016

'''Pivot=> is the item that  we use to compare each number. Sometimes first item is used for pivot but that's not the best choice.
The best choice to choose pivot is somewhere where the pivot can seperate the array in two equal parts.
Quick sort is a recursive (method that calls itself)
Divide and conquer algorithm
Very efficient for large data sets.
Worse case is O(n**2)
Average case is O(n log n )

Performance also depends largely on our pivot selection.



Choosing the median of the first,middle,last as a pivot is another good way, so for this code we will choose the median as a pivot.



def quick_sort(A):
	quick_sort2(A, 0, len(A)-1)
	
def quick_sort2(A, low, hi):
	if hi-low < threshold and low < hi:
		quick_selection(A, low, hi)
	elif low < hi:
		p = partition(A, low, hi)
		quick_sort2(A, low, p - 1)
		quick_sort2(A, p + 1, hi)
	
def get_pivot(A, low, hi):
	mid = (hi + low) // 2
	s = sorted([A[low], A[mid], A[hi]])
	if s[1] == A[low]:
		return low
	elif s[1] == A[mid]:
		return mid
	return hi
	
def partition(A, low, hi):
	pivotIndex = get_pivot(A, low, hi)
	pivotValue = A[pivotIndex]
	A[pivotIndex], A[low] = A[low], A[pivotIndex]
	border = low

	for i in range(low, hi+1):
		if A[i] < pivotValue:
			border += 1
			A[i], A[border] = A[border], A[i]
	A[low], A[border] = A[border], A[low]

	return (border)
	
def quick_selection(x, first, last):
	for i in range (first, last):
		minIndex = i
		for j in range (i+1, last+1):
			if x[j] < x[minIndex]:
				minIndex = j
		if minIndex != i:
			x[i], x[minIndex] = x[minIndex], x[i]
