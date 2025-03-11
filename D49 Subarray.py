#User function Template for python3

class Solution:
    def countSubarrays(self, arr, k):
        # code here
        d = {0:1}
        i,j = 0,0
        cur_sum = 0
        cnt = 0
        target = k
        while j<len(arr):
            cur_sum += arr[j]
            if cur_sum - target in d:
                cnt+=d[cur_sum - target]
            d[cur_sum] = d.get(cur_sum,0)+1
            j+=1
        return cnt
