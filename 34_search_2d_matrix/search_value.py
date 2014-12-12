class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        for vec in matrix:
            if target >= vec[0] and target <= vec[-1]:
                if self.binary_search(vec, target):
                    return True
                else:
                    return False
        else:
            return False

    def binary_search(self, vector, target):
        left = 0
        right = len(vector)-1
        while left <= right:
            mid = (left + right) / 2
            if vector[mid] > target:
                right = mid - 1
            elif vector[mid] < target:
                left = mid + 1
            else:
                return True
        return False

if __name__ == "__main__":
    solution = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    target = 51
    print solution.searchMatrix(matrix, target)
