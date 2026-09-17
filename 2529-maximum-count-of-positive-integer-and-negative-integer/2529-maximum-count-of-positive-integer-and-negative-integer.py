class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        c=0
        n=0
        for i in nums:
            if i > 0:
                c+=1
            elif i<0:
                n+=1
        return max(c,n)