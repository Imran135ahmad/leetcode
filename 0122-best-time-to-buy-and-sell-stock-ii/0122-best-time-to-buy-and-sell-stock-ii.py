class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=0
        n=len(prices)
        for i in range(n-1):
            if prices[i+1]>prices[i]:
                p+=prices[i+1]-prices[i]
        return p
