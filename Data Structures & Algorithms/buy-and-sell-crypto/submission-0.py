class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        res=0
        for price in prices:
            buy=min(buy,price)
            profit=price-buy
            res=max(profit,res)

        return res