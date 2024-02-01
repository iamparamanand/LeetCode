class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # result = []
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             result.append(i)
        #             result.append(j)
        # return result

        for i in range(len(nums)):
            comp = target - nums[i]
            test = nums[:i] + nums[i+1:]  
            if comp in test:
                a = test.index(comp)
                return [i, a + 1 if a >= i else a] 