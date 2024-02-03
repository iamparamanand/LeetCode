class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        nums = nums1 + nums2
        nums.sort()
        if (m+n) % 2 == 0:
            mid = int((m + n) / 2)
            median = (nums[mid] + nums[mid - 1]) / 2
        else:
            mid = int((m + n) / 2)
            print(mid)
            median = nums[mid]

        return median