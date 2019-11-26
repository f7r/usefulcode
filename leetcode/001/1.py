# =============================================================================
# Author: falseuser
# Created Time: 2019-06-20 09:58:20
# Last modified: 2019-06-20 11:00:17
# Description: 1.py
# =============================================================================
class Solution:

    def twoSum1(self, nums: list, target: int) -> list:
        for i in nums:
            for k in nums:
                if i + k == target and nums.index(i) != nums.index(k):
                    return [nums.index(i), nums.index(k)]

    def twoSum2(self, nums: list, target: int) -> list:
        d = {}
        i = 0
        for j in nums:
            d[j] = i
            i += 1
        for k in d:
            if target - k in d and d[k] != d[target - k]:
                return [d[k], d[target - k]]

    def twoSum3(self, nums: list, target: int) -> list:
        d = {}
        i = 0
        for j in nums:
            if target - j in d and i != d[target - j]:
                return [d[target - j], i]
            else:
                d[j] = i
                i += 1


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum1([2,7,11,15], 9))
    print(s.twoSum2([2,7,11,15], 9))
    print(s.twoSum3([2,7,11,15], 9))
