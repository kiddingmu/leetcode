class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeros(self, matrix):
        row = set()
        col = set()
        row_size = len(matrix)
        col_size = len(matrix[0])
        for i in range(row_size):
            for j in range(col_size):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        for i in range(row_size):
            for j in range(col_size):
                if i in row or j in col:
                    matrix[i][j] = 0


if __name__ == "__main__":
    solution = Solution()
    #matrix = [[1,2,3,4], [2,0,3,1], [1,1,2,0], [1,1,1,2]]
    matrix = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
    #matrix = [[0], [1]]
    solution.setZeros(matrix)
    print matrix
