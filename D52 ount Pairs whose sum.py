
class Solution:
    def countPairs(self, arr, target):
        n = len(arr)
        
        arr.sort()
        count =0
        
        l,r = 0,n-1
        
        while(l<r):
            sum = arr[l] + arr[r]
            
            if(sum>=target):
                r = r-1
            else:
                count = count + (r-l)
                l = l+1
        return count
                
        
        
        
