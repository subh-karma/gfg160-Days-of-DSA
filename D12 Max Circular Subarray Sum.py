'''
Given an array of integers arr[] in a circular fashion. Find the maximum subarray sum that we can get if we assume the array to be circular.

Examples:

Input: arr[] = [8, -8, 9, -9, 10, -11, 12]
Output: 22
Explanation: Starting from the last element of the array, i.e, 12, and moving in a circular fashion, we have max subarray as 12, 8, -8, 9, -9, 10, which gives maximum sum as 22.
Input: arr[] = [10, -3, -4, 7, 6, 5, -4, -1]
Output: 23
Explanation: Maximum sum of the circular subarray is 23. The subarray is [7, 6, 5, -4, -1, 10].
Input: arr[] = [-1, 40, -14, 7, 6, 5, -4, -1] 
Output: 52
Explanation: Circular Subarray [7, 6, 5, -4, -1, -1, 40] has the maximum sum, which is 52.

'''

def circularSubarraySum(arr):
    ##Your code here
    tot=0
    cmin=0
    cmax=0
    ma=arr[0]
    mi=arr[0]
    for i in range(len(arr)):
        cmax=max(arr[i],cmax+arr[i])
        ma=max(cmax,ma)
        cmin=min(cmin+arr[i],arr[i])
        mi=min(cmin,mi)
        tot+=arr[i]
    cir=tot-mi
    if mi==tot:
        return ma
    return max(ma,cir)
