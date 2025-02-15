'''
Given an array of Intervals arr[][], where arr[i] = [starti, endi]. The task is to merge all of the overlapping Intervals.

Examples:

Input: arr[][] = [[1,3],[2,4],[6,8],[9,10]]
Output: [[1,4], [6,8], [9,10]]
Explanation: In the given intervals we have only two overlapping intervals here, [1,3] and [2,4] which on merging will become [1,4]. Therefore we will return [[1,4], [6,8], [9,10]].
Input: arr[][] = [[6,8],[1,9],[2,4],[4,7]]
Output: [[1,9]]
Explanation: In the given intervals all the intervals overlap with the interval [1,9]. Therefore we will return [1,9].
'''
class Solution:
    def mergeOverlap(self, arr):
        #Code here
        #sort the array
        arr.sort()
        # make the answer array
        ans = [arr[0]]
        # now loop over the array 
        for i in range(1 , len(arr)):
            # chek if the arr[i][0] time <= ans[-1][1]
            if(arr[i][0] <= ans[-1][1]):
                # if this happens
                # max of the ending time will be added to the ans[-1][1]
                ans[-1][1] = max(ans[-1][1] , arr[i][1])
            else:
                ans.append(arr[i])
        # now retunrn the ans
        return  ans
      
