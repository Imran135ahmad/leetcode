class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        m=min(nums)
        l=max(nums)
        s=set(nums)
        ans=[]
        for i in range(m+1,l):
            if i not in s:
                ans.append(i)
        return ans 