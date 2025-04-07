class Solution:
    def power(self, b: float, e: int) -> float:
        # Code Here
        if e==0:
            return 1
        if e<0:
            return 1/self.power(b, -e)
        temp = self.power(b, e//2)
        if e%2 == 0:
            return temp*temp
        else:
            return temp*temp*b

#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        b = float(input())
        e = int(input())
        ob = Solution()
        result = ob.power(b, e)
        print(f"{result:.5f}")
        print("~")
# } Driver Code Ends
