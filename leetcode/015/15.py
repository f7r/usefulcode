# =============================================================================
# Author: falseuser
# Created Time: 2019-06-27 15:25:04
# Last modified: 2019-06-28 10:30:13
# Description: 15.py
# =============================================================================


class Solution:
    def threeSum(self, nums: list) -> list:
        nums.sort()
        n = len(nums)
        res = []
        #print(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if cur_sum == 0:
                    tmp = [nums[i],nums[left],nums[right]]
                    res.append(tmp)
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif cur_sum > 0:
                    right -= 1
                else:
                    left += 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
