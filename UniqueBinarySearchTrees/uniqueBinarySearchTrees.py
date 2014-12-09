#!/usr/bin/python
class Solution:
    # @return an integer
    def numTrees(self, n):
        '''
        /**
         * Solution:
         * DP
         * a BST can be destruct to root, left subtree and right subtree.
         * if the root is fixed, every combination of unique left/right subtrees forms
         * a unique BST.
         * Let a[n] = number of unique BST's given values 1..n, then
         * a[n] = a[0] * a[n-1]     // put 1 at root, 2...n right
         *      + a[1] * a[n-2]     // put 2 at root, 1 left, 3...n right
         *      + ...
         *      + a[n-1] * a[0]     // put n at root, 1...n-1 left
         */
        '''
        if n<0: return 0
        length = n+1
        tmp_list = [0]*length
        tmp_list[0] = 1
        for i in range(1,length):
            for j in range(0,i):
                tmp_list[i] += tmp_list[j] * tmp_list[i-j-1]
        #print tmp_list
        return tmp_list[-1]


        
def test():
    print  Solution().numTrees(3)
if __name__ == '__main__':
    import pdb
    #pdb.set_trace()
    test()
