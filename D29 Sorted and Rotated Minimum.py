class Solution:
    def findMin(self, arr):
        #complete the function here
        low, high = 0, len(arr)-1
        while low<high:
            mid = low+(high-low)//2

            if arr[mid]>arr[high]:
                low = mid+1
            else:
                high = mid
        return arr[low]
