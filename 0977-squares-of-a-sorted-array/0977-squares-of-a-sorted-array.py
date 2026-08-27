class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l=[]
        m=0
        for i in nums:
            m=i**2
            l.append(m)
        l.sort()
        return l
