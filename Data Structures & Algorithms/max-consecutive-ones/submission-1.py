class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = 0
        cnt=0
        for i in nums:
            if i==1:
                cnt+=1
                n=max(n,cnt)
            else:
                cnt=0
        return n