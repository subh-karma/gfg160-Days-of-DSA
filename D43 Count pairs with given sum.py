class Solution:
    #Complete the below function
    def countPairs(self,arr, tar):
        #Your code here
        freq ={}
        c = 0
        
        for i in range(len(arr)):
            if (tar - arr[i]) in freq:
                c+=freq[tar-arr[i]]
            
            
            freq[arr[i]] = freq.get(arr[i],0)+1
        
        return c
