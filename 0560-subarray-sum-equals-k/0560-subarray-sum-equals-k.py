class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumdict={0:1}
        c=0
        s=0
        for i in nums:
            s+=i
            if s-k in sumdict:
                c+=sumdict[s-k]
            if s in sumdict:
                sumdict[s]+=1
            else:
                sumdict[s]=1
        return c