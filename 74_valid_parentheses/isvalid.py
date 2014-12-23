class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        for item in s:
            if not stack or self.match(stack[-1], item) == False:
                stack.append(item)
            else:
                stack.pop()
        if not stack:
            return True
        else:
            return False

    def match(self, a, b):
        if (a, b) == ('(', ')') or (a, b) == ('{', '}') or (a, b) == ('[',']'):
            return True
        else:
            return False


if __name__ == "__main__":
    solution = Solution()
    #s = "()"
    #s = "()[]{}"
    #s = "(]"
    s = "([)]"
    print solution.isValid(s)
