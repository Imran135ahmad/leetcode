class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans=[]
        for num in nums:
            total = 0

            while num > 0:
                total += num % 10
                num //= 10
            ans.append(total)
        return min(ans)