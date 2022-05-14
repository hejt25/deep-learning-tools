#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：deep-learning-tools 
@File    ：mergeSort.py
@IDE     ：PyCharm 
@Author  ：hejintao
@Date    ：2022/5/14 22:21 
"""


def mergeSort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    return merge(left, right)


def merge(left, right):
    res = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    res += left[l:]
    res += right[r:]
    return res


if __name__ == '__main__':
    nums = [1, 4, 3, 5, 2, 9]
    print(mergeSort(nums))
