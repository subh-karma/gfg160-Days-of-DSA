class Solution:
    def countDistinct(self, arr, k):
        dici={}
        l=0
        res=[]
        for r in range(len(arr)):
            if arr[r] not in dici:
                dici[arr[r]]=1
            else:
                dici[arr[r]]+=1
            if r-l+1==k:
                res.append(len(dici))
                dici[arr[l]]-=1
                if dici[arr[l]]==0:
                    del dici[arr[l]]
                l+=1
        return(res)
