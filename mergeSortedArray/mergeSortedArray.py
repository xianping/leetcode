#Given two sorted integer arrays A and B, merge B into A as one sorted array.

#Note:
#You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.

#Hide Tags Array Two Pointers

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        #tmp = [0 for i in range(m + n)]
        tmp = [0]*(m+n)
        i = 0; j = 0; k = 0
        while i < m and j < n:
            if A[i] <= B[j]:
                tmp[k] = A[i]; i += 1
            else:
                tmp[k] = B[j]; j += 1
            k += 1
        if i == m:
            while k < m + n:
                tmp[k] = B[j]; k += 1; j += 1
        else:
            while k < m + n:
                tmp[k] = A[i]; i += 1; k += 1
        for i in range(0, m + n):
            A[i] = tmp[i]
