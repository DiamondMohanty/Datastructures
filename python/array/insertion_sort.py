# Implementation of insertion sort
# Author: Diamond Mohanty
# Date: 03-Jan-2022

def insertion_sort(A):
    '''
        Given an array A returns the sorted array A in increasing order
    '''
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] < A[i]:
                temp = A[j]
                k = j
                # Right shiffting the elements
                while k >= i+1:
                    A[k] = A[k-1]
                    k = k - 1
                A[k] = temp

    return A

# Testing code
sample_arr = [2,8,4,1,6]
sample_arr = insertion_sort(sample_arr)
print(sample_arr)