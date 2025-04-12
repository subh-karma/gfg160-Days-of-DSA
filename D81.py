class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        # code here
        if root is None:
            return -1
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return 1+(max(left_height, right_height))
