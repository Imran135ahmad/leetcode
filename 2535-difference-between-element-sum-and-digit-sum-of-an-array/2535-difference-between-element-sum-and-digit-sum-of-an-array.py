class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        n=0
        for i in nums:
            total = 0
            while i>9:
                total += i % 10
                i //= 10

            total += i
            n += total

        return abs(sum(nums) - n)