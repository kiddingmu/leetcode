class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        prev = num[0]
        for i in xrange(1, len(num)):
            if num[i] < prev:
                return num[i]
            else:
                prev = num[i]
        else:
            return num[0]

if __name__ == "__main__":
    #num = [4,5,6,7,0,1,2]
    num = [7,8,8,9,10,0,1,1,2,3,4,4,5,6]
    solution = Solution()
    print solution.findMin(num)
