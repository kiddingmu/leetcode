class Solution:
    # @return an integer
    def numTrees(self, n):
        """
        Taking 1~n as root respectively:
            1 as root: # of trees = F(0) * F(n-1)
            2 as root: # of trees = F(1) * F(n-2)
            3 as root: # of trees = F(2) * F(n-3)
            ...
            n-1 as root: # of trees = F(n-2) * F(1)
            n as root: # of trees = F(n-1) * F(0)
        
        So, the formulation is:
            F(n) = F(0) * F(n-1) + F(1) * F(n-2) + F(2) * F(n-3) + ... + F(n-2) * F(1) + F(n-2) * F(1)
        """
        result = {0:1, 1:1,}
        for i in range(2, n+1):
            result[i] = 0
            for j in range(1, i+1):
                result[i] += result[j-1] * result[i-j]
        #print result
        return result[n]

if __name__ == "__main__":
    solution = Solution()
    n = 3
    print solution.numTrees(n)
