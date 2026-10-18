from itertools import product
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        adjMap = collections.defaultdict(list)
        
        for tup in product(range(k), repeat = n-1):
            node = "".join(map(str, tup))
            for j in range(k):
                val = node + str(j)
                val = val[1:]
                adjMap[node].append((val,str(j)))
        
        res = []
        def dfs(node):
            while adjMap[node]:
                dest,val = adjMap[node].pop()
                dfs(dest)
                res.append(str(val))
        
        start = "0" * (n-1)
        dfs(start)
        return start + "".join(res[::-1])



        