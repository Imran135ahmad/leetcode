class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        dict2={}
        for i in range(n):
            rem=target-nums[i]
            if rem in dict2:
                return [dict2[rem],i]
            dict2[nums[i]]=i