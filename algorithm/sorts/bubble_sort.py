# =============================================================================
# Author: falseuser
# Created Time: 2019-10-28 17:47:26
# Last modified: 2019-10-29 16:07:16
# Description: 冒泡排序
# 从前往后比较，已排序的放在后面
# =============================================================================


def sort(collection):

    # 每次循环的最大值将会被放到最后
    for unsorted in range(len(collection)-1, 0, -1):
        swapped = False
        for i in range(unsorted):
            if collection[i] > collection[i+1]:
                collection[i], collection[i+1] = collection[i+1], collection[i]
                swapped = True
        # 每次循环都没有发生交换才为False，说明已排好序
        if not swapped:
            break
    return collection


if __name__ == "__main__":
    collection = [4, 5, 2, 1, 9, 0]
    print(sort(collection))
