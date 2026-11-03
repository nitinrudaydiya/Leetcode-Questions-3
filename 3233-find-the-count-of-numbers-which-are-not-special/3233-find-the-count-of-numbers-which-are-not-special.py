class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        n = int(r ** 0.5)

        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False

        special = 0

        for i in range(2, n + 1):
            if is_prime[i]:
                square = i * i
                if l <= square <= r:
                    special += 1

        return (r - l + 1) - special