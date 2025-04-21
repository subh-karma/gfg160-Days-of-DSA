class Solution:
    # Return the kth smallest element in the given BST 
    def traverse_inorder(self,root):
        if not root:
            return
        self.traverse_inorder(root.left)
        self.inorder_array.append(root.data)
        self.traverse_inorder(root.right)
        
    def kthSmallest(self, root, k): 
        #code here.
        self.inorder_array = []
        self.traverse_inorder(root)
        
        if len(self.inorder_array) < k:
            return -1
        else:
            return self.inorder_array[k-1]
