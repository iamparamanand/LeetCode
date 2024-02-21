class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        map = {}
        sum_val = 0

        for num in nums:
            sum_val += num

            if sum_val == k:
                count += 1

            if sum_val - k in map:
                count += map[sum_val - k]

            map[sum_val] = map.get(sum_val, 0) + 1

        return count