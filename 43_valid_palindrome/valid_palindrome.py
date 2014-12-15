class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        s = [x.lower() for x in s if x.isalpha() or x.isdigit()]
        size = len(s)
        for i in xrange(size):
            if s[i] != s[size-1-i]:
                return False
        return True

if __name__ == "__main__":
    solution = Solution()
    #s = "A man, a plan, a canal: Panama"
    #s = "race a car"
    #s = "1a2"
    s = "A man a plan, 11a canal: Panama"
    print solution.isPalindrome(s)
