class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=nums
        l=[]
        m=0
        for i in n:
            m=i**2
            l.append(m)
        l.sort()
        return l
