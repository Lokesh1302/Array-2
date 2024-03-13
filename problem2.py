# https://leetcode.com/problems/game-of-life/

# Time Complexity : O(M x N) where M is number of rows and N is number of columns
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : None


# Your code here along with comments explaining your approach in three sentences only
# Approach : We have to mark the elements which will change by iterating it first. Then change all the values
# in the next iteration.

from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        dirX = [0, 0, 1, -1, -1, -1, 1, 1]
        dirY = [-1, 1, 0, 0, 1, -1, 1, -1]
        for r in range(row):
            for c in range(col):
                flag = 1
                if board[r][c] == 0:
                    flag = -1
                count = 0
                for i in range(8):
                    new_r = r + dirX[i]
                    new_c = c + dirY[i]
                    if new_r >= 0 and new_c >= 0 and new_r < row and new_c < col and board[new_r][new_c] > 0:
                        count = count + 1
                if count == 0 and board[r][c] == 1:
                    count = +1
                board[r][c] = count * flag
        for r in range(row):
            for c in range(col):
                print(board[r][c], end=" ")
                cur = board[r][c]
                if cur < 0:
                    if cur == -3:
                        board[r][c] = 1
                    else:
                        board[r][c] = 0
                else:
                    if cur <= 1:
                        board[r][c] = 0
                    elif cur == 2 or cur == 3:
                        board[r][c] = 1
                    elif cur > 3:
                        board[r][c] = 0
            print("")




