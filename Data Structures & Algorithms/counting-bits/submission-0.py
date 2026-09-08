class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[]
        for i in range(0,n+1):
            a=format(i,'032b')
            r=self.see(a)
            l.append(r)
        return l
    def see(self,r: str)->int:
        cnt=0
        for i in r:
            if(i=="1"):
                cnt+=1
        return cnt

            
        