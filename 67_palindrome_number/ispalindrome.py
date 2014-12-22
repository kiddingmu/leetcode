class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        """
        # Time Limit Exceeded
        palindrom_val = 0
        original = x
        while x:
            palindrom_val = palindrom_val * 10 + x % 10
            x = x / 10
        return palindrom_val == original
        """
        """
        # Accepted
        xstr = str(x)
        xreversed = xstr[::-1]
        return xstr == xreversed
        """
        xstr = str(x)
        size = len(xstr)
        for i in xrange(size/2):
            if xstr[i] != xstr[size-1-i]:
                return False
        else:
            return True

if __name__ == "__main__":
    x = 1001
    solution = Solution()
    print solution.isPalindrome(x)

