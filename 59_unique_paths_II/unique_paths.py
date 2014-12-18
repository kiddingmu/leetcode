class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        result = {}
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        else:
            result[(0,0)] = 1
        rows_num = len(obstacleGrid)
        cols_num = len(obstacleGrid[0])
        for i in xrange(1, rows_num):
            if obstacleGrid[i][0] == 0 and result[(i-1, 0)]:
                result[(i, 0)] = 1
            else:
                result[(i, 0)] = False
        for j in xrange(1, cols_num):
            if obstacleGrid[0][j] == 0 and result[(0, j-1)]:
                result[(0, j)] = 1
            else:
                result[(0, j)] = False
        for i in xrange(1, rows_num):
            for j in xrange(1, cols_num):
                if obstacleGrid[i][j] == 1:
                    result[(i, j)] = False
                else:
                    result[(i,j)] = 0
                    if result[(i-1, j)]:
                       result[(i,j)] += result[(i-1, j)]
                    if result[(i, j-1)]:
                        result[(i,j)] += result[(i, j-1)]
                    if result[(i,j)] == 0:
                        result[(i,j)] = False
        if not result[(rows_num-1,cols_num-1)]:
            return 0
        return result[(rows_num-1, cols_num-1)]


if __name__ == "__main__":
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    solution = Solution()
    print solution.uniquePathsWithObstacles(obstacleGrid)
