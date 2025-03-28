'''
The cost of stock on each day is given in an array price[]. Each day you may decide to either buy or sell the stock i at price[i], you can even buy and sell the stock on the same day. Find the maximum profit that you can get.

Note: A stock can only be sold if it has been bought previously and multiple stocks cannot be held on any given day.

Examples:

Input: prices[] = [100, 180, 260, 310, 40, 535, 695]
Output: 865
Explanation: Buy the stock on day 0 and sell it on day 3 => 310 – 100 = 210. Buy the stock on day 4 and sell it on day 6 => 695 – 40 = 655. Maximum Profit = 210 + 655 = 865

'''
from typing import List


class Solution:
    def maximumProfit(self,prices) -> int:
        res = 0
        
        for i in range(0, len(prices)-1):
            if prices  [i+1] > prices[i]:
                res += prices[i+1] - prices[i]
        
        return res
