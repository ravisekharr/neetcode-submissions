class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd = 0
        factor = 1
        m,n = len(str1),len(str2)
        for i in range(1,n+1):
            if m%i==0 and n%i==0:
                gcd=i
                factor = m//gcd
        print(gcd)
        if str2[:gcd]*factor==str1:
            return str2[:gcd]
        return ""