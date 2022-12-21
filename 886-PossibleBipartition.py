from collections import deque

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def bfs(start):
            q = deque([start])
            color[start] = 0

            while q:
                u = q.popleft()
                for neighbor in adj[u]:
                    if color[neighbor] == color[u]: 
                        return False
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[u]
                        q.append(neighbor)
            return True

        adj = [[] for _ in range(n + 1)]
        for dislike in dislikes:
            adj[dislike[0]].append(dislike[1])
            adj[dislike[1]].append(dislike[0])
        
        color = [-1] * (n + 1)
        for i in range(1, n + 1):
            if color[i] == -1:
                if not bfs(i):
                    return False

        return True