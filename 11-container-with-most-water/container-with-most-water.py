class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            if height[left] < height[right]:
                area = min(height[left], height[right]) * (right - left)
                max_area = max(max_area, area)
                left += 1
            else:
                area = min(height[left], height[right]) * (right - left)
                max_area = max(max_area, area)
                right -= 1
        return max_area

    #Brute-Force Solution
        # h = len(height)
        # max_area = 0
        # for left in range(h - 1):
        #     for right in range(left + 1, h):
        #         area = min(height[left], height[right]) * (right -left)
        #         max_area = max(max_area , area)
        # return max_area

