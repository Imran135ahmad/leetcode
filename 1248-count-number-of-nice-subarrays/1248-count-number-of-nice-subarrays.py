class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        def atMost(k):
            l=0
            ans=0
            odd=0
            
            for right in range(n):
                if nums[right]%2==1:
                    odd+=1
                
                while odd>k:
                    if nums[l]%2==1:
                        odd-=1
                    l+=1

                ans += right-l+1
            return ans
        return atMost(k)-atMost(k-1)