class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        if m == 1 or n == 1:
            return 1
        else:
            return self.uniquePaths(m, n-1) + self.uniquePaths(m-1, n)

if __name__ == "__main__":
    m = 1
    n = 2
    solution = Solution()
    print solution.uniquePaths(m ,n)
