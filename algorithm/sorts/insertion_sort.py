# =============================================================================
# Author: falseuser
# Created Time: 2019-10-29 15:50:52
# Last modified: 2019-10-29 16:06:37
# Description: 插入排序
# 从后向前比较，已排序的放在前面
# =============================================================================


def sort(collection):
    # 从第二项开始，每次和前面的项作比较
    for index in range(1, len(collection)):
        value = collection[index]
        index2 = index  # 移动索引
        while index2 > 0 and collection[index2-1] > value:
            collection[index2] = collection[index2-1]  # 值向后移位
            index2 = index2 - 1
        collection[index2] = value  # 插入
    return collection


if __name__ == "__main__":
    collection = [3, 5, 1, 3, 6, 4, 9, 7]
    print(sort(collection))
