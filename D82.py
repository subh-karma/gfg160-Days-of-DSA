class Solution:
    def diameter(self, root):
        self.max_diameter = 0

        def height(node):
            if not node:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            self.max_diameter = max(self.max_diameter, left_height + right_height)

            return 1 + max(left_height, right_height)

        height(root)
        return self.max_diameter
