# =============================================================================
# Author: falseuser
# Created Time: 2019-01-09 17:39:05
# Last modified: 2019-01-09 17:51:37
# Description: display.py
# =============================================================================
import sys
import time


def enhanced_print(
        string, fg_color, bg_color="", bold=False,
        underscore=False, blink=False, reverse=False):
    # Print enhanced.
    fg_color_code_map = {
        "black": 30, "red": 31, "green": 32, "yellow": 33,
        "blue": 34, "magenta": 35, "cyan": 36, "white": 37,
    }
    bg_color_code_map = {
        "black": 40, "red": 41, "green": 42, "yellow": 43,
        "blue": 44, "magenta": 45, "cyan": 46, "white": 47,
    }
    code_list = []
    # Foreground colors.
    if fg_color in fg_color_code_map:
        fg_color_code = fg_color_code_map[fg_color]
        code_list.append(fg_color_code)
    # Background colors
    if bg_color in bg_color_code_map:
        bg_color_code = bg_color_code_map[bg_color]
        code_list.append(bg_color_code)
    # Text attributes
    if bold:
        code_list.append(1)
    if underscore:
        code_list.append(4)
    if blink:
        code_list.append(5)
    if reverse:
        code_list.append(7)
    code = "0"
    for i in code_list:
        code = code + ";" + str(i)
    enhanced_string = "\033[{0}m{1}\033[0m".format(code, string)
    sys.stdout.write(enhanced_string)
    # line break
    print()


# 输出数字进度符

def printpi(percent):
    # Print progress indicator.
    time.sleep(0.1)
    string = "\033[1000D{0}%\033[0m".format(percent)
    sys.stdout.write(string)
    sys.stdout.flush()
    if percent == 100:
        print()

# 输出进度条


def printpb(percent):
    # Print progress bar.
    time.sleep(0.1)
    width = int(percent / 4)
    bar = "[" + "#" * width + " " * (25 - width) + "]"
    string = "\033[1000D{0}\033[0m".format(bar)
    sys.stdout.write(string)
    sys.stdout.flush()
    if percent == 100:
        print()


if __name__ == "__main__":
    enhanced_print("11111111111", "red")
