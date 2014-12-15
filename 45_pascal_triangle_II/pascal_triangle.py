class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            temp = [1,1]
            for i in xrange(2, rowIndex+1):
                for j in xrange(len(temp)-1):
                    temp[j] = temp[j]+temp[j+1]
                temp = [1] + temp[:-1] + [1]
            return temp

if __name__ == "__main__":
    solution = Solution()
    k = 0
    print solution.getRow(k)
