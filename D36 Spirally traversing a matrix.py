class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        # code here
        m,n=len(mat),len(mat[0])
        m_,n_=0,0
        i,j=0,0
        dir=1
        ans=[]
        while n_<n and m_<m:
            while n_<=j<n:
                ans.append(mat[i][j])
                j+=dir
            j-=dir
            i+=dir
            while m_<=i<m:
                ans.append(mat[i][j])
                i+=dir
            i-=dir
            j-=dir
            if dir==1:
                m_+=1
                n-=1
            else:
                m-=1
                n_+=1
            dir*=-1
        return ans
