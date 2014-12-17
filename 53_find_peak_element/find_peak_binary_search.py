class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        size = len(num)
        fixed_num = [-2147483649] + num + [-2147483649]
        start = 1
        end = size
        while start <= end:
            mid = start + (end - start) / 2
            if fixed_num[mid] > fixed_num[mid-1] and fixed_num[mid] > fixed_num[mid+1]:
                return mid-1
            elif fixed_num[mid] < fixed_num[mid+1]:
                start = mid+1
            elif fixed_num[mid] < fixed_num[mid-1]:
                end = mid-1

if __name__ == "__main__":
    num = [10,1,2,3,1]
    #num = [10]
    #num = [-2147483648]
    solution = Solution()
    print solution.findPeakElement(num)
