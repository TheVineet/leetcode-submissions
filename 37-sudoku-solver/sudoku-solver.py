class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rowN,colN = len(board), len(board[0])

        rows = [set() for i in range(rowN)]
        cols = [set() for i in range(colN)]
        squares = [set() for i in range(rowN)]

        dotCount = 0

        for r in range(rowN):
            for c in range(colN):

                if board[r][c] == ".":
                    continue
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    sqIndex = (r // 3) * 3 +  (c // 3)
                    squares[sqIndex].add(board[r][c])


        def dfs(posn):
            if posn >= 81:
                return True
            
            r = posn // 9
            c = posn % 9
            
            if board[r][c] == "." :
                for i in range(1,10):
                    i = str(i)
                    if i in rows[r]:
                        continue
                    if i in cols[c]:
                        continue
                    
                    sqIndex = (r // 3) * 3 +  (c // 3)
                    if i in squares[sqIndex]:
                        continue
                    
                    board[r][c] = i
                    rows[r].add(i)
                    cols[c].add(i)
                    squares[sqIndex].add(i)
                    
                    if dfs(posn + 1):
                        return True
                    
                    # backtrack
                    board[r][c] = "."
                    rows[r].remove(i)
                    cols[c].remove(i)
                    squares[sqIndex].remove(i)
            
            else :
                if dfs(posn + 1):
                    return True
            
            return False
            
        dfs(0)


            

            

        