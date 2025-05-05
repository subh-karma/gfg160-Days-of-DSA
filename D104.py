class Solution:
    def maxOfMins(self, arr):
        s=[]
        n=len(arr)
        window=[0]*(n)
        l=[-1]*(n)
        r=[n]*(n)
        res=[]
       
        for i in range(n):
            while s and arr[s[-1]]>arr[i]:
               ind=s.pop()
               r[ind]=i
            s.append(i)
        
        while s:
            s.pop()
            
        for i in range(n-1,-1,-1):
            while s and arr[s[-1]]>arr[i]:
                ind=s.pop()
                l[ind]=i
            s.append(i)
        
        
        for i in range(n):
            ind=r[i]-l[i]-2
            window[ind]=max(window[ind],arr[i])

        for i in range(n-2,-1,-1):
            window[i]=max(window[i],window[i+1])
        
        return window
