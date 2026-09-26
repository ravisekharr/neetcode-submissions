class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [0]*n
        last_max = -1
        for i in range(n-1,-1,-1):
            res[i]=last_max
            last_max = max(last_max,arr[i])
        return res



        