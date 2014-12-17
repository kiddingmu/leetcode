class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        if not A:
            return
        start = 0
        end = len(A)-1
        
        while start < end:
            move = False
            while A[start] == 0:
                start += 1
                move = True
            while A[end] == 2:
                end -= 1
                move = True
            if not move:
                if A[start] == 2 or A[end] == 0:
                    move = True
                else:
                    if start+1 == end:
                        end = start+1
                        break
                    for i in range(start+1, end):
                        if A[i] == 0:
                            self.swap(A, i, start)
                            move = True
                        if A[i] == 2:
                            self.swap(A, i, end)
                            move = True
                        if move:
                            break
            if move:
                self.swap(A, start, end)
            else:
                start += 1
                end -= 1

    def swap(self, A, i, j):
        temp = A[i]
        A[i] = A[j]
        A[j] = temp

if __name__ == "__main__":
    A = [0, 1, 2, 1, 0, 1, 2, 0]
    #A = [1, 0, 2, 1]
    #A = [1]
    #A = []
    solution = Solution()
    solution.sortColors(A)
    print A
