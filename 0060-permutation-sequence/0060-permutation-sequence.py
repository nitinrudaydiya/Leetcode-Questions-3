class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import itertools
        return ["".join(i) for i in itertools.permutations("123456789"[:n])][k-1]