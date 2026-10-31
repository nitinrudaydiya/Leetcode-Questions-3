class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        freq = [0] * 60
        c = 0

        for t in time:
            rem = t % 60
            req = (60 - rem) % 60

            c += freq[req]
            freq[rem] += 1

        return c