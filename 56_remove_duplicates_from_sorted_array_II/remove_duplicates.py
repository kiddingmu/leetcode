class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        prev = A[0]
        count = 1
        size = len(A)
        i = 1
        while i < size:
            if A[i] == prev:
                if count == 2:
                    del A[i]
                    size -= 1
                    i -= 1
                else:
                    count += 1
            else:
                prev = A[i]
                count = 1
            i += 1
        return len(A)

if __name__ == "__main__":
    solution = Solution()
    A = [1, 1, 1, 2, 2, 3, 3,3,3]
    print solution.removeDuplicates(A)
    print A
