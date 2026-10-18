class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        majority = (n//2)+1
        from collections import Counter
        counts = Counter(nums)
        for i in counts:
            if counts[i]>=majority:
                return i