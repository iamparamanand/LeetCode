class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        list = []
        for i in range(0, n):
            list.append(nums[i])
            list.append(nums[n])
            n += 1
        return list