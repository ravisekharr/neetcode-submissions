class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        dct = Counter(nums)
        for i in dct:
            if dct[i]==1:
                return i
        