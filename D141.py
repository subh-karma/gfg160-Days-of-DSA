class Solution:
    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])  # Path compression
        return parent[x]

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        
        if xroot == yroot:
            return False  # Cycle detected

        # Union by rank
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

        return True

    def isCycle(self, V, edges):
        parent = list(range(V))
        rank = [0] * V

        for u, v in edges:
            if not self.union(parent, rank, u, v):
                return True  # Cycle exists

        return False  # No cycle
