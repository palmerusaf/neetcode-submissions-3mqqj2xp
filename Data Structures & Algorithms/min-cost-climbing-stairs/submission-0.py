class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        m={}
        def dfs(i):
            if i >= len(cost):
                return 0
            if i in m:
                return m[i]
            m[i]=cost[i]+min(dfs(i+1),dfs(i+2))
            return m[i]
        return min(dfs(0),dfs(1))