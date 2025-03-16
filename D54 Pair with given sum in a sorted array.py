class Solution:
    def countPairs (self, arr, target) :
        
        n = len(arr)
        l =0
        r = n-1
        c=0
        
        while(l<r):
            new_target = arr[l]+arr[r]
            if(new_target < target):
                l =l+1
            elif(new_target > target):
                r = r-1
            else:
                c1 = 0
                c2 = 0
                ele1 = arr[l]
                ele2 = arr[r]
                
                while(l<=r and arr[l] == ele1):
                    l = l+1
                    c1 =c1+1
                
                while(l<=r and arr[r]==ele2):
                    r = r-1
                    c2 = c2+1
                
                if(ele1 == ele2):
                    c +=  (c1*(c1-1))//2
                else:
                    c +=  c1*c2
                    
                
                
        return c





#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    t = int(data[0].strip())
    index = 1

    for _ in range(t):
        arr = list(map(int, data[index].strip().split()))
        index += 1
        target = int(data[index].strip())
        index += 1

        res = Solution().countPairs(arr, target)
        print(res)
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
