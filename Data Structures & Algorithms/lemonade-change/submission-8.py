class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        purse={5:0,10:0}
        for i in bills:
            print(i,purse)
            if i==5:
                purse[5]+=1
            elif (i==10 and purse[5]>0):
                purse[5]-=1
                purse[10]+=1
            elif (i==20 and purse[5]>=1 and purse[10]>=1):
                purse[5]-=1
                purse[10]-=1
            elif (i==20 and purse[5]>=3):
                purse[5]-=3
            else:
                return False
        return True

            