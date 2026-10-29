class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        judge={}
        sub_judge={}
        for i in range(1,n+1):
            judge[i]=[]
            sub_judge[i]=[]
        n1 = len(trust)
        if n1<n-1:
            return -1
        for i in trust:
            a,b=i[0],i[1]
            judge[b]=judge[b]+[a]
            sub_judge[a]=sub_judge[a]+[b]
        for i in judge:
            if len(judge[i])==n-1 and len(sub_judge[i])==0:
                return i
        return -1