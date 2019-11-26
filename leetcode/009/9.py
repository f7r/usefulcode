# =============================================================================
# Author: falseuser
# Created Time: 2019-06-25 12:09:17
# Last modified: 2019-06-25 14:47:57
# Description: 9.py
# =============================================================================


class Solution:
    def isPalindrome1(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            y = x
            z = 0
            while y != 0:
                z = z * 10 + y % 10
                y = y // 10
            if z == x:
                return True
            else:
                return False

    def isPalindrome2(self, x: int) -> bool:
        if x < 0 or not x % 10 and x:  # 以0结尾的非0整数
            return False
        else:
            y = x
            z = 0
            while y > z:
                z = z * 10 + y % 10
                y = y // 10
            if z//10 == y or z == y:
                return True
            else:
                return False


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome1(123321))
    print(s.isPalindrome2(10))
    print(s.isPalindrome2(0))
    print(s.isPalindrome2(11))
