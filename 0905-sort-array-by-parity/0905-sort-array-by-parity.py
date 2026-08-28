class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n=len(nums)
        s=0
        for i in range(n):
            if nums[i]%2==0:
                temp=nums[i]
                nums[i]=nums[s]
                nums[s]=temp
                s+=1
            i+=1
        return nums

