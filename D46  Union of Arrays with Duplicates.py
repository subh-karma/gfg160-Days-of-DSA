class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def findUnion(self, a, b):
        return len(set(a+b))
