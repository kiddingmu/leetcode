class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        #s = [x.lower() for x in s if x.isalnum()]
        #return s
        start = 0
        end = len(s)-1
        while start <= end:
            if not s[start].isalnum():
                start += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue
            if s[start].lower() != s[end].lower():
                print start, end
                print s[start], s[end]
                return False
            else:
                print s[start], s[end],(start, end)
                start += 1
                end -= 1
        return True


if __name__ == "__main__":
    #s = "race a car"
    #s = "1a2"
    #s = "A man, a plan, a canal: Panama"
    s = ""
    solution = Solution()
    print solution.isPalindrome(s)
