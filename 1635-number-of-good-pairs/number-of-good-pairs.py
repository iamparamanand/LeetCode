class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # count = 0
        # for i in range(0, len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             count +=1
        # return count

            n: int = len(nums)
            d = {}
            ans = 0
            for x in nums:
                if x in d:
                    ans += d[x]
                d[x] = d.get(x, 0) + 1
            return ans