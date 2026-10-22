class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]
        stones = sorted(stones)
        last = stones.pop()
        stones[-1] = abs(stones[-1]-last)
        return self.lastStoneWeight(stones)