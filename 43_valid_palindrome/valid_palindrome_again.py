class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        s = [x.lower() for x in s if x.isalpha() or x.isdigit()]
        str1 = ''.join(s)
        str2 = str1[::-1]
        if str1 == str2:
            return True
        else:
            return False

if __name__ == "__main__":
    solution = Solution()
    s = "A man, a plan, a canal: Panama"
    #s = "race a car"
    #s = "1a2"
    #s = "A man a plan, 11a canal: Panama"
    print solution.isPalindrome(s)
