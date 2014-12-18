# Given a sorted array of integers, find the starting and ending position of a given target value.
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        if not A:
            return [-1, -1]
        start = 0
        end = len(A)-1
        while start <= end:
            mid = start + (end - start)/2
            if A[mid] == target:
                back = mid
                forward = mid
                while back >= start:
                    if A[back] == target:
                        back -= 1
                    else:
                        break
                while  forward <= end:
                    if A[forward] == target:
                        forward += 1
                    else:
                        break
                return [back+1, forward-1]
            elif A[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        else:
            return [-1, -1]

if __name__ == "__main__":
    A = [5, 7, 7, 8, 8, 8, 8, 8, 10]
    target = 8
    solution = Solution()
    print solution.searchRange(A, target)
