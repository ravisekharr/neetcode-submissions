class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = []
        last_max = 0
        for i in range(n-1,-1,-1):
            if i==n-1:
                res.append(-1)
            else:
                last_max = max(last_max,arr[i+1])
                res.append(last_max)
        return res[::-1]



        