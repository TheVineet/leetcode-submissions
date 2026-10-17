class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        par = [i for i in range(n)]
        rank = [0] * n

        def find(n1):
            curr = n1
            while par[curr] != curr:
                par[curr] = par[par[curr]]
                curr = par[curr]
            
            return curr
        

        def union(n1,n2):
            p1,p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            return 1
        
        res = n
        for r in range(n):
            for c in range(n):
                if isConnected[r][c] == 0:
                    continue
                
                res -= union(r,c)
        
        return res