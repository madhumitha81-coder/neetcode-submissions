class Solution:
    def reverseBits(self, n: int) -> int:
        a = format(n, '032b')
        b = a[::-1]
        d = int(b, 2)
        return d
        