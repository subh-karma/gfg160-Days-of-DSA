class Solution:
    def inorderTraversal(self,root, inorder):
        if root is None:
            return
    
        self.inorderTraversal(root.left, inorder)
    
        # Store the current node's value
        inorder.append(root.data)
    
        self.inorderTraversal(root.right, inorder)
    def findTarget(self, root, target):
        inorder = []
        self.inorderTraversal(root, inorder)
    
        # Use two-pointer technique to find the pair with given sum
        left, right = 0, len(inorder) - 1
    
        while left < right:
            currentSum = inorder[left] + inorder[right]
    
            # If the pair is found, return true
            if currentSum == target:
                return True
    
            # If the current sum is less than the target, 
            # move the left pointer
            if currentSum < target:
                left += 1
              
            # If the current sum is greater than 
            # the target, move the right pointer
            else:
                right -= 1
    
        return False
        # your code he
