class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
                ans.extend([int(x) for x in str(i)])
        return ans