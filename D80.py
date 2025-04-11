class Solution:
    def levelOrder(self, root):
        # Your code here
        if root is None:
            return[]
        q=[]
        res=[]
        q.append(root)
        curr_level=0
        while q:
            len_q=len(q)
            res.append([])
            for _ in range(len_q):
                node=q.pop(0)
                res[curr_level].append(node.data)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            curr_level+=1
        return res
