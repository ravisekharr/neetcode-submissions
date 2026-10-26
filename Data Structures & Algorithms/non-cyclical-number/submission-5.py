class Solution:
    def isHappy(self, n: int) -> bool:
        dct=set()
        while n!=1:
            s = 0
            while n>0:
                m = n%10
                s+= m**2
                n = n//10
            n = s
            if n in dct:
                return False
            else:
                dct.add(n)
        return True