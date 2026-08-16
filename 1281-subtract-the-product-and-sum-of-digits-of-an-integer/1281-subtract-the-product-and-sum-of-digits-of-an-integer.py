class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp=n
        r=0
        m=1
        while temp>0:
            n=temp%10
            temp//=10
            r+=n
            m*=n
           
        return m-r