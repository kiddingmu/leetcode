class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        size = len(A)
        saved = 0
        visited = 1
        count = 1
        while visited < size:
            if A[visited] == A[saved]:
                if count == 1:
                    count += 1
                    saved += 1
                    A[saved] = A[visited]
                else:
                    count += 1
            else:
                saved += 1
                A[saved] = A[visited]
                count = 1
            visited += 1
        return saved+1


if __name__ == "__main__":
    solution = Solution()
    A = [1,1,1,2,2,3,4,4]
    print solution.removeDuplicates(A)
    print A
