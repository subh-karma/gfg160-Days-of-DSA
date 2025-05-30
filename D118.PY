class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        cost.append(0)
        dp = [-1] * (n+1)

        def recursive(i):
            if i < 0:  # If we go before the first step, cost is 0
                return 0
            if i == 0 or i == 1:
                return cost[i]
            if dp[i] != -1:
                return dp[i]
            dp[i] = min(recursive(i-1), recursive(i-2)) + cost[i]
            return dp[i]

        return recursive(n)
        
