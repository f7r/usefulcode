# =============================================================================
# Author: falseuser
# Created Time: 2019-06-26 15:55:19
# Last modified: 2019-06-26 18:05:46
# Description: 12.py
# =============================================================================


class Solution:
    def intToRoman(self, num: int) -> str:
        RomeMap = {
            "M": num // 1000,
            "D": (num % 1000) // 500,
            "C": (num % 500) // 100,
            "L": (num % 100) // 50,
            "X": (num % 50) // 10,
            "V": (num % 10) // 5,
            "I": num % 5 // 1,
        }
        RomeList = ["M", "D", "C", "L", "X", "V", "I"]
        Roman = ""
        for r in RomeList:
            if RomeMap[r] == 0:
                continue
            else:
                for i in range(RomeMap[r]):
                    Roman = Roman + r
        Roman = Roman.replace("DCCCC", "CM")  # 900
        Roman = Roman.replace("CCCC", "CD")  # 400
        Roman = Roman.replace("LXXXX", "XC")  # 90
        Roman = Roman.replace("XXXX", "XL")  # 40
        Roman = Roman.replace("VIIII", "IX")  # 9
        Roman = Roman.replace("IIII", "IV")  # 4
        return Roman


if __name__ == "__main__":
    s = Solution()
    print(s.intToRoman(1994))
