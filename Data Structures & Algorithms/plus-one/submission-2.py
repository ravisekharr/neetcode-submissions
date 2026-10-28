class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)-1
        carry = 1
        while n>=0:
            res = digits[n]+carry
            if res>9:
                digits[n] = 0
                carry = 1
            else:
                digits[n] = res
                carry = 0
                return digits
            n-=1
        if digits[0]==0:
            return [1]+digits
        return digits
        