
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = []
        countMap = {}

        for num in nums:
            count = countMap.get(num, 0)
            countMap[num] = count + 1

        def dfs(path, visitCount):
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for curr in countMap:
                currCount = visitCount.get(curr, 0)
                totalCount = countMap.get(curr)

                if currCount >= totalCount:
                    continue

                path.append(curr)
                visitCount[curr] = currCount + 1

                dfs(path, visitCount)

                # Backtrack
                path.pop()
                visitCount[curr] = currCount

        dfs([], {})
        return res
