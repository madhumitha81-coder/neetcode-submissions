class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=""
        for i in s:
            if i>='A' and i<='Z' or i>='a' and i<='z' or i>='0' and i<='9':
                string+=i
        st=string.lower()
        stri=st[::-1]
        for i in range(0,len(st)):
            if(st[i]!=stri[i]):
                return False
        return True