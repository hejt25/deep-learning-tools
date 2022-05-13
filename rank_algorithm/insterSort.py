#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：deep-learning-tools 
@File    ：insterSort.py
@IDE     ：PyCharm 
@Author  ：何锦涛
@Date    ：2022/5/13 23:32 
"""


def insertSort(nums):
    # 插入排序，向前遍历找到当前位置的元素对应的索引
    n = len(nums)
    for i in range(1, n):
        target = nums[i]
        j = i - 1
        while j >= 0 and target < nums[j]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
            j -= 1
        # nums[j] = target
    return nums


if __name__ == '__main__':
    nums = [11, 4, 3, 2, 12]
    print(insertSort(nums))
