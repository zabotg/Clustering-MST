class UnionFind:

    def __init__(self, vector):
        self.rank = [1] * len(vector)
        self.parent = vector
        self.size = len(vector)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)

        # X and Y are already in the same set
        if xRoot == yRoot:
            return

        # X and Y are not in same set, so we merge them
        if self.rank[xRoot] < self.rank[yRoot]:
            xRoot, yRoot = yRoot, xRoot  # Swap xRoot and yRoot

        self.size -= 1
        # merge yRoot into xRoot
        self.parent[yRoot] = xRoot
        if self.rank[xRoot] == self.rank[yRoot]:
            self.rank[xRoot] = self.rank[yRoot] + 1
