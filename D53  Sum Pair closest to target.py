class Solution:
    def sumClosest(self, arr, target):
        
        n = len(arr)
        arr.sort()
        
        maxDiff = float('inf')
        
        res = []
        l = 0
        r = n-1
        
        while(l<r):
            currsum = arr[l]+arr[r]
            
            if(abs(currsum-target) < maxDiff):
                maxDiff = abs(currsum - target)
                res = [arr[l], arr[r]]
            
            
            if(currsum < target):
                l = l+1
            elif(currsum > target):
                r = r-1
            else:
                return res
        return res
        
