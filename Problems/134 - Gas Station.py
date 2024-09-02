class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1

        tank = 0
        n = len(gas)
        res = 0
        for i,x in enumerate(gas):
            tank += x
            tank -= cost[i]
            if tank < 0:
                tank = 0
                res = i + 1
            #print(tank,res)
        return res
