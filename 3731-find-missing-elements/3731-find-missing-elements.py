class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        m=min(nums)
        l=max(nums)
        ans=[]
        for i in range(m+1,l):
            if i not in nums:
                ans.append(i)
        return ans 