# =============================================================================
# Author: falseuser
# Created Time: 2019-06-25 11:07:08
# Last modified: 2019-06-25 12:08:27
# Description: 8.py
# =============================================================================


class Solution:
    def myAtoi(self, s: str) -> int:
        nums = []
        ss = s.lstrip()
        if ss == "":
            return 0
        if ss[0] in "+-":
            for b in ss[1:]:
                if b in "0123456789":
                    nums.append(b)
                else:
                    break
        elif ss[0] in "0123456789":
            for b in ss:
                if b in "0123456789":
                    nums.append(b)
                else:
                    break
        else:
            return 0
        res = 0
        for n in nums:
            res = 10 * res + int(n)
        if ss[0] == "-":
            if res < 2**31:
                return -res
            else:
                return - 2**31
        else:
            if res < 2**31 - 1:
                return res
            else:
                return 2**31 - 1


if __name__ == "__main__":
    s = Solution()
    print(s.myAtoi("  -4193 with words"))
