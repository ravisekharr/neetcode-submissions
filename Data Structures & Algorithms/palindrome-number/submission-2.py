class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        original=x
        while x>0:
            rev = (rev*10)+(x%10)
            x=x//10
        if original==rev:
            return True
        return False
        