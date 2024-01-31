class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        for i in range(0,len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i]*=2
                nums[i+1]*= 0
            else:
                continue
        k = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                result.insert(k, nums[i])
                k += 1
            elif nums[i] == 0:
                result.insert(n , 0)
                n -= 1
        return result