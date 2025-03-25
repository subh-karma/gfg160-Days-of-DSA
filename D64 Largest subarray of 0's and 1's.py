from collections import defaultdict

class Solution:
    def __init__(self):
        self.prefixSum = defaultdict(lambda: -2)
        
    def maxLen(self, arr):
        
        subArrayLen = 0
        totalSum = 0
        self.prefixSum[totalSum] = -1
        index = 0
        for val in arr:
            if val == 0:
                totalSum -= 1
            else:
                totalSum += 1
                
            if self.prefixSum[totalSum] != -2:
                currSubArrayLen = index  - self.prefixSum[totalSum]
                if currSubArrayLen > subArrayLen:
                    subArrayLen = currSubArrayLen
            else:
                self.prefixSum[totalSum] = index
                
            index += 1
        
        return subArrayLen
