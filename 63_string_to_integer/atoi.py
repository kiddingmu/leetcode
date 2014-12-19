class Solution:
    # @return an integer
    def atoi(self, str):
        result = 0
        flag = 1
        start = False
        for i in xrange(len(str)):
            if str[i] == ' ':
                if not start:
                    continue
                else:
                    return result
            elif str[i] == '+':
                if not start:
                    start = True
                else:
                    return 0
            elif str[i] == '-':
                if not start:
                    flag = -1
                    start = True
                elif start or flag == -1:
                    return 0
            elif not str[i].isdigit():
                break
            else:
                start = True
                result = 10*result + int(str[i])
        result = flag * result
        if result >= 2147483648:
            result = 2147483647
        if result < -2147483648:
            result = -2147483648
        return flag * result
        """
        try:
            return int(str)
        except ValueError:
            return 0
        """

if __name__ == "__main__":
    str = "     -0012a42"
    #str = "     010"
    #str = ""
    solution = Solution()
    print solution.atoi(str)
