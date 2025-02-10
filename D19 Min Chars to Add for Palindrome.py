'''
Explanation: Add 2 a's at front of above string to make it palindrome : "aaaacecaaaa"

'''
class Solution:
    def minChar(self, s):
        n = len(s)
        rev_s = s[::-1]
        concat_s = s + "$" + rev_s
        
        lps = [0] * len(concat_s)
        j = 0
        
        for i in range(1, len(concat_s)):
            while j > 0 and concat_s[i] != concat_s[j]:
                j = lps[j - 1]
            if concat_s[i] == concat_s[j]:
                j += 1
            lps[i] = j
        
        return n - lps[-1]
        #Write your code here





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        obj = Solution()
        ans = obj.minChar(s)
        print(ans)
        print("~")

# } Driver Code Ends
