class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        adjMap = {}
        for i in range(len(equations)):
            n1 = equations[i][0]
            n2 = equations[i][1]
            val = values[i]

            if not n1 in adjMap:
                adjMap[n1] = []
            
            if not n2 in adjMap:
                adjMap[n2] = []
            
            adjMap[n1].append((n2,val)) #node,val
            adjMap[n2].append((n1, 1 / val))
        
        def dfs(curr, target, visit):
            if curr == target:
                return 1.0

            visit.add(curr)

            for node, val in adjMap[curr]:
                if node in visit:
                    continue

                result = dfs(node, target, visit)

                if result != -1.0:
                    return val * result

            return -1.0
        
        res = []
        for q1,q2 in queries:
            if q1 not in adjMap or q2 not in adjMap:
                res.append(-1)
                continue
            
            if q1 == q2:
                res.append(1)
                continue
            
            res.append(dfs(q1,q2,set()))
        
        return res
            
