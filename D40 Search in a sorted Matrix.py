class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def searchMatrix(self, mat, x): 
        # code here 
        n=len(mat)
        m=len(mat[0])
        i,j=0,m-1
        while i<n and j>=0:
            if mat[i][j]==x:
                return True
            elif mat[i][j]<x:
                i+=1
            else:
                j-=1
        return Fals
