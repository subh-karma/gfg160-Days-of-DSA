#User function Template for python3


        # code here
class Solution:
    def longestUniqueSubstr(self, s):
        n= len(s)
        left =0 
        res=0
        right=0
        visited=[0]*26
        while(right<len(s)):
            
            while(visited[ord(s[right])- ord('a')] =='True'):
                visited[ord(s[left])-ord('a')] = False
                left+=1
            visited[ord(s[right])-ord('a')] = 'True'
            right+=1
            res = max(res, (right-left))
        return res
             
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.longestUniqueSubstr(s)

        print(ans)

        print("~")
# } Driver Code Ends
