class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # nums.sort()
        # res, quad = [], []
        # def kSum(k, start, target):
        #     if k != 2:
        #         for i in range(0, len(nums) - k + 1):
        #             if i > start and nums[i] == nums[i-1]:
        #                 continue
        #             quad.append(nums[i])
        #             kSum(k - 1, i + 1, target - nums[i])
        #             quad.pop()
        #         return
        #     #Base case for two sum II
        #     l, r = start, len(nums) - 1
        #     while l < r:
        #         if nums[l] + nums[r] < target:
        #             l += 1
        #         elif nums[l] + nums[r] > target:
        #             r -= 1
        #         else:
        #             res.append(quad+ [nums[l], nums[r]])
        #             l += 1
        #             while l < r and nums[l] == nums[l - 1]:
        #                 l += 1
        # kSum(4, 0, target)
        # return res
        
        n = len(nums)
        nums.sort()
        res = []

        for i in range(n-3):
            # avoid the duplicates while moving i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1, n-2):
                # avoid the duplicates while moving j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                lo = j + 1
                hi = n - 1
                while lo < hi:
                    temp = nums[i] + nums[j] + nums[lo] + nums[hi]
                    if temp == target:
                        res += [nums[i], nums[j], nums[lo], nums[hi]],

                        # skip duplicates
                        while lo < hi and nums[lo] == nums[lo + 1]:
                            lo += 1
                        lo += 1
                        while lo < hi and nums[hi] == nums[hi - 1]:
                            hi -= 1
                        hi -= 1
                    elif temp < target:
                        lo += 1
                    else:
                        hi -= 1
        return res