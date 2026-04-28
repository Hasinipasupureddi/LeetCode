#802. Find Eventual Safe States-Leetcode
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        #bfs approach
        '''n = len(graph)
        revg=[[] for i in range(n)]
        out = [0] * n

        for u in range(n):
            out[u]=len(graph[u])
            for v in graph[u]:
                revg[v].append(u)
        q = []
        for i in range(n):
            if out[i]==0:
                q.append(i)
        safe = [False] * n
        while q:
            node=q.pop(0)
            safe[node]=True
            for nei in revg[node]:
                out[nei]-=1
                if out[nei]==0:
                    q.append(nei)
        res=[]
        for i in range (n):
            if safe[i]:
                res.append(i)
        return res'''

        #dfs approach
        n = len(graph)
        v=[0] * n
        pv = [0] * n
        check = [0] * n
        def dfs(node):
            v[node]=1
            pv[node]=1
            for nei in graph[node]:
                if v[nei]==0:
                    if dfs(nei):
                        return True
                elif pv[nei]==1:
                    return True
            check[node]=1
            pv[node]=0
            return False
        for i in range(n):
            if v[i]==0:
                dfs(i)
        res=[]
        for i in range(n):
            if check[i]==1:
                res.append(i)
        return res