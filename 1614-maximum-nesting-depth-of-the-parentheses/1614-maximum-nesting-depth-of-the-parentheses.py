class Solution:
    def maxDepth(self, s: str) -> int:
        stack=0
        c=0
        for i in s:
            if i=='(':
                stack+=1
                c=max(c,stack)
            elif i==')':
                stack-=1
        return c
