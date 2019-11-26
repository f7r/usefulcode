# =============================================================================
# Author: falseuser
# Created Time: 2019-06-20 11:22:43
# Last modified: 2019-06-20 14:49:24
# Description: 2.py
# =============================================================================


class Solution:

    def addTwoNumbers1(self, l1: list, l2: list) -> list:
        res = []
        carry = 0
        if len(l1) > len(l2):
            short = l2
        elif len(l1) < len(l2):
            short = l1
        for i in range(abs(len(l1)-len(l2))):
            short.append(0)
        for i in range(len(l1)):
            l1[i] = l1[i] + carry
            r = l1[i] + l2[i]
            carry, mod = divmod(r, 10)
            res.append(mod)
        if carry == 1:
            res.append(1)
        return res

    def addTwoNumbers2(self, l1: list, l2: list) -> list:
        res = []
        carry = 0
        times = min(len(l1), len(l2))
        for i in range(times):
            l1[i] = l1[i] + carry
            r = l1[i] + l2[i]
            carry, mod = divmod(r, 10)
            res.append(mod)
        if len(l1) > len(l2):
            l1[i+1] = l1[i+1] + carry
            res.extend(l1[i+1:])
        elif len(l1) < len(l2):
            l2[i+1] = l2[i+1] + carry
            res.extend(l2[i+1:])
        else:
            if carry == 1:
                res.append(1)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.addTwoNumbers2([2,4,3], [5,6,4]))
