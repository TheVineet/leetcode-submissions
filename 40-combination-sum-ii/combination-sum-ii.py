class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()

        def dfs(i,path,total):
            if total == target:
                res.append(path.copy())
                return
            
            if total > target or i >= len(candidates):
                return
            
            path.append(candidates[i])
            dfs(i+1, path, total + candidates[i])
            path.pop()

            while (i + 1) < len(candidates) and candidates[i+1] == candidates[i]:
                i +=1
            dfs(i+1, path, total)
        

        dfs(0,[],0)
        return res

        