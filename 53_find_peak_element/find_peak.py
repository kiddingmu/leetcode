class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        size = len(num)
        fixed_num = [-2147483649] + num + [-2147483649]
        for i in xrange(1, size+1):
            peak = fixed_num[i]
            if peak > fixed_num[i-1] and peak > fixed_num[i+1]:
                return i-1

if __name__ == "__main__":
    num = [10, 1,2,3,1]
    solution = Solution()
    print solution.findPeakElement(num)
