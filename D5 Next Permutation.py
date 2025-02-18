'''
Given an array of integers arr[] representing a permutation, implement the next permutation that rearranges the numbers into the lexicographically next greater permutation. If no such permutation exists, rearrange the numbers into the lowest possible order (i.e., sorted in ascending order). 

Note - A permutation of an array of integers refers to a specific arrangement of its elements in a sequence or linear order.

Examples:

Input: arr = [2, 4, 1, 7, 5, 0]
Output: [2, 4, 5, 0, 1, 7]
Explanation: The next permutation of the given array is {2, 4, 5, 0, 1, 7}.
Input: arr = [3, 2, 1]
Output: [1, 2, 3]
Explanation: As arr[] is the last permutation, the next permutation is the lowest one.
Input: arr = [3, 4, 2, 5, 1]
Output: [3, 4, 5, 1, 2]
Explanation: The next permutation of the given array is {3, 4, 5, 1, 2}.
'''
class Solution:
    def nextPermutation(self, arr):
        # code here
        i=len(arr)-2
        while i>=0 and arr[i]>=arr[i+1]:     #i is bigger than index and i bigger than its before element 
            i-=1
        if i>=0:
            j=len(arr)-1
            while arr[j]<=arr[i]:
                j-=1
            arr[i],arr[j]=arr[j],arr[i]    
        arr[i+1:]=arr[i+1:][::-1]
        return arr
    
