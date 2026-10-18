class Solution:
    def minSwapsCouples(self, row: list[int]) -> int:
        """
        The core idea is simple cycle detection.
        The intuition to think about is, how we can represent the data in a graph. More like
        how we can arrange it in adjMap.
        One key information that drives the intuition is that, row 0, row 1 would be C1 node.
        row 2, row 3 would be part of C2 node.
        So we just apply union find then
        """
        n = len(row) // 2
        par = [i for i in range(n)]
        rank = [0] * n

        def find(node):
            while par[node] != node:
                par[node] = par[par[node]]
                node = par[node]
            return node
        
        def union(n1,n2):
            p1,p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else :
                par[p1] = p2
                rank[p2] += rank[p1]
            return 1
        

        res = n
        for i in range(0, len(row),2):
            a1 = row[i] // 2
            a2 = row[i + 1] // 2
            res -= union(a1,a2)
        
        return n - res