class Solution:
    def romanToInt(self, s: str) -> int:
        dct = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        n = len(s)-1
        num = 0
        while n>=0:
            if n-1>=0 and dct[s[n]]>dct[s[n-1]]:
                num+= dct[s[n]]-dct[s[n-1]]
                n-=1
            else:
                num+= dct[s[n]]
            n-=1
            print(num)
        return num