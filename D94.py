class Solution:
    def serialize(self, root):
        res = []
        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.data))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)
    
    def deSerialize(self, arr):
        vals = arr.split(",")
        self.i = 0
        
        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = Node(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right= dfs()
            return node
        return dfs()
