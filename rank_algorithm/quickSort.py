#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：deep-learning-tools 
@File    ：quickSort.py
@IDE     ：PyCharm 
@Author  ：何锦涛
@Date    ：2022/5/14 00:11 
"""


def partition(nums, l, r):
    target = nums[l]
    while l != r:
        while l < r and target <= nums[r]:
            r -= 1
        nums[l] = nums[r]
        while l < r and target > nums[l]:
            l += 1
        nums[r] = nums[l]
    nums[l] = target
    return l


def quickSort(nums, l, r):
    if l < r:
        key = partition(nums, l, r)
        quickSort(nums, l, key-1)
        quickSort(nums, key+1, r)
    return nums


if __name__ == '__main__':
    nums = [3, 1, 4, 2, 5]
    print(quickSort(nums, 0, len(nums) - 1))
    # print(nums)
