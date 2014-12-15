class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        if not num:
            return None
        min_num = num[0]
        for i in xrange(1, len(num)):
            if num[i] - num[i-1] < 0:
                return num[i]
        return min_num

if __name__ == "__main__":
    solution = Solution()
    num = [4,5,6,7,0,1,2]
    print solution.findMin(num)
