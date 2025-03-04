#User function Template for python3
class Solution:
    def twoSum(self, arr, target):
        seen = set()
        for i in arr:
            complement = target- i
            if complement in seen:
                return True
            seen.add(i)
        return False
