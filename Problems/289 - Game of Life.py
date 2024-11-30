class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        live, die = [],[]
        direction = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
        for i in range(len(board)):
            for j in range(len(board[0])):
                temp = 0
                for d in direction:
                    m,n = i + d[0], j + d[1]
                    if m >=0 and m < len(board) and n >=0 and n < len(board[0]):
                        if board[m][n] == 1:
                            temp += 1

                if board[i][j] == 1:
                    if temp != 2 and temp != 3:
                        die.append([i,j])
                else:
                    if temp == 3:
                        live.append([i,j])
        for l in live:
            board[l[0]][l[1]] = 1
        for d in die:
            board[d[0]][d[1]] = 0
