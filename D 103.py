class Solution:
    def getMaxArea(self,arr):
        #code here
        stack = []
        n = len(arr)
        ans = arr[0]
        stack.append((arr[0],1))
        for i in range(1,n):
            #print(ans,arr[i],stack)
            if arr[i] > stack[-1][0]:
                stack.append((arr[i],1))
                ans = max(ans,arr[i])
            else:
                barheight_count = stack.pop()
                height = barheight_count[0]
                count = barheight_count[1]
                ans = max(ans,height*count)
                while len(stack) > 0 and stack[-1][0] >= arr[i]:
                    barheight_count = stack.pop()
                    height = barheight_count[0]
                    count = count + barheight_count[1]
                    ans = max(ans,height*count)
                stack.append((arr[i],count+1))
        barheight_count = stack.pop()
        height = barheight_count[0]
        count = barheight_count[1]
        ans = max(ans,height*count)                
        while len(stack) > 0:
            #print(ans,arr[i],stack)            
            barheight_count = stack.pop()
            height = barheight_count[0]
            count = count + barheight_count[1]
            ans = max(ans,height*count)
        return ans
