class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:

        res = []
        done = set()

        def dfs(node,visit, done):

            if node in done:
                return True

            if not graph[node]:
                return True

            if node in visit:
                return False

            visit.add(node)

            for nei in graph[node]:
                if not dfs(nei,visit,done):
                    visit.remove(node)
                    return False

            visit.remove(node)
            done.add(node)
            return True
        
        for node in range(len(graph)):
            if dfs(node,set(),done):
                res.append(node)
        
        return res
        