# coding=utf8
from collections import Counter

"""
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
"""

# create a set of digits seen in each row,
# column and box. False if any duplicates.


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        size = 9
        digits = {str(i) for i in range(1, 10)}
        rows = [set() for _ in range(size)]
        cols = [set() for _ in range(size)]
        boxes = [set() for _ in range(size)]

        for r in range(size):
            for c in range(size):

                digit = board[r][c]
                if digit == '.':
                    continue

                if digit not in digits:
                    return False

                box = (size//3) * (r//(size//3)) + (c//(size//3))
                if digit in rows[r] or digit in cols[c] or digit in boxes[box]:
                    return False
                rows[r].add(digit)
                cols[c].add(digit)
                boxes[box].add(digit)

        return True


board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
a = Solution()
print a.isValidSudoku(board)
            