class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        # c = 0
        # for i in range(len(arr)):
        #     for j in range(i+1,len(arr)+1):
        #         if sum(arr[i:j])%2 != 0:
        #             c+=1
        # return c


        odd = 0
        even = 1
        prefix = 0
        mod = 10**9 + 7

        for num in arr:
            prefix += num

            if prefix % 2 == 0:
                even += 1
            else:
                odd += 1

        return (odd * even) % mod