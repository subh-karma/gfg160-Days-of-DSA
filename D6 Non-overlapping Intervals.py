'''
Given a 2D array intervals[][] of representing intervals where intervals [i] = [starti, endi ]. Return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Examples:

Input: intervals[][] = [[1, 2], [2, 3], [3, 4], [1, 3]]
Output: 1
Explanation: [1, 3] can be removed and the rest of the intervals are non-overlapping.
'''
class Solution:
    def minRemoval(self, intervals):
        # Code here
        # sort the array
        intervals.sort()
        # take the  first index of zeroth elemet of the array in the ans
        ans = intervals[0][1]
        # initialise the count
        c = 0
        # now loop over the 1st eleme to the len of the array
        for i in range(1,len(intervals)):
            # check for overlapping
            if(intervals[i][0] < ans):
                # there is an overlap
                c +=1 # increse the count 
                ans = min(ans , intervals[i][1])
            else:
                # dont take the min
                ans = intervals[i][1]
        # return count
        return c        #
