class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        words = s.split()
        if not words:
            return 0
        return len(words[-1])

if __name__ == "__main__":
    #s = "Hello World"
    #s = "hello"
    s = "   "
    solution = Solution()
    print solution.lengthOfLastWord(s)

