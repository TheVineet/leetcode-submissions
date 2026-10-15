class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}
        for c1,c2 in prerequisites:
            preMap[c1].append(c2)
        
        done = set()
        def dfs(i,visit,done):
            if i >= numCourses:
                return True

            if i in visit:
                return False
            
            if i in done:
                return True
            
            
            visit.add(i)
            for preq in preMap[i]:
                if not dfs(preq,visit,done):
                    return False
            
            visit.remove(i)
            done.add(i)
            return True
        
        for course in range(numCourses):
            if not dfs(course,set(),done):
                return False
        
        return True
            




        