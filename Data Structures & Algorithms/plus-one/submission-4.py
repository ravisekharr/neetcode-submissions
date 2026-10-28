class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)-1
        while n>=0:
            res = digits[n]+1
            if res<=9:
                digits[n] = res
                return digits
            digits[n] = 0
            n-=1
        return [1]+digits
        