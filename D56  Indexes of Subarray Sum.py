class Solution:
    def subarraySum(self, arr, target):
        # code here
        s,e=0,0
        ans=[]
        sm=0
        for i in range(len(arr)):
            sm+=arr[i]
            if sm>=target:
                e=i
                while sm>target:
                    sm-=arr[s]
                    s+=1
                if sm==target:
                    ans.append(s+1)
                    ans.append(e+1)
                    return ans
        return [-1]
