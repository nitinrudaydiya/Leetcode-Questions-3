class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        a = 0
        for i in range(start,start+n*2,2):
            a^= i
        return a
            