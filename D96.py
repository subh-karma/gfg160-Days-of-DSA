class Solution:
    def LCA(self, root, n1, n2):
        # your code here
        val1 = n1.data if isinstance(n1, Node) else n1
        val2 = n2.data if isinstance(n2, Node) else n2
        if not root:
            return None
        if val1 < root.data and val2 < root.data:
            return self.LCA(root.left, val1, val2)
        elif val1 > root.data and val2 > root.data:
            return self.LCA(root.right, val1, val2)
        else:
            return root
