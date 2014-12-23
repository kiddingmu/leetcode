class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        size = len(A)
        maxpos = 0
        for i in xrange(size):
            if maxpos >= i and i + A[i] > maxpos:
                maxpos = i+A[i]
        return maxpos >= size-1

if __name__ == "__main__":
    #A = [2,3,1,1,4]
    A = [3,2,1,0,4]
    #A = [2, 0]
    #A = [2,5,0,0]
    solution = Solution()
    print solution.canJump(A)
