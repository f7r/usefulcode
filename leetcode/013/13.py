# =============================================================================
# Author: falseuser
# Created Time: 2019-06-27 10:25:54
# Last modified: 2019-06-27 10:32:30
# Description: 13.py
# =============================================================================


class Solution:
    def romanToInt(self, s: str) -> int:
        romanmap = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1,
        }
        roman = s
        roman = roman.replace("CD", "CCCC")
        roman = roman.replace("CM", "DCCCC")
        roman = roman.replace("XL", "XXXX")
        roman = roman.replace("XC", "LXXXX")
        roman = roman.replace("IV", "IIII")
        roman = roman.replace("IX", "VIIII")
        num = 0
        for r in roman:
            if r in romanmap:
                num = num + romanmap[r]
        return num


if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("MCMXCIV"))
