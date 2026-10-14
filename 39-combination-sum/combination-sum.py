class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res=[]

        def dfs(i,path,total):
            if total == target:
                res.append(path.copy())
                return
            
            if total > target or i >= len(candidates):
                return
            
            path.append(candidates[i])
            dfs(i,path, total + candidates[i])
            path.pop()

            dfs(i+1,path, total)
        

        dfs(0,[],0)

        return res
