class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        res = []

        def dfs(openB, closedB, path):
            if openB == closedB == n:
                res.append("".join(path.copy()))
                return
            
            if openB <=n:
                path.append("(")
                dfs(openB + 1, closedB, path)
                path.pop()
            
            if closedB < openB:
                path.append(")")
                dfs(openB, closedB +1, path)
                path.pop()
        
        dfs(0,0,[])
        return res

        