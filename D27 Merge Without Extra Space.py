'''
Given two sorted arrays a[] and b[] of size n and m respectively, the task is to merge them in sorted order without using any extra space. Modify a[] so that it contains the first n elements and modify b[] so that it contains the last m elements.

Examples:

Input: a[] = [2, 4, 7, 10], b[] = [2, 3]
Output:
2 2 3 4
7 10
Explanation: After merging the two non-decreasing arrays, we get, 2 2 3 4 7 10
'''
class Solution:
    def mergeArrays(self, a, b):
        l=[]
        for i in a:
            l.append(i)
        for i in b:
            l.append(i)
        l.sort()
        for i in range(len(a)):
            a[i]=l[i]
        j=0
        for k in range(len(a),len(l)):
            b[j]=l[k]
            j+=1
        return a,b
