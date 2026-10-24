class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        c = 0
        s = sorted(heights)
        for i in range(len(s)):
            if heights[i]!=s[i]:
                c+=1
        return c       