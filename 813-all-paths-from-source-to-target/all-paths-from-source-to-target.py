class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        res = []
        n = len(graph)

        def dfs(node, path):
            path.append(node)

            if node == n - 1:
                res.append(path.copy())
            else:
                for nei in graph[node]:
                    dfs(nei, path)

            path.pop()

        dfs(0, [])
        return res