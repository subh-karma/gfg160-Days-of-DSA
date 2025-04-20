class Solution:
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        #code here
        def isBSTBoundaries(node, min_val, max_val):
            if node is None:
                return True
            if not (min_val < node.data < max_val):
                return False
            return (isBSTBoundaries(node.left, min_val, node.data) and
                    isBSTBoundaries(node.right, node.data, max_val))
    
        return isBSTBoundaries(root, float('-inf'), float('inf'))
