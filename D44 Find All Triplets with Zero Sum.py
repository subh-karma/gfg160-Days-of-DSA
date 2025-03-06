from collections import defaultdict

        # Your code here
class Solution:
    def findTriplets(self, arr):
        
        n = len(arr)
        hashmap = defaultdict(list)
        
        # store sum of all the pairs with their indices
        for i in range(n):
            for j in range(i+1, n):
                pair_sum = arr[i] + arr[j]
                hashmap[pair_sum].append( (i, j) )
        
        res = set()
        for i in range(n):
            rem = -arr[i]
            if rem in hashmap:
                pairs = hashmap[rem]
                for p in pairs:
                    if p[0] != i and p[1] != i:
                        res.add( tuple(sorted([ i, p[0], p[1] ])) )
        
        return list(res)
