class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        
        def dfs(path,visit):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for num in nums:
                if num in visit:
                    continue
                
                path.append(num)
                visit.add(num)
                dfs(path,visit)

                # backtrack
                path.pop()
                visit.remove(num)
        
        dfs([],set())
        return res

        
