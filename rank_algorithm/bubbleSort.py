#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：deep-learning-tools 
@File    ：bubbleSort.py
@IDE     ：PyCharm 
@Author  ：何锦涛
@Date    ：2022/5/13 23:14 
"""


def bubbleSort(nums):
    n = len(nums)
    for i in range(n):
        # 找到第i+1大的数
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


if __name__ == '__main__':
    nums = [2, 5, 6, 7, 3]
    print(bubbleSort(nums))
