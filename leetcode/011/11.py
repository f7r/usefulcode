# =============================================================================
# Author: falseuser
# Created Time: 2019-06-26 14:22:03
# Last modified: 2019-06-26 15:41:28
# Description: 11.py
# =============================================================================


class Solution:
    def maxArea(self, height: list) -> int:
        size = len(height)
        left = 0
        right = size - 1
        area = 0
        while left < right:
            cur_area = (right - left) * min(height[left], height[right])
            if cur_area > area:
                area = cur_area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return area


if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))
