class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        if not grid:
            return 0
        row_num = len(grid)
        col_num = len(grid[0])
        result = {}
        for i in xrange(row_num):
            if i == 0:
                result[(i, 0)] = grid[i][0]
            else:
                result[(i, 0)] = grid[i][0] + result[(i-1,0)]
        for j in xrange(col_num):
            if j == 0:
                result[(0, j)] = grid[0][j]
            else:
                result[(0, j)] = grid[0][j] + result[(0, j-1)]
        for i in xrange(1, row_num):
            for j in xrange(1, col_num):
                result[(i,j)] = min(result[(i, j-1)] + grid[i][j], result[(i-1,j)]+grid[i][j])
        return result[(row_num-1, col_num-1)]

if __name__ == "__main__":
    #grid = [[1,2,3],[4,5,6], [7,8,9], [10,11,12]]
    grid = [[1, 2],[1,1]]
    solution = Solution()
    print solution.minPathSum(grid)
