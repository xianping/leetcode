#!/usr/bin/python
class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        '''
            f(n) = f(n-1)+f(n-2)
            from n-1 step one, or from n-2 step two to here
        '''
        array_len = n+1
        tmp_list = [0,1,2]
        if array_len< 4: return tmp_list[n]
        for i in range(3,array_len):
            tmp_list[i%3 ] = tmp_list[(i-2)%3] + tmp_list[(i-1)%3]
        #print tmp_list
        return tmp_list[i%3]
    def climbStairs_v1(self, n):
        '''
            f(n) = f(n-1)+f(n-2)
            from n-1 step one, or from n-2 step two to here
        '''
        array_len = n+1
        tmp_list = [0]*array_len
        tmp_list[0] = 0
        tmp_list[1] = 1
        tmp_list[2] = 2
        for i in range(3,array_len):
            tmp_list[i ] = tmp_list[i-2] + tmp_list[i-1]
        #print tmp_list
        return tmp_list[array_len-1]
            
        
def test():
    result = Solution().climbStairs(5)
    print result
    print  Solution().climbStairs(4)
if __name__ == '__main__':
    import pdb
    #pdb.set_trace()
    test()
