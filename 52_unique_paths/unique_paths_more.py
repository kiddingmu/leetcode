class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        result = {}
        for i in xrange(m):
            result[(i, 0)] = 1
        for j in xrange(n):
            result[(0, j)] = 1
        for i in xrange(1, m):
            for j in xrange(1, n):
                result[(i, j)] = result[(i, j-1)] + result[(i-1, j)]
        return result[(m-1, n-1)]
        
if __name__ == "__main__":
    m = 3
    n = 7
    solution = Solution()
    print solution.uniquePaths(m ,n)
