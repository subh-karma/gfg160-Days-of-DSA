'''
Given a sorted and rotated array arr[] of distinct elements, the task is to find the index of a target key. Return -1 if the key is not found.
'''
class Solution:
    def search(self,arr,key):
        start=0
        end=len(arr)-1
        while start<=end:
            mid=(start+end)//2
            if(arr[mid]==key):
                return mid
            elif(arr[start]<=arr[mid]):
                if(key<arr[mid] and key>=arr[start]):
                    end=mid-1
                else:
                    start=mid+1
            else:
                if(arr[mid]<key<=arr[end]):
                    start=mid+1
                else:
                    end=mid-1
        return -1
