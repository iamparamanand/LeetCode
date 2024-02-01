class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i + n])
        return ans

        
        # list = []
        # for i in range(0, n):
        #     list.append(nums[i])
        #     list.append(nums[n])
        #     n += 1
        # return list