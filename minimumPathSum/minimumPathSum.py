#!/usr/bin/python
class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        m =len(grid)  
        if m == 0: return 0
        n = len(grid[0])
        if n == 0: return 0

        dp_list = list()
        for i in range(0,m):
            tmp_list = list()
            for j in range(0,n):
                tmp_list.append(0)
            dp_list.append(tmp_list)
        for i in range(0,m):
            for j in range(0,n):
                if i==0 and j ==0: dp_list[i][j] = grid[i][j]
                elif i==0: dp_list[i][j] = dp_list[i][j-1] + grid[i][j]
                elif j==0: dp_list[i][j] = dp_list[i-1][j] + grid[i][j]
                else:
                    dp_list[i][j] = min(dp_list[i][j-1],dp_list[i-1][j]) + grid[i][j]
        #print dp_list
        return dp_list[-1][-1]

if __name__ == '__main__':
    import pdb
    #pdb.set_trace()
    grid = [[7,2],[6,6],[8,6],[8,7],[5,0],[6,0]]
    print Solution().minPathSum(grid)
