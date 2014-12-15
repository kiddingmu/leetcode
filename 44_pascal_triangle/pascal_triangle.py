class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        result = []
        for n in xrange(0, numRows):
            if n == 0:
                result.append([1])
            elif n == 1:
                result.append([1, 1])
            else:
                base = result[n-1]
                cur_temp = []
                for i in xrange(len(base)-1):
                    cur_temp.append(base[i]+base[i+1])
                temp = [1,] + cur_temp+[1]
                result.append(temp)
        return result

if __name__ == "__main__":
    solution = Solution()
    nRows = 6
    print solution.generate(nRows)
