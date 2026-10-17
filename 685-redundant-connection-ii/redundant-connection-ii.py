class Solution:
    def findRedundantDirectedConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges) #usually its edges + 1, but here since it has one extra edge

        par = [i for i in range(n + 1)]
        rank = [0] * (n + 1)

        parents = [0] * (n + 1)
        candA = candB = None

        for n1,n2 in edges:
            if parents[n2] == 0:
                parents[n2] = n1

            else:
                candA = [parents[n2],n2]
                candB = [n1,n2]
            

        def find(n1):
            curr = n1
            while par[curr] != curr:
                par[curr] = par[par[curr]]
                curr = par[curr]
            
            return curr
        

        def union(n1,n2):
            p1,p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]

            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            return True
        
        for n1,n2 in edges:
            if [n1,n2] == candB:
                continue
            
            if not union(n1,n2):
                return candA if candB else [n1,n2]    
        
        return candB
        
        
