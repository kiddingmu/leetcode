class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        return self.reverseNum(x) == x

    def reverseNum(self, n, partial=0):
        if n == 0:
            return partial
        return self.reverseNum(n/10, partial*10+n%10)

if __name__ == "__main__":
    solution = Solution()
    x = 10001
    print solution.isPalindrome(x)
