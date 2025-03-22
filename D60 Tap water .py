class Solution:
    def maxWater(self, arr):
        # code here
        left, right = 0, len(arr) - 1
        res = 0
        while left < right:
            water = min(arr[left], arr[right]) * (right - left)
            res = max(water, res)
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1
        return res
