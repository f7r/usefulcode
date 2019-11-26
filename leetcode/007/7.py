# =============================================================================
# Author: falseuser
# Created Time: 2019-06-24 17:58:30
# Last modified: 2019-06-25 11:09:56
# Description: 7.py
# =============================================================================


class Solution:
    def reverse(self, x: int) -> int:
        nums = []
        if x > 0:
            of = 2 ** 31 - 1
            nums.append(1)
        elif x < 0:
            of = 2 ** 31
            nums.append(0)
        else:
            return 0
        bits = len(str(abs(x)))
        x = abs(x)
        res = 0
        for i in range(bits):
            x, num = divmod(x, 10)
            nums.append(num)
        for j in nums[1:]:
            res = res * 10 + j
        if res > of:
            return 0
        if nums[0] == 1:
            return res
        else:
            return -res


if __name__ == "__main__":
    s = Solution()
    print(s.reverse(-1230))
