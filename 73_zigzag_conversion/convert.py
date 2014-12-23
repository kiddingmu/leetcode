class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:
            return s
        result = []
        for i in xrange(nRows):
            result.append([])
        index = 0
        direction = True
        for item in s:
            result[index].append(item)
            if index == 0:
                direction = True
            elif index == nRows-1:
                direction = False
            if direction:
                index += 1
            else:
                index -= 1
        result = reduce(lambda x, y: x + y, result)
        return ''.join(result)

if __name__ == "__main__":
    #s = "PAYPALISHIRING"
    s = "AB"
    n = 1
    solution = Solution()
    print solution.convert(s, n)
