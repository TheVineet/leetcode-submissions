from functools import lru_cache
class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        rows,cols = len(matrix), len(matrix[0])


        @lru_cache(None)
        def dfs(r,c):
            longest = 1
            curr = matrix[r][c]    

            directions = [[1,0],[0,1],[-1,0],[0,-1]]

            for dr,dc in directions:
                row,col = r + dr, c + dc
                if row < 0 or row >= rows or col < 0 or col >= cols:
                    continue
                if matrix[row][col] <= curr:
                    continue
                longest = max(longest, 1 + dfs(row,col))
            
            return longest
            

        longest = 1
        for r in range(rows):
            for c in range(cols):
                longest = max(longest,dfs(r,c))

        return longest
            

            

