class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        set1, set2 = set(), set()


        for start in range(len(graph)):
            if start in set1 or start in set2:
                continue

            q = collections.deque()
            q.append(start)
            set1.add(start)

            while q:
                u = q.popleft()

                for v in graph[u]:
                    if v ==u :
                        return False

                    if u in set1:
                        if v in set1:
                            return False
                        if v not in set2:
                            set2.add(v)
                            q.append(v)

                    else:
                        if v in set2:
                            return False
                        if v not in set1:
                            set1.add(v)
                            q.append(v)
            
        return True
