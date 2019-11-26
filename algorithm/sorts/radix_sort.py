# =============================================================================
# Author: falseuser
# Created Time: 2019-10-31 16:42:25
# Last modified: 2019-10-31 17:21:40
# Description: 基数排序
# 从待排序项的低位到高位进行多次桶排序
# =============================================================================


def sort(collection):
    RADIX = 10  # 0 - 9
    placement = 1  # 个 十 百 千

    max_value = max(collection)

    while placement < max_value:
        buckets = [[] for i in range(RADIX)]
        for j in collection:
            bit_value = int((j / placement) % RADIX)
            buckets[bit_value].append(j)

        k = 0
        for b in range(RADIX):
            for v in buckets[b]:
                collection[k] = v   # 取出bucket里的值，取出顺序与放入顺序相同
                k = k + 1
        placement = placement * RADIX

    return collection


if __name__ == "__main__":
    collection = [123, 8, 34, 2, 98, 4, 245, 77]
    print(sort(collection))
