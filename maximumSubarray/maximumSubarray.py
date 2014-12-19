#!/usr/bin/python
#coding:utf-8
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        def mymax(x,y): 
            if x>y: return x
            return y
        m = A[0]
        sum = [0]*len(A)
        sum[0] = A[0]
        for i,value in enumerate(A):
            if i == 0:
                continue
            sum[i] = mymax(value, sum[i-1] + value)
            m = mymax(m,sum[i])
        return m
    def maxSubArray_v2(self, A):
        if(A[0] > 0):
            thisSum = A[0]
        else:
            thisSum = 0
        maxSum = A[0]
        
        for num in A[1:]:
            thisSum += num
            
            if thisSum > maxSum:
                maxSum = thisSum
            
            if thisSum < 0:
                thisSum = 0
        
        return maxSum
if __name__ == '__main__':
    import pdb
    #pdb.set_trace()
    A = [-2,1,-3,4,-1,2,1,-5,4]
    print Solution().maxSubArray(A)
