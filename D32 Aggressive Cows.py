'''
You are given an array with unique elements of stalls[], which denote the position of a stall. You are also given an integer k which denotes the number of aggressive cows. Your task is to assign stalls to k cows such that the minimum distance between any two of them is the maximum possible.

Examples :

Input: stalls[] = [1, 2, 4, 8, 9], k = 3
Output: 3
Explanation: The first cow can be placed at stalls[0], 
the second cow can be placed at stalls[2] and 
the third cow can be placed at stalls[3]. 
The minimum distance between cows, in this case, is 3, which also is the largest among all possible ways.
''''
class Solution:

    def aggressiveCows(self, stalls, k):
        # your code here
        stalls.sort()
        l=1
        r=stalls[-1]-stalls[0]
        ans=-1
        n=len(stalls)
        while(l<=r):
            mid=(l+r)//2
            c=1
            prev=stalls[0]
            for i in range(1,n):
                if stalls[i]-prev>=mid:
                    c+=1
                    prev=stalls[i]
            if c>=k:
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans
