class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:

        tickets.sort(reverse = True)

        adjMap = defaultdict(list)

        for src,dest in tickets:
            adjMap[src].append(dest)
        
        res = []
        
        def dfs(src):
            while adjMap[src]:
                dest = adjMap[src].pop()
                dfs(dest)
            res.append(src)

        dfs("JFK")

        return res[::-1]
        