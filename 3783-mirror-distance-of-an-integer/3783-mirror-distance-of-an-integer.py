class Solution:
    def mirrorDistance(self, n: int) -> int:
        c=0
        m=n
        while m>0:
            rev=m%10
            c=c*10+rev
            m=m//10
        
        return abs(n-c)
        
