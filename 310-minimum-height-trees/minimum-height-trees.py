class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return [0]
        adjMap = {i : [] for i in range(n)}
        for n1,n2 in edges:
            adjMap[n1].append(n2)
            adjMap[n2].append(n1)

        # Find the leave and start bfs from there

        edge_cnt = {}
        q = collections.deque()


        for src,neigh in adjMap.items():
            if len(neigh) == 1:
                q.append(src)
            
            edge_cnt[src] = len(neigh)

        
        while q:
            if n <= 2:
                return list(q)
            for i in range(len(q)):
                src = q.popleft()
                n -= 1
                for neigh in adjMap[src]:
                    edge_cnt[neigh] -= 1
                    if edge_cnt[neigh] == 1:
                        q.append(neigh)

            




        
