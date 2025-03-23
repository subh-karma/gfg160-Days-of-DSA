class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        # code here
        n=len(arr)
        larr=[0]*n
        rarr=[0]*n
        larr[0]=arr[0]
        rarr[n-1]=arr[n-1]
        for i in range(1,n):
            larr[i]=arr[i]+larr[i-1]
            
        for j in range(n-2,-1,-1):
            rarr[j]=arr[j]+rarr[j+1]
            
        for i in range(n):
            rightsum=larr[i-1] if i>0 else 0
            leftsum=rarr[i+1] if i<n-1 else 0
            if leftsum==rightsum:
                return i
        return -1
