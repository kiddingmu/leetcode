class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        words = s.split()
        return ' '.join(words[::-1])

if __name__ == "__main__":
    solution = Solution()
    #s = "the sky is blue"
    s = ""
    print solution.reverseWords(s)
