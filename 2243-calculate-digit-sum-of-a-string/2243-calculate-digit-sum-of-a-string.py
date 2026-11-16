
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        # while len(s) > k:
        #     ans = ""

        #     for i in range(0, len(s), k):
        #         group = s[i:i+k]
        #         total = 0

        #         for j in group:
        #             total += int(j)

        #         ans += str(total)

        #     s = ans

        # return s

        while len(s) > k:
            s = ''.join(str(sum(map(int, s[i:i+k]))) for i in range(0, len(s), k))

        return s
