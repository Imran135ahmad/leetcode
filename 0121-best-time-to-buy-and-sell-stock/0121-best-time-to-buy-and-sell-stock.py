class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp=prices[0]
        p=0
        for i in range(1,len(prices)):
            cp=prices[i]-mp
            if cp>p:
                p=cp
            mp=min(mp,prices[i])
        return p
        
            