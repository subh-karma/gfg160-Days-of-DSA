class Solution:
    def nextLargerElement(self, arr):
        # code here
        st, ans = [arr[-1]], [-1]
        for i in range(len(arr)-2, -1, -1):
            stack_len = len(st) - 1
            while stack_len >= 0:
                if st[-1] > arr[i]:
                    ans.append(st[-1])
                    st.append(arr[i])
                    break
                else:
                    st.pop()
                stack_len -= 1
            if not st:
                ans.append(-1)
                st.append(arr[i])
        ans.reverse()
        return ans
        
