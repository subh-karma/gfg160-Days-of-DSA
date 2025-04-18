class Solution:
    #Function to return maximum path sum from any node in a tree.
    def findMaxSum(self, root): 
        #Your code here
        m = [float('-inf')]
        
        def findPath(root,m):
            if root is None:
                return 0
            
            left = max(0, findPath(root.left,m))
            right = max(0, findPath(root.right,m))
            
            
            m[0] = max(m[0],left+right+root.data)
            
            
            return max(left,right) +root.data
            
        findPath(root,m)
        
        return m[0]
