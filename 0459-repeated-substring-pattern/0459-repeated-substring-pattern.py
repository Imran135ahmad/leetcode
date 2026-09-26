class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n= len(s)
        for l in range(1,n):
            if n%l==0:
                pattern=s[:l]

                if pattern * (n//l)==s:
                    return True
        return False
