class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adjMap = {i  : [] for i in range(1,n +1)}

        for n1,n2,t in times:
            adjMap[n1].append((t,n2))
        
        # q = collections.deque()
        minHeap = []
        time = 0
        minHeap.append((0,k))
        visit = set()
        

        while minHeap:
            t,node = heapq.heappop(minHeap)
            if node in visit:
                continue

            visit.add(node)
            
            time = max(t,time)

            for t1,n1 in adjMap[node]:
                heapq.heappush(minHeap, (t + t1, n1))
    


        return time if len(visit) == n else -1