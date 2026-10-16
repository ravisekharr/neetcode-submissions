class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct={}
        for i,val in enumerate(nums):
            if target-val in dct:
                return [dct[target-val],i]
            dct[val] = i