class Solution:
    def maxWater(self, arr):
        # code here
        n=len(arr)
        
        lmax=[0 for i in range(n)]
        rmax=[0 for i in range(n)]
        
        lmax[0]=arr[0]
        rmax[-1]=arr[-1]
        
        
        for i in range(1,n):
            lmax[i]=max(lmax[i-1],arr[i])
        
        for i in range(n-2,-1,-1):
            rmax[i]=max(rmax[i+1],arr[i])
        
        ans=0
        for i in range(1,n-1):
            ans+=(min(lmax[i],rmax[i])-arr[i])
        
        return ans
