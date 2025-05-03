class Solution:
    def calculateSpan(self, arr):
        n = len(arr)
        stack = []
        span = []

        for i in range(n):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()

            if not stack:
                span.append(i + 1)
            else:
                span.append(i - stack[-1])

            stack.append(i)

        return span
