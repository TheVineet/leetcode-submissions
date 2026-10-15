class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        preMap = {i : [] for i in range(numCourses)}
        for c1,c2 in prerequisites:
            preMap[c1].append(c2)
        
        res = []

        def dfs(i,visit,done):
            if i >= numCourses:
                return False
            
            if i in visit:
                return False
            
            if i in done:
                return True
            
            visit.add(i)

            for course in preMap[i]:
                if not dfs(course,visit, done):
                    return False
            

            visit.remove(i)
            done.add(i)
            res.append(i)
            return True

        done = set()
        for course in range(numCourses):
            if not dfs(course,set(),done):
                return []
        
        return res