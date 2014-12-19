#!/usr/bin/python
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        '''
        record the current i before, minimum element,
        diff with current i to calc profit may have
        '''
        if len(prices) < 2: return 0

        profit = 0
        min_price = prices[0]
        for i in range(1,len(prices)):
            cur_profit = prices[i] - min_price 
            if cur_profit > profit:
                profit = cur_profit
            if prices[i] < min_price:
                min_price = prices[i]
        return profit

        
if __name__ == '__main__':
    import pdb
    #pdb.set_trace()
    print  Solution().maxProfit([10,2,3,5,8,6])
