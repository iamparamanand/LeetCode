class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False


        # dict = {}
        # for i in nums:
        #     if i in dict:
        #         return True
        #     dict[i] = 0
        # return False