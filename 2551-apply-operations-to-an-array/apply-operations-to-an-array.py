class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(0,len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i]*=2
                nums[i+1]*= 0
            else:
                continue
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == 0 and nums[j] !=0:
                    nums[i],nums[j] = nums[j], nums[i]
        return nums