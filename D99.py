class Solution:
    def isBalanced(self, s):
        stack = []
        map = {')':'(',']':'[','}':'{'}
        for i in s:
            if i in map.values():
                stack.append(i)
            else:
                if len(stack)==0 or stack[-1]!=map[i]:
                    return 0
                stack.pop()
        return len(stack)==0
