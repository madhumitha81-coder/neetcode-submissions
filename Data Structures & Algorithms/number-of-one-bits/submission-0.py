class Solution:
    def hammingWeight(self, n: int) -> int:
        a=format(n,'032b')
        b=str(a)
        cnt=0
        for i in b:
            if(i=="1"):
                cnt+=1
        return cnt
        