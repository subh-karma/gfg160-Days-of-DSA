class Solution:
    def boundaryTraversal(self, root):
        # Code here
        def is_leaf(node):
            return node.left is None and node.right is None
        def left_boundary(node, boundary):
            curr = node.left
            while curr:
                if not is_leaf(curr):
                    boundary.append(curr.data)
                if curr.left:
                    curr = curr.left
                else:
                    curr= curr.right
        def right_boundary(node, boundary):
            curr = node.right
            st = []
            while curr:
                if not is_leaf(curr):
                    st.append(curr.data)
                if curr.right:
                    curr = curr.right
                else:
                    curr = curr.left
            while st:
                boundary.append(st.pop())
        def add_leaves(node, boundary):
            curr = node
            
            if is_leaf(curr):
                boundary.append(curr.data)
            else:
                if curr.left:
                    add_leaves(curr.left,boundary)
                if curr.right:
                    add_leaves(curr.right,boundary)
        if not root:
            return []
        boundary = []
        if not is_leaf(root):
            boundary.append(root.data)
        left_boundary(root,boundary)
        add_leaves(root,boundary)
        right_boundary(root,boundary)
        
        return boundary
