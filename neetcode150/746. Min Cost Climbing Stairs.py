class Solution:
    #n, 1
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        #appending 0 for ez math
        for i in range(len(cost) - 3, -1, -1):
            cost[i] = cost[i] + min(cost[i + 1], cost[i + 2]) # 2 options: one step, two steps
        return min(cost[0], cost[1])