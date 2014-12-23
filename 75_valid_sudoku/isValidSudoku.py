class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for vec in board:
            result = set()
            for val in vec:
                if val in result and val != '.':
                    return False
                else:
                    result.add(val)
        size = len(board)
        for j in xrange(size):
            result = set()
            for i in xrange(size):
                if board[i][j] in result and board[i][j] != '.':
                    return False
                else:
                    result.add(board[i][j])
        for i in xrange(0,3):
            for k in xrange(0,3):
                result = set()
                for j in xrange(0,3):
                    for t in xrange(0,3):
                        if board[3*i+j][3*k+t] in result and board[3*i+j][3*k+t] != '.':
                            return False
                        else:
                            result.add(board[3*i+j][3*k+t])
        return True


if __name__ == "__main__":
    solution = Solution()
    board = [
            [5,3,'.','.',7,'.','.','.','.'],
            [6,'.','.',1,9,5,'.','.','.'],
            ['.',9,8,'.','.','.','.',6,'.'],
            [8,'.','.','.',6,'.','.','.',3],
            [4,'.','.',8,'.',3,'.','.',1],
            [7,'.','.','.',2,'.','.','.',6],
            ['.',6,'.','.','.','.',2,8,'.'],
            ['.','.','.',4,1,9,'.','.',5],
            ['.','.','.','.',8,'.','.',7,9]
            ]
    #print board[1][0]
    #for vec in board:
    #    print len(vec)
    print solution.isValidSudoku(board)
